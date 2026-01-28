import mutagen
import re
from pathlib import Path
from models import AudioFile

def sanitize_filename(filename: str) -> str:
    return re.sub(r'[\\/:*?"<>|]', '_', filename)

# modify this function to return list[AudioFile]
def get_audio_files() -> list[AudioFile]:
    audio_files = []
    DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "input"

    for file_path in DATA_DIR.iterdir():
        file_obj = mutagen.File(file_path)
        audio_files.append(
            AudioFile(
                path: file, 
                original_name = file_obj["TIT2"], 
                normalized_name = "None",
                duration = file_obj["TLEN"]
            )
        )
    return audio_files
    
def counter(start: int = 1) -> int:
    n = start
    while True:
        yield n
        n += 1

def get_new_file_name(track: dict) -> str:
    return f"{next(count):03d} - {track["artist"]} - {track["name"]}"

def rename_file(current_name, new_name) -> None:
    try:
        current_file = DATA_DIR / current_name
        new_file = DATA_DIR / new_file
        current_file.rename(new_file)

        print(f"\"{current_name}\" has been renamed to \"{new_name}\"")
    except Error as e:
        print(e)

if __name__ == "__main__":
    get_audio_files()