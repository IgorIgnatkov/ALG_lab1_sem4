def rle_compress(data: bytes) -> bytes:
    compressed_output = []
    repeat_count = 1

    for current_index in range(1, len(data)):
        if data[current_index] == data[current_index - 1] and repeat_count < 127:
            repeat_count += 1
        else:
            while repeat_count > 127:
                compressed_output.append(0x80 | 127)
                compressed_output.append(data[current_index - 1])
                repeat_count -= 127
            compressed_output.append(0x80 | repeat_count)
            compressed_output.append(data[current_index - 1])
            repeat_count = 1

    while repeat_count > 127:
        compressed_output.append(0x80 | 127)
        compressed_output.append(data[-1])
        repeat_count -= 127

    compressed_output.append(0x80 | repeat_count)
    compressed_output.append(data[-1])

    return bytes(compressed_output)

def rle_decompress(encoded_data: bytes) -> bytes:
    decompressed_output = bytearray()
    current_position = 0
    data_length = len(encoded_data)

    while current_position < data_length:
        count = encoded_data[current_position]
        current_position += 1

        if count & 0x80:
            count &= 0x7F
            byte_value = encoded_data[current_position]
            current_position += 1
            decompressed_output.extend([byte_value] * count)
        else:
            decompressed_output.append(encoded_data[current_position])
            current_position += 1

    return bytes(decompressed_output)
