import functools

class TypeErrorWithMessage(TypeError):
    pass

def check_argument_type(required_type):
    """
    A decorator factory that returns a decorator that checks the argument type
    of a function.

    :param required_type: The required argument type.
    :type required_type: type
    :return: A decorator that checks the argument type of a function.
    :rtype: callable
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(arg):
            """
            A wrapper function that checks the argument type before calling the decorated
            function.

            :param arg: The argument to check the type of.
            :raises TypeErrorWithMessage: If the argument is not of the required type.
            """
            if not isinstance(arg, required_type):
                raise TypeErrorWithMessage(f"Argument must be of type {required_type.__name__}")
            return func(arg)
        return wrapper
    return decorator


@check_argument_type(int)
def double(x):
    return x * 2


result = double(3)
print(result)  # prints 6

result = double('not an int')  # raises TypeErrorWithMessage


# more exercise
def surprise(func):
    def wrapper(*args, **kwargs):
        print("surprise!")

    return wrapper


@surprise
def my_function():
    print("Hello, world!")


my_function()  # prints "surprise!"

