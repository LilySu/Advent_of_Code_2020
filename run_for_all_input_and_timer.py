import time
import os

class Manager:

    def get_file(self, strip = True):
        current_file = str(os.path.abspath(os.getcwd())[-2::])
        with open("input-" + current_file) as f:
            content = f.readlines()
        if strip:
            return [x.strip() for x in content]
        return content

def timer(func):
    def wrapper(*args, **kwargs):
        all_runtimes = 0
        iterations = 1
        for i in range(iterations):
            start_time = time.time()
            result = func(*args, **kwargs)
            all_runtimes += time.time() - start_time
        print(f"\nTime required on average for 1 iterations: {(all_runtimes/iterations)*1000:.4f} ms\n")
        return result
    return wrapper