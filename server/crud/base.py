from datetime import datetime
from typing import Any, Generic, Optional, Type, TypeVar

from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession  # type: ignore
from sqlalchemy.future import select  # type: ignore

from server.db.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """Base CRUD class with default CRUD methods.

        **Parameters**
        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    async def create_many(
        self, db_session: AsyncSession, models: list[CreateSchemaType]
    ):
        # TODO: dynamically instantiate self.model before committing
        db_session.add_all(models)
        await db_session.commit()

    async def find_one(self, db_session: AsyncSession, id: Any) -> Optional[ModelType]:
        result = await db_session.execute(select(self.model).where(self.model.id == id))
        return result.scalars().first()

    async def find_many(self, db_session: AsyncSession) -> Optional[ModelType]:
        results = await db_session.execute(select(self.model))
        return results.scalars().all()

    # TODO: incorporate with find_many
    async def find_many_date_range(
        self,
        db_session: AsyncSession,
        station_id: str,
        begin_date: datetime,
        end_date: datetime,
    ) -> Optional[ModelType]:
        result = await db_session.execute(
            select(self.model).where(
                self.model.station_id == station_id
                and self.model.date_recorded >= begin_date
                and self.model.date_recorded <= end_date
            )
        )
        return result

    # TODO: remove after blending it with `get_many`.
    # def get_multi(
    #     self, db: Session, *, skip: int = 0, limit: int = 100
    # ) -> List[ModelType]:
    #     return db_session.query(self.model).offset(skip).limit(limit).all() # noqa: E501, W505

    # TODO: replace with async implementation
    # def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType: # noqa: E501, W505
    #     obj_in_data = jsonable_encoder(obj_in)
    #     db_obj = self.model(**obj_in_data)
    #     db_session.add(db_obj)
    #     db_session.commit()
    #     db_session.refresh(db_obj)
    #     return db_obj

    # TODO: replace with async implementation
    # def update(
    #     self,
    #     db: Session,
    #     *,
    #     db_obj: ModelType,
    #     obj_in: Union[UpdateSchemaType, Dict[str, Any]],
    # ) -> ModelType:
    #     obj_data = jsonable_encoder(db_obj)
    #     if isinstance(obj_in, dict):
    #         update_data = obj_in
    #     else:
    #         update_data = obj_in.dict(exclude_unset=True)
    #     for field in obj_data:
    #         if field in update_data:
    #             setattr(db_obj, field, update_data[field])
    #     db_session.add(db_obj)
    #     db_session.commit()
    #     db_session.refresh(db_obj)
    #     return db_obj

    # TODO: replace with async implementation
    # def remove(self, db: Session, *, id: int) -> ModelType:
    #     obj = db_session.query(self.model).get(id)
    #     db_session.delete(obj)
    #     db_session.commit()
    #     return obj
