import struct

CHUNK_SIZE = 1000
END_OF_BLOCK_MARKER = b'\x01'

def create_suffix_array(data: bytes):
    return sorted(
        range(len(data)),
        key=lambda index: data[index:]
    )

def bwt_compress(input_data: bytes) -> bytes:
    input_data += END_OF_BLOCK_MARKER
    suffix_array = create_suffix_array(input_data)
    original_index = suffix_array.index(0)
    bwt_transformed = bytearray(input_data[i - 1] if i > 0 else input_data[-1] for i in suffix_array)
    compressed_data = struct.pack('I', original_index) + bwt_transformed
    return compressed_data

def bwt_decompress(compressed_data: bytes) -> bytes:
    if len(compressed_data) < 5:
        raise ValueError("Некорректные данные: слишком короткий блок")

    original_index = struct.unpack('I', compressed_data[:4])[0]
    bwt_transformed = compressed_data[4:]
    data_length = len(bwt_transformed)

    if original_index >= data_length:
        raise ValueError(f"Ошибка индекса: original_index {original_index} >= {data_length}")

    byte_count = [0] * 256
    for byte in bwt_transformed:
        byte_count[byte] += 1

    total = 0
    first_column_positions = [0] * 256
    for i in range(256):
        first_column_positions[i] = total
        total += byte_count[i]

    rank = [0] * data_length
    seen = [0] * 256
    for i in range(data_length):
        rank[i] = first_column_positions[bwt_transformed[i]] + seen[bwt_transformed[i]]
        seen[bwt_transformed[i]] += 1

    original_data = bytearray(data_length)
    current_index = original_index
    for i in range(data_length - 1, -1, -1):
        if current_index >= data_length:
            raise ValueError(f"Ошибка ранга: current_index {current_index} >= {data_length} (i={i})")
        original_data[i] = bwt_transformed[current_index]
        current_index = rank[current_index]

    decompressed_data = bytes(original_data).rstrip(END_OF_BLOCK_MARKER)
    return decompressed_data
