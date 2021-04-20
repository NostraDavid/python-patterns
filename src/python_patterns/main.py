from shape_factory import ShapeFactory

def factory():
    shape_factory = ShapeFactory()

    # get an object of Circle and call its draw method.
    shape1 = shape_factory.get_shape("CIRCLE")

    # call draw method of Circle
    shape1.draw()

    # get an object of Rectangle and call its draw method.
    shape2 = shape_factory.get_shape("RECTANGLE")

    # call draw method of Rectangle
    shape2.draw()

    # get an object of Square and call its draw method.
    shape3 = shape_factory.get_shape("SQUARE")

    # call draw method of square
    shape3.draw()

def main():
    """put each separate function here"""
    factory()


if __name__ == '__main__':
    main()