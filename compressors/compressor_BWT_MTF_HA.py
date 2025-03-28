import os

from base_algorithms.BWT import bwt_compress, bwt_decompress
from base_algorithms.HA import ha_compress, ha_decompress
from base_algorithms.MTF import mtf_compress, mtf_decompress
from lib.start_compression_decompression import start_compression_decompression


def compressor_bwt_mtf_ha(input_path: str, compressed_path: str, decompressed_path: str, part_of_another_compressor: bool):
    bwt_compress_path = start_compression_decompression(input_path, compressed_path, bwt_compress)
    bwt_mtf_compress_path = start_compression_decompression(bwt_compress_path, compressed_path, mtf_compress)
    bwt_mtf_ha_compress_path = start_compression_decompression(bwt_mtf_compress_path, compressed_path, ha_compress)

    bwt_decompress_path = start_compression_decompression(bwt_mtf_ha_compress_path, decompressed_path, bwt_decompress)
    bwt_mtf_decompress_path = start_compression_decompression(bwt_decompress_path, decompressed_path, mtf_decompress)
    bwt_mtf_ha_decompress_path = start_compression_decompression(bwt_mtf_decompress_path, decompressed_path, ha_decompress)

    input_size = os.path.getsize(input_path)
    compressed_size = os.path.getsize(compressed_path)
    decompressed_size = os.path.getsize(decompressed_path)

    print(f"Исходный размер BWT_MTF_HA файла: {input_size} байт")
    print(f"Сжатый размер файла BWT_MTF_HA: {compressed_size} байт")
    print(f"Разжатый размер файла BWT_MTF_HA: {decompressed_size} байт")

    return bwt_mtf_ha_compress_path
