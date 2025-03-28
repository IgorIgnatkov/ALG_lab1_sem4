def mtf_compress(data: bytes) -> bytes:
    symbol_list = list(range(256))
    compressed_output = []

    for byte in data:
        index = symbol_list.index(byte)
        compressed_output.append(index)
        symbol_list.pop(index)
        symbol_list.insert(0, byte)

    return bytes(compressed_output)

def mtf_decompress(data: bytes) -> bytes:
    symbol_list = list(range(256))
    decompressed_output = []

    for index in data:
        symbol = symbol_list[index]
        decompressed_output.append(symbol)
        symbol_list.pop(index)
        symbol_list.insert(0, symbol)

    return bytes(decompressed_output)
