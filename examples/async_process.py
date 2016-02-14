import py_easy_async
import time


def print_with_sleep(word):
    time.sleep(1)
    print(word)


print('first')
py_easy_async.async(lambda: print_with_sleep('second'))
print('third')

# will produce:
# first
# third
# second
