from geoalchemy2.elements import WKBElement  # type: ignore
from geoalchemy2.shape import to_shape  # type: ignore


def ewkb_to_wkt(geom: WKBElement):
    """
    Converts a geometry formated as WKBE to WKT
    in order to parse it into pydantic Model

    Args:
        geom (WKBElement): A geometry from GeoAlchemy query
    """
    return to_shape(geom).wkt


def ewkb_to_coords(geom: WKBElement):
    """
    Converts a Point formated as WKBE to an array
    of coordinates in order to parse it into pydantic Model

    Args:
        geom (WKBElement): A geometry from GeoAlchemy query
    """
    return to_shape(geom).coords[0]
