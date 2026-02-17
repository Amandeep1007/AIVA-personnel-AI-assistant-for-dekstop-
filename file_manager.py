import os
from pydub import AudioSegment
from pydub.playback import play

MUSIC_FOLDER = os.path.expanduser("~/Music")

def play_music():
    songs = os.listdir(MUSIC_FOLDER)
    if not songs:
        return "No music found in Music folder."

    song_path = os.path.join(MUSIC_FOLDER, songs[0])
    audio = AudioSegment.from_file(song_path)
    play(audio)
    return f"Playing {songs[0]}"

def play_specific_song(song_name):
    for file in os.listdir(MUSIC_FOLDER):
        if song_name.lower() in file.lower():
            song_path = os.path.join(MUSIC_FOLDER, file)
            audio = AudioSegment.from_file(song_path)
            play(audio)
            return f"Playing {file}"

    return "Song not found."

def open_folder(folder_name):
    base = os.path.expanduser("~")

    paths = {
        "downloads": os.path.join(base, "Downloads"),
        "documents": os.path.join(base, "Documents"),
        "desktop": os.path.join(base, "Desktop"),
        "music": os.path.join(base, "Music")
    }

    if folder_name in paths:
        os.startfile(paths[folder_name])
        return f"Opening {folder_name} folder."

    return "Folder not found."

def find_file(filename):
    base = os.path.expanduser("~")

    for root, dirs, files in os.walk(base):
        for file in files:
            if filename.lower() in file.lower():
                os.startfile(os.path.join(root, file))
                return f"Opening {file}"

    return "File not found."

