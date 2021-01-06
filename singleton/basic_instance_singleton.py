class SingletonThing(object):
    _instance = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(self):
        if self._instance is None:
            print('Creating new instance')
            self._instance = self.__new__(self)

        return self._instance

first_singelton = SingletonThing.instance()  # created the object
second_singleton = SingletonThing.instance()  # retrieved same object
print(first_singelton is second_singleton)  # verify they are the same
