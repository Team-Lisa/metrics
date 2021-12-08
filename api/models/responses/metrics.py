from typing import List

from pydantic.main import BaseModel


class Time(BaseModel):
    time: float


class Access(BaseModel):
    date: str
    access_amount: int


class Units(BaseModel):
    date: str
    units_completed_amount: int


class MetricsContent(BaseModel):
    new_access: List[Access]
    unit_completed: List[Units]
    exam_resolution_time: Time
    user_frequency: Time


class Metrics(BaseModel):
    metrics: MetricsContent
