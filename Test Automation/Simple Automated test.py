def multiplication(a, b):
    return a * b


try:
    assert multiplication(3,5) == 15
    print("Test is passed")

    assert multiplication(0, 5) == 0
    print("Test with zero is passed")
except AssertionError:
    print("Test is failed")
