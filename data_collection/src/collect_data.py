import os
import sys

from dotenv import load_dotenv
from DataCollector import DataCollector
from DataPoster import DataPoster

def main():
    load_dotenv()
    api_key = os.getenv("API_KEY")
    data_collector = DataCollector(api_key)
    data_poster = DataPoster()
    
    matches = data_collector.collect_matches_by_player(sys.argv[1])
    data_poster.post_player_matches(matches)


if __name__ == '__main__':
    main()