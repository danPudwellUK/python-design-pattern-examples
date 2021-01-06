from log_decorator import log

@log
def find_rectangle_area(width, length):
    area = width * length
    return area


a = find_rectangle_area(10,20)
print(a)


# decorators wrap a function, modifying its behavior.
