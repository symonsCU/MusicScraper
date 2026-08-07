from scraper.beatport import BeatportScraper


def main():
    scraper = BeatportScraper()

    tracks = scraper.get_tracks()

    print(f"Found {len(tracks)} tracks")

    for track in tracks[:10]:
        print(track)


if __name__ == "__main__":
    main()