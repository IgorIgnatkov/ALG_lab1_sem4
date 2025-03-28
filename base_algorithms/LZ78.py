import struct

def lz78_compress(input_data: bytes):
    dictionary = {}
    compressed_data = bytearray()
    current_index, dictionary_size = 0, 1
    current_buffer = bytearray()

    while current_index < len(input_data):
        current_buffer.append(input_data[current_index])

        if bytes(current_buffer) not in dictionary:
            dictionary[bytes(current_buffer)] = dictionary_size
            prefix_index = dictionary.get(bytes(current_buffer[:-1]), 0)
            compressed_data.extend(struct.pack(">IB", prefix_index, current_buffer[-1]))
            dictionary_size += 1
            current_buffer.clear()

        current_index += 1

    return compressed_data

def lz78_decompress(compressed_data: bytes):
    dictionary = {0: b""}
    decompressed_data = bytearray()
    current_index, dictionary_size = 0, 1

    while current_index < len(compressed_data):
        prefix_index, char = struct.unpack(">IB", compressed_data[current_index:current_index+5])
        current_index += 5

        new_entry = dictionary[prefix_index] + bytes([char])
        dictionary[dictionary_size] = new_entry
        dictionary_size += 1

        decompressed_data.extend(new_entry)

    return bytes(decompressed_data)
