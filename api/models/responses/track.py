from pydantic.main import BaseModel


class Track(BaseModel):
    message: str
