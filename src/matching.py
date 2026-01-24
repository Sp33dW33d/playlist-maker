"""
notes

preprocessing is required, damn
need to strip, probably remove the artist name(?)
ehh but should i do string based removal? what if i use a different source for the music files. 
or just that the music file names have a different formatting

i guess i could do searches based on the mp3 file's metadata tags
but some sources might not provide tags sooo... idk
maybe i should add 2 different modes
filename based search, and tag based search
and maybe for filename based search, i should add different modes to allow for different mp3 file naming formats. eh.
would be a lot of hard coding maybe
"""
# func for getting the song_files
# func for getting the song_name

# func for getting best name match
# func for getting artist match
# func for getting duration match
# func for getting best overall match

# func for renaming a specific file
# func for running the loop

import rapidfuzz
import os


def find_best_name_match(song_name, song_files, score_cutoff=70):
    return rapidfuzz.process.extract(song_name, song_files, score_cutoff=score_cutoff)[0]

location = r"D:\Coding_Stuff\Codes\Python\playlist-maker\data\input"
song_files = get_songfiles(location)

track_name = "HEARTBREAKER CLUB"
