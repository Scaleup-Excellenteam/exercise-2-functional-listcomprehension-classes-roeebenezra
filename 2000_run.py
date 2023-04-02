import time


def timer(f, *args, **kwargs):
    """
    Measure the execution time of a function f with given parameters.
    :param f: The function to measure its execution time.
    :param args: The arguments for the function f.
    :param kwargs: The keyword arguments for the function f.
    :return: None
    """
    start_time = time.perf_counter()
    f(*args, **kwargs)
    end_time = time.perf_counter()
    print("Execution time: {:.6f} seconds".format(end_time - start_time))


timer(print, "Hello")
timer(zip, [1, 2, 3], [4, 5, 6])
timer("Hi {name}".format, name="Bug")
