from geoalchemy2.elements import WKBElement
from geoalchemy2.shape import to_shape


def ewkb_to_wkt(geom: WKBElement):
    """
    Converts a geometry formated as WKBE to WKT
    in order to parse it into pydantic Model

    Args:
        geom (WKBElement): A geometry from GeoAlchemy query
    """
    return to_shape(geom).wkt
