import automated_clean_code


def test_sanity():
    assert 1 + 1 == 2


def test_add():
    assert automated_clean_code.add_numbers(1, 2) == 3


# def test_subtract(x: int, y: int):
#     return x - y  # pragma: no cover
