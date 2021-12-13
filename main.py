from pandas import DataFrame
from algorithms import burrows_wheeler, rle, zlib, lzw, huffman
from helper.benchmark import benchmark
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
    for algo in algos:
        print(f"Running benchmarks for {algo=}...")
        results = benchmark(algo, results)
    results.to_csv(out_file)


if __name__ == "__main__":
    main()
