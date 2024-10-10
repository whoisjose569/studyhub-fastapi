from pydantic import BaseModel, Field, constr, validator, EmailStr
from typing import Optional
from src.errors.types import HttpBadRequestError

class StudentSearchSchema(BaseModel):
    search: Optional[constr(max_length=100)] = Field(default="") # type: ignore

    @validator('search')
    def check_search(cls, v):
        if v and not v.isalnum() and not all(c in ' @._-' for c in v):
            raise HttpBadRequestError('search must contain only alphanumeric characters, spaces, and @._-')
        return v

class StudentInputSchema(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr  

    @validator('name')
    def name_must_contain_only_letters_and_spaces(cls, v):
        if not all(c.isalpha() or c.isspace() for c in v):
            raise HttpBadRequestError('Name must contain only letters and spaces.')
        return v

    class Config:
        anystr_strip_whitespace = True