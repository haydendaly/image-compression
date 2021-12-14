from pandas import DataFrame
from algorithms import burrows_wheeler, rle, zlib, lzw, huffman
from helper.benchmark import benchmark, find_benchmark_images
from helper.constants import cols

# TODO: Add more algorithms through parametrization
algos = [
    rle,
    zlib,
    lzw,
    huffman,
    burrows_wheeler,
]


def main(out_file="results/benchmarks.csv"):
    results = DataFrame(columns=cols)
    images = find_benchmark_images()
    for algo in algos:
        for image in images:
            print(f"Running benchmarks for {(algo.__name__.split('.')[1], image)}...")
            results = benchmark(algo, image, results)
    results.to_csv(out_file)


if __name__ == "__main__":
    main()
