from multipledispatch import dispatch
from riotwatcher import LolWatcher, RiotWatcher

class DataCollector:
    def __init__(self, api_key) -> None:
        self.api_key = api_key
        
        self.riot_watcher = RiotWatcher(self.api_key)
        self.lol_watcher = LolWatcher(self.api_key)
    
    def collect_matches_by_division(self, region_major, region_minor, rank, division):
        players = self.lol_watcher.league.entries(region_minor, 'RANKED_SOLO_5x5', rank, division)
        matches = []
            
    
    def collect_matches_by_player(self, region_major, region_minor, summoner_name, summoner_tag):
        riot_account = self.riot_watcher.account.by_riot_id(region_major, summoner_name, summoner_tag)
        lol_account = self.lol_watcher.summoner.by_puuid(region_minor, riot_account['puuid'])
        
        match_ids = self.lol_watcher.match.matchlist_by_puuid(region_major, lol_account['puuid'])
        match_stats = []
        for match_id in match_ids:
            match_stats.append(self.lol_watcher.match.by_id(region_major, match_id)['info'])

        return match_stats