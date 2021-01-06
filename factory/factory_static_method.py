class Polygon(object):
    pass

class Triangle(Polygon):
    pass

class Sqaure(Polygon):
    pass

class Pentagon(Polygon):
    pass


class PolygonFactory(object):

    @staticmethod
    def get_shape(numberOfSides):
        if numberOfSides == 3:
            return Triangle()
        elif numberOfSides == 4:
            return Sqaure()
        elif numberOfSides == 5:
            return Pentagon()
        else:
            raise RuntimeError('no option for numberOfSides')


triangle = PolygonFactory.get_shape(3)
print(type(triangle))
square = PolygonFactory.get_shape(4)
print(type(square))
pentagon = PolygonFactory.get_shape(5)
print(type(pentagon))
