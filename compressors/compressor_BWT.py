import os

from base_algorithms.BWT import bwt_compress, bwt_decompress
from lib.start_compression_decompression import start_compression_decompression


def compressor_bwt(input_path: str, compressed_path: str, decompressed_path: str, part_of_another_compressor: bool):
    start_compression_decompression(input_path, compressed_path, bwt_compress)
    start_compression_decompression(compressed_path, decompressed_path, bwt_decompress)

    input_size = os.path.getsize(input_path)
    compressed_size = os.path.getsize(compressed_path)
    decompressed_size = os.path.getsize(decompressed_path)

    if not(part_of_another_compressor):
        print(f"Исходный размер BWT файла: {input_size} байт")
        print(f"Сжатый размер файла BWT: {compressed_size} байт")
        print(f"Разжатый размер файла BWT: {decompressed_size} байт")

    return compressed_path
