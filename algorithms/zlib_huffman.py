import zlib as z


def compress(data):
    compressor = z.compressobj(strategy=z.Z_HUFFMAN_ONLY)
    return compressor.compress(data) + compressor.flush()


def decompress(compressed_data):
    return z.decompress(compressed_data)
