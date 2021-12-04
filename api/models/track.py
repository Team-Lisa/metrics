import mongoengine
from mongoengine import Document


class Track(Document):
    name = mongoengine.StringField()
    event_data = mongoengine.DictField()
    date = mongoengine.StringField()

    def to_json(self):
        result = self.to_mongo().to_dict()
        if "_id" in result:
            del result["_id"]
        return result