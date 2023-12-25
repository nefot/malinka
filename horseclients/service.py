def benchmark(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print(f'[{func.__name__}] Время выполнения: {end - start} секунд.')
        return return_value
    return wrapper


color = '\033[31m'


def debug(text):
    print('\033[0m')


if __name__ == '__main__':
    debug('привет $red(Артем)  $green(сто ты умеешь)')
