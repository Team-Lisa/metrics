from api.repositories.track_repository import TrackRepository
from api.models.track import Track


class TracksController:

    @staticmethod
    def create(track):
        track_to_save = Track(name=track.name, event_data=track.event_data, date=track.date)
        TrackRepository.add_track(track_to_save)
        return {"message": "track saved"}