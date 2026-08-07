import csv
import os


def save_tracks(tracks, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Artist",
            "Track",
            "YouTube URL"
        ])

        for track in tracks:
            writer.writerow([
                track["artist"],
                track["title"],
                track.get("youtube", "")
            ])