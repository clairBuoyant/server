import typing as t

from sqlalchemy.orm import declarative_base  # type: ignore

class_registry: t.Dict = {}


Base = declarative_base()

# TODO: implement with metadata attribute
# @as_declarative(class_registry=class_registry)
# # class _Base:
# #     id: t.Any
# #     __name__: str
# #     # Generate __tablename__ automatically
# #     @declared_attr
# #     def __tablename__(cls) -> str:
# #         return cls.__name__.lower()
