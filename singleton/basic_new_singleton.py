class SingletonThing(object):
    _instance = None

    def __new__(self):
        if self._instance is None:
            print('Creating the object')
            self._instance = super().__new__(self)

        return self._instance


first_singleton = SingletonThing()  # created the object
second_singleton = SingletonThing()  # retrieved same object
print(first_singleton is second_singleton)  # verify they are the same
