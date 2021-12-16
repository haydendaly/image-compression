import zlib as z
from algorithms.utils import AlgorithmModule


def compress(data):
    compressor = z.compressobj(strategy=z.Z_HUFFMAN_ONLY)
    return compressor.compress(data) + compressor.flush()


def decompress(compressed_data):
    return z.decompress(compressed_data)


def make_benchmarkable_algorithm():
    name = "algorithms.zlib_huffman"
    return AlgorithmModule({"compress": compress, "decompress": decompress}, name=name)
