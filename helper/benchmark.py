from pandas import Series
from time import perf_counter_ns
from helper.constants import cols
from PIL import Image
import io


def benchmark(algo, results): 
    image = Image.open("images/rgb8bit/artificial.ppm")
    imgByteArr = io.BytesIO()
    image.save(imgByteArr, format=image.format)
    raw_bytes = imgByteArr.getvalue()

    # time compression
    compress_start = perf_counter_ns()
    compressed_bytes = algo.compress(raw_bytes)
    compress_end = perf_counter_ns()

    # time decompression
    decompress_start = perf_counter_ns()
    decompressed_bytes = algo.decompress(compressed_bytes)
    decompress_end = perf_counter_ns()

    # compression ratio
    compression_ratio = len(raw_bytes) / len(compressed_bytes)

    # source entropy
    # TODO
    source_entropy = 10

    # bits per pixel
    # TODO
    bits_per_pixel = 10

    # record results
    result = Series(
        [
            algo.__name__.split(".")[1],
            compress_end - compress_start,
            decompress_end - decompress_start,
            compression_ratio,
            source_entropy,
            bits_per_pixel,
        ],
        index=cols,
    )
    return results.append(result, ignore_index=True)
