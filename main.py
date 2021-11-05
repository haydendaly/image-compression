from pandas import DataFrame
from algorithms import zlib
from helper.benchmark import benchmark
from helper.constants import cols

algos = [
    zlib
]


def main(out_file="results/benchmarks.csv"):
    results = DataFrame(columns=cols)
    for algo in algos:
        results = benchmark(algo, results)
    results.to_csv(out_file)


if __name__ == "__main__":
    main()
