from pathlib import Path
from pandas import Series, DataFrame
from time import perf_counter_ns
from helper.constants import cols
from PIL import Image
import io


def find_benchmark_images():
    """Return the images in the images sub-folders or rgb + gray"""
    images = Path("images/rgb8bit").glob("*.ppm")
    images_2 = Path("images/gray8bit").glob("*.pgm")
    joined_paths = list(images) + list(images_2)
    return [*map(str, joined_paths)]


def benchmark(algo, results: DataFrame):
    # TODO: Benchmark more than one image
    image = Image.open("images/rgb8bit/artificial.ppm")
    img_byte_array = io.BytesIO()
    image.save(img_byte_array, format=image.format)
    raw_bytes = img_byte_array.getvalue()

    # time compression
    compress_start = perf_counter_ns()
    compressed_bytes = algo.compress(raw_bytes)
    if algo.__name__ == "algorithms.huffman":
        compressed_bytes, encoding_tree = compressed_bytes[0], compressed_bytes[1]
    compress_end = perf_counter_ns()

    # time decompression
    decompress_start = perf_counter_ns()
    if algo.__name__ == "algorithms.huffman":
        decompressed_bytes = algo.decompress(compressed_bytes, encoding_tree)
    else:
        decompressed_bytes = algo.decompress(compressed_bytes)

    decompress_end = perf_counter_ns()

    # compression ratio
    # TODO: Fix compression ratio to use bytes instead of len of the byte data
    # structure
    compressed_size = len(compressed_bytes)
    compression_ratio = len(raw_bytes) / (compressed_size if compressed_size else 1)

    # record results
    result = Series(
        [
            algo.__name__.split(".")[1],
            compress_end - compress_start,
            decompress_end - decompress_start,
            compression_ratio,
        ],
        index=cols,
    )
    return results.append(result, ignore_index=True)
