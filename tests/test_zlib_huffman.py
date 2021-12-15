from algorithms import zlib_huffman


def test_import():
    assert zlib_huffman.compress
    assert zlib_huffman.decompress


def test_compress_decompress():
    data = b"simple data"
    compressed_data = zlib_huffman.compress(data)
    decompressed_data = zlib_huffman.decompress(compressed_data)
    assert data == decompressed_data
