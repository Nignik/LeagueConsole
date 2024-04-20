from pymongo import MongoClient

class DataPoster:
    def __init__(self) -> None:
        self.db = MongoClient("localhost", 27017).league_of_legends
    
    def post_player_matches(self, matches):
        for match in matches:
            self.db.matches.insert_one({"match": match})