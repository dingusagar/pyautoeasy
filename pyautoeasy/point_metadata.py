from jsonobject.api import JsonObject
from jsonobject.properties import IntegerProperty, StringProperty


class CursorPointMetaData(JsonObject):
    variable_name = StringProperty()
    x_cord = IntegerProperty()
    y_cord = IntegerProperty()


class ImageMetaData(JsonObject):
    variable_name = StringProperty()
    image_path = StringProperty()
