import shutil
import os

def safe_rmdir(folder):
    if os.path.exists(folder):
        try:
            shutil.rmtree(folder)
            print(f"Removed folder: {folder}")
        except Exception as e:
            print(f"Failed to delete {folder}: {e}")

def safe_remove(file):
    if os.path.isfile(file):
        try:
            os.remove(file)
            print(f"Removed file: {file}")
        except Exception as e:
            print(f"Failed to delete {file}: {e}")

def cleanup():
    safe_remove("downloads/video.mp4")
    safe_rmdir("vidFrames")
    safe_rmdir("asciiFrames")
