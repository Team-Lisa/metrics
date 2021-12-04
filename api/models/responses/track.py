from pydantic.main import BaseModel


class Track(BaseModel):
    tracks: dict
