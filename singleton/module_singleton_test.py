from module_singleton_class import stuff_instance

first_singleton = stuff_instance  # created the object
second_singleton = stuff_instance  # retrieved same object
print(first_singleton is second_singleton)  # verify they are the same
