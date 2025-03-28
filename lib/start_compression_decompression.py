CHUNK_SIZE = 1024

def start_compression_decompression(input_path: str, compressed_decompressed_path: str, compression_function):
    with open(input_path, 'rb') as input_file, open(compressed_decompressed_path, 'wb') as output_file:
        while chunk := input_file.read(CHUNK_SIZE):
            processed_chunk = compression_function(chunk)
            with open(input_path, 'w'):
                pass
            output_file.write(processed_chunk)
    return compressed_decompressed_path
