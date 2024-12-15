try:
    from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
    from sqlalchemy.orm import relationship
    from app.database.base import Base
except Exception as error:
    raise ("Erro de biblioteca: %s" % error)


class Job(Base):
    __tablename__ = "job"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )
    name = Column(
        String,
        nullable=False,
        unique=True
    )
    code = Column(
        String(4),
        unique=True
    )
    department_id = Column(
        Integer,
        ForeignKey("department.id"),
        nullable=False
    )

    department = relationship(
        "Department",
        foreign_keys=[department_id]
    )