from pandas import Series
from time import perf_counter_ns
from helper.constants import cols


def benchmark(algo, results):
    raw_bytes = bytes("I am the bytes of an image file", "utf-8")

    # time compression
    compress_start = perf_counter_ns()
    compressed_bytes = algo.compress(raw_bytes)
    compress_end = perf_counter_ns()

    # time decompression
    decompress_start = perf_counter_ns()
    decompressed_bytes = algo.decompress(compressed_bytes)
    decompress_end = perf_counter_ns()

    # record results
    result = Series([
        algo.__name__.split(".")[1],
        compress_end - compress_start,
        decompress_end - decompress_start,
        len(raw_bytes) / len(compressed_bytes)
    ], index=cols)
    return results.append(result, ignore_index=True)
