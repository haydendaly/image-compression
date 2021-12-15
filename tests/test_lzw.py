from algorithms import lzw

data = b"hello world"


def test_compress_decompress():
    c_data = lzw.compress(data)
    d_data = lzw.decompress(c_data)
    assert data == d_data


def test_parametrization():
    algo = lzw.make_benchmarkable_algorithm(bit_max_width=12)
    assert algo.compress
    assert algo.decompress
    assert data == algo.decompress(algo.compress(data))
