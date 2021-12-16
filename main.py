from pandas import DataFrame
from itertools import repeat
from algorithms import ALGORITHMS
from helper.benchmark import benchmark, find_benchmark_images
from helper.constants import cols


def main(out_file="results/benchmarks.csv"):
    results = DataFrame(columns=cols)
    images = find_benchmark_images()

    algorithm_names = [a.__name__ for a in ALGORITHMS]

    print("=> Testing these algorithms:")
    print(*[c + x for x, c in zip(algorithm_names, repeat("\t"))], sep="\n")

    for algo in ALGORITHMS:
        for image in images:
            print(
                f"=> Running benchmarks for {(algo.__name__.split('.')[1], image)}..."
            )
            results = benchmark(algo, image, results)
    results.to_csv(out_file)


if __name__ == "__main__":
    main()
