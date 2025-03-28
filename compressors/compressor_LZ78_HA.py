import os

from base_algorithms.HA import ha_compress, ha_decompress
from base_algorithms.LZ78 import lz78_compress, lz78_decompress
from lib.start_compression_decompression import start_compression_decompression


def compressor_lz78_ha(input_path: str, compressed_path: str, decompressed_path: str, part_of_another_compressor: bool):
    lz78_compress_path = start_compression_decompression(input_path, compressed_path, lz78_compress)
    lz78_ha_compress_path = start_compression_decompression(lz78_compress_path, compressed_path, ha_compress)

    path_lz78_decompress = start_compression_decompression(lz78_ha_compress_path, decompressed_path, ha_decompress)
    path_lz78_ha_decompress = start_compression_decompression(path_lz78_decompress, decompressed_path, lz78_decompress)

    input_size = os.path.getsize(input_path)
    compressed_size = os.path.getsize(compressed_path)
    decompressed_size = os.path.getsize(decompressed_path)

    print(f"Исходный размер LZ78_HA файла: {input_size} байт")
    print(f"Сжатый размер файла LZ78_HA: {compressed_size} байт")
    print(f"Разжатый размер файла LZ78_HA: {decompressed_size} байт")

    return lz78_ha_compress_path
