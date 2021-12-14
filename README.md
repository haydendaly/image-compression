# A Comparison of Lossless Compression Algorithms for Images

This repository contains the benchmarking code for lossless image compression algorithms. This is the final project for CS 5112 at Cornell Tech.

## Usage

Create virtualenv:

```sh
$ virtualenv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

Run benchmarks (will be in `results/benchmarks.csv`):

```sh
$ python3 main.py
```

Generate charts (will be in `results/graphs/*.png`):

```sh
$ python3 analysis.py
```

## Benchmark Format

| Column    | Description   | Unit      |
| --------- | ------------- | --------- |
| `compress_time` | Time for compression | Nanoseconds |
| `decompress_time` | Time for decompression | Nanoseconds |
| `compression_ratio` | Byte size of compressed over normal | raw_bytes / compressed_bytes |
