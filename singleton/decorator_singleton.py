def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

@singleton
class Stuff():
    pass


first_singleton = Stuff()  # created the object
second_singleton = Stuff()  # retrieved same object
print(first_singleton is second_singleton)  # verify they are the same
