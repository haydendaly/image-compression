from pandas import DataFrame
from algorithms import bz2, rle, zlib, lzw, huffman
from helper.benchmark import benchmark
from helper.constants import cols

algos = [
    rle,
    zlib,
    lzw,
    huffman,
    bz2,
]


def main(out_file="results/benchmarks.csv"):
    results = DataFrame(columns=cols)
    for algo in algos:
        results = benchmark(algo, results)
    results.to_csv(out_file)


if __name__ == "__main__":
    main()
