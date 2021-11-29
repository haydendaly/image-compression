from pandas import DataFrame
<<<<<<< HEAD
from algorithms import rle, zlib
from algorithms.arithmetic import arithmetic
=======
from algorithms import rle, zlib, lzw
>>>>>>> 62994d974b59166ef87c2d8c17cbef13995c476f
from helper.benchmark import benchmark
from helper.constants import cols

algos = [
<<<<<<< HEAD
    # rle, 
    zlib, arithmetic
=======
    # rle,
    zlib,
    lzw,
>>>>>>> 62994d974b59166ef87c2d8c17cbef13995c476f
]


def main(out_file="results/benchmarks.csv"):
    results = DataFrame(columns=cols)
    for algo in algos:
        results = benchmark(algo, results)
    results.to_csv(out_file)


if __name__ == "__main__":
    main()
