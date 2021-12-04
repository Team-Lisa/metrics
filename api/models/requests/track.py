from pydantic.main import BaseModel


class Track(BaseModel):
    name: str
    event_data: dict
    date: str
