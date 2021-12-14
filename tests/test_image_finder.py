from helper import benchmark


def test_finding_benchmark_images():
    images = benchmark.find_benchmark_images()
    assert len(images) == 18
    for image in images:
        assert type(image) == str
