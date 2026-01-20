from os import rename
import re

# change this to f"{count} - {}"
def get_new_file_name(location, track) -> str:
    return f"{counter}/{track[0]} - {track[1]}"

def sanitize_filename(filename: str) -> str:
    return re.sub(r'[\\/:*?"<>|]', '_', filename)

def rename_file(current_name, new_name):
    try:
        rename(current_name, new_name)
        print("")
    except Error as e:
        print(e)
# ---


# theres a function get_tracklist() which returns list[str], with the songs in order of the playlist on spotify
# i have the song mp3 files in a folder
# now i just need to iterate through the tracklist, find the best match possible, and then rename the mp3 file with that number
# but sometimes the song_name might not be the same, because of translations, different names on different platforms maybe etc
# so how do i find the best possible match, not the exact match
# and how do i find out if none of the files are a good enough match, so that i can skip that file and let the user know

# i could normalize the track_name and the file_name first, and then run a fuzzy match. if the confidence is high it will rename the file,
# if it doesnt cross a certain threshold it will print a warning and skip to the next file. also maybe record the skipped track in a log file.
# but im a bit worried about the normalization part. what about songs of the same name, but from different artists? what about different
# versions of the same song? for example, "Blinding Lights" vs "Blinding Lights (Remastered)". if i normalize them, there wont be any
# difference between them. normally it shouldnt pose much of an issue, but what if there are both versions in the same playlist?