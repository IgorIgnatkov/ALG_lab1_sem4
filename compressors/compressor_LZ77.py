import os

from base_algorithms.LZ77 import lz77_compress, lz77_decompress
from lib.start_compression_decompression import start_compression_decompression


def compressor_lz77(input_path: str, compressed_path: str, decompressed_path: str, part_of_another_compressor: bool):
    start_compression_decompression(input_path, compressed_path, lz77_compress)
    start_compression_decompression(compressed_path, decompressed_path, lz77_decompress)

    input_size = os.path.getsize(input_path)
    compressed_size = os.path.getsize(compressed_path)
    decompressed_size = os.path.getsize(decompressed_path)

    if not(part_of_another_compressor):
        print(f"Исходный размер LZ77 файла: {input_size} байт")
        print(f"Сжатый размер файла LZ77: {compressed_size} байт")
        print(f"Разжатый размер файла LZ77: {decompressed_size} байт")

    return compressed_path
