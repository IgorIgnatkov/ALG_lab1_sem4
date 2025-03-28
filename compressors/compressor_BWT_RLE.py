import os

from base_algorithms.BWT import bwt_compress, bwt_decompress
from base_algorithms.RLE import rle_compress, rle_decompress
from lib.start_compression_decompression import start_compression_decompression


def compressor_bwt_rle(input_path: str, compressed_path: str, decompressed_path: str, part_of_another_compressor: bool):
    bwt_compress_path = start_compression_decompression(input_path, compressed_path, bwt_compress)
    bwt_rle_compress_path = start_compression_decompression(bwt_compress_path, compressed_path, rle_compress)

    path_rle_decompress = start_compression_decompression(bwt_rle_compress_path, decompressed_path, rle_decompress)
    path_bwt_rle_decompress = start_compression_decompression(path_rle_decompress, decompressed_path, bwt_decompress)

    input_size = os.path.getsize(input_path)
    compressed_size = os.path.getsize(compressed_path)
    decompressed_size = os.path.getsize(decompressed_path)

    print(f"Исходный размер BWT_RLE файла: {input_size} байт")
    print(f"Сжатый размер файла BWT_RLE: {compressed_size} байт")
    print(f"Разжатый размер файла BWT_RLE: {decompressed_size} байт")

    return bwt_rle_compress_path
