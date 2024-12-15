from pydantic import BaseModel
from typing import Optional


class DepartmentBase(BaseModel):
    name: str
    leader_id: Optional[int] = None


class DepartmentCreate(DepartmentBase):
    pass


class DepartmentUpdate(BaseModel):
    name: Optional[str] = None
    leader_id: Optional[int] = None


class Department(DepartmentBase):
    id: int

    class Config:
        from_attributes = True