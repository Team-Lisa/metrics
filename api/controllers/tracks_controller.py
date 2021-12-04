from api.repositories.track_repository import TrackRepository
from api.models.track import Track
from fastapi import HTTPException



class TracksController:

    @staticmethod
    def create(track):
        track_to_save = Track(name=track.name, event_data=track.event_data)
        TrackRepository.add_track(track_to_save)
        return {"message": "track saved"}


    @staticmethod
    def find_by_name(name):
        raise HTTPException(status_code=404, detail="User not found")