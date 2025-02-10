def log_message(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open("/tmp/decorator_logs.txt", "a") as file:
            file.write(result+"\n")
        return result
    return wrapper
