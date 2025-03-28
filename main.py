from compressors.compress_BWT_MTF import compressor_bwt_mtf
from compressors.compress_HA import compressor_ha
from compressors.compressor_BWT import compressor_bwt
from compressors.compressor_BWT_MTF_HA import compressor_bwt_mtf_ha
from compressors.compressor_BWT_MTF_RLE_HA import compressor_bwt_mtf_rle_ha
from compressors.compressor_BWT_RLE import compressor_bwt_rle
from compressors.compressor_LZ77 import compressor_lz77
from compressors.compressor_LZ77_HA import compressor_lz77_ha
from compressors.compressor_LZ78 import compressor_lz78
from compressors.compressor_LZ78_HA import compressor_lz78_ha
from compressors.compressor_MTF import compressor_mtf
from compressors.compressor_RLE import compressor_rle


def main():
    input_files = [
        r"common/original/enwik7.txt",
        r"common/original/Отцы_и_дети.txt",
        r"common/original/grey_image.raw",
        r"common/original/color_image.raw",
        r"common/original/black_white_image.raw",
        r"common/original/file.exe",
    ]

    compressor_ha(input_files[0], r"common/compressed/HA_compressed.txt", r"common/decompressed/HA_compressed.txt", False)
    compressor_bwt(input_files[0], r"common/compressed/BWT_compressed.txt", r"common/decompressed/BWT_compressed.txt", False)
    compressor_rle(input_files[0], r"common/compressed/RLE_compressed.txt", r"common/decompressed/RLE_compressed.txt", False)
    compressor_lz77(input_files[0], r"common/compressed/LZ77_compressed.txt", r"common/decompressed/LZ77_compressed.txt", False)
    compressor_lz78(input_files[0], r"common/compressed/LZ78_compressed.txt", r"common/decompressed/LZ78_compressed.txt", False)
    compressor_mtf(input_files[0], r"common/compressed/MTF_compressed.txt",r"common/decompressed/MTF_compressed.txt", False)

    compressor_bwt_rle(input_files[0], r"common/compressed/BWT_RLE_compressed.txt", r"common/decompressed/BWT_RLE_compressed.txt", True)
    compressor_bwt_mtf_ha(input_files[0], r"common/compressed/BWT_MTF_HA_compressed.txt", r"common/decompressed/BWT_MTF_HA_compressed.txt", True)
    compressor_bwt_mtf_rle_ha(input_files[0], r"common/compressed/BWT_MTF_RLE_HA_compressed.txt", r"common/decompressed/BWT_MTF_RLE_HA_compressed.txt", True)
    compressor_lz77_ha(input_files[0], r"common/compressed/LZ77_HA_compressed.txt",r"common/decompressed/LZ77_HA_compressed.txt", True)
    compressor_lz78_ha(input_files[0], r"common/compressed/LZ78_HA_compressed.txt",r"common/decompressed/LZ78_HA_compressed.txt", True)
    compressor_bwt_mtf(input_files[0], r"common/compressed/BWT_MTF_compressed.txt",r"common/decompressed/BWT_MTF_compressed.txt", True)

if __name__ == "__main__":
    main()
