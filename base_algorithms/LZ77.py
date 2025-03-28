import struct

def lz77_compress(input_data: bytes, window_size=4096, lookahead_buffer_size=18):
    compressed_data = bytearray()
    current_index = 0

    while current_index < len(input_data):
        offset, length_of_match = 0, 0
        search_start = max(0, current_index - window_size)

        for match_length in range(1, min(lookahead_buffer_size, len(input_data) - current_index) + 1):
            sequence = input_data[current_index:current_index + match_length]
            position = input_data[search_start:current_index].rfind(sequence)

            if position != -1:
                offset = current_index - (search_start + position)
                length_of_match = match_length
            else:
                break

        next_char = input_data[current_index + length_of_match] if current_index + length_of_match < len(input_data) else 0
        compressed_data.extend(struct.pack(">HB", offset, length_of_match) + bytes([next_char]))
        current_index += length_of_match + 1

    return compressed_data

def lz77_decompress(compressed_data: bytes):
    decompressed_data = bytearray()
    current_index = 0

    while current_index < len(compressed_data):
        offset, length_of_match = struct.unpack(">HB", compressed_data[current_index:current_index+3])
        next_char = compressed_data[current_index+3]
        current_index += 4

        start_position = len(decompressed_data) - offset
        for j in range(length_of_match):
            decompressed_data.append(decompressed_data[start_position + j])

        if next_char:
            decompressed_data.append(next_char)

    return bytes(decompressed_data)
