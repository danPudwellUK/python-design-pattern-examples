def log(func):
    def wrapper(*args, **kwargs):
        print("arguments:", args)
        func_response = func(*args, **kwargs)
        print("response:", func_response)
        return func_response
    return wrapper
