from circle import Circle
from rectangle import Rectangle
from shape import IShape
from square import Square


class ShapeFactory:
    def get_shape(self, shape_type: str) -> IShape | None:
        # just
        options = {"CIRCLE": Circle(), "RECTANGLE": Rectangle(), "SQUARE": Square()}
        return options[shape_type.upper()]
