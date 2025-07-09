from downloader.downloader import download_video
from frames.extracter import extract_frames_live
from asciiConverter.asciiWatcher import  watch_and_convert
from player.player import play_ascii_frames
from threading import Thread
import atexit
import signal
from utils.cleanup import cleanup

def main():
    url = input("Enter YouTube URL: ").strip()

    print("Downloading video...")
    download_video(url)

    print("Starting frame extraction...")
    ffmpeg_proc = extract_frames_live()

    print("Launching ASCII converter thread...")
    converter_thread = Thread(target=watch_and_convert)
    converter_thread.start()

    print("Launching ASCII playback thread...")
    player_thread = Thread(target=play_ascii_frames)
    player_thread.start()

    ffmpeg_proc.wait()
    converter_thread.join()
    player_thread.join()

    print("Done.")
    cleanup()

if __name__ == "__main__":
    def handle_exit(*args):
        cleanup()
        exit(0)

    atexit.register(cleanup)
    signal.signal(signal.SIGINT, handle_exit)

    main()
