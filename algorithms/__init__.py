from algorithms import bzip2, rle, zlib, lzw, zlib_huffman
import algorithms.lzw as lzw_module

lzw_algorithms = [
    lzw,
    lzw_module.make_benchmarkable_algorithm(bit_max_width=16),
    lzw_module.make_benchmarkable_algorithm(bit_max_width=32),
]
huffman = zlib_huffman.make_benchmarkable_algorithm()

ALGORITHMS = [
    bzip2,
    rle,
    zlib,
    *lzw_algorithms,
    huffman,
]
