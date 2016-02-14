from py_easy_async import pool


def message_handler(message):
    print('got message:', message)


identifier = pool.run_thread(message_handler)

for i in range(10):
    pool.message(identifier, "test message #%s" % i)

pool.stop_thread(identifier)
