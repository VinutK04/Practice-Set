import time
from functools import wraps

def time_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__}() took {end_time - start_time} seconds to execute")
        return result
    return wrapper

@time_decorator
def add(a, b):
    time.sleep(1)
    return a + b

result = add(3, 4)
print(result)
