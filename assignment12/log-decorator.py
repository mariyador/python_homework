import logging

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.log(
            logging.INFO,
            f"function: {func.__name__}, "
            f"positional parameters: {args or 'none'}, "
            f"keyword parameters: {kwargs or 'none'}, "
            f"return: {result}"
        )
        return result
    return wrapper

@logger_decorator
def say_hello():
    print("Hello, World!")

@logger_decorator
def check_all(*args):
    return True

@logger_decorator
def keyword_only(**kwargs):
    return logger_decorator

if __name__ == "__main__":
    say_hello()
    check_all(1, 2, 3)
    keyword_only(a=1, b=2, c=3)