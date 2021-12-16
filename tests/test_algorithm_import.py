from algorithms import ALGORITHMS


def test_contains_compression_attributes():
    for algo in ALGORITHMS:
        assert algo.compress
        assert algo.decompress
        assert algo.__name__


def test_algorithm_names_are_unique():
    algorithm_names = [a.__name__ for a in ALGORITHMS]
    assert len(set(algorithm_names)) == len(algorithm_names)
