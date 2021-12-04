from api.models.track import Track


class TrackRepository:

    @staticmethod
    def add_track(user):
        return user.save()

    @staticmethod
    def get_track_by_name(value):
        user = Track.objects(name=value)
        return user

    @staticmethod
    def delete_all_track():
        Track.objects().delete()

    @staticmethod
    def get_all_tracks():
        return Track.objects()