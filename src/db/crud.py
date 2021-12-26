from sqlalchemy.orm import Session

from . import models, schemas


def get_buoy(db: Session, station_id: str):
    return db.query(models.Buoy).filter(models.Buoy.station_id == station_id).first()


def create_buoy(db: Session, buoy: schemas.BuoyCreate):
    buoy_to_db = models.Buoy(**buoy)  # TODO: manually assign to kwargs for readability
    db.add(buoy_to_db)
    db.commit()
    db.refresh(buoy_to_db)
    return buoy_to_db
