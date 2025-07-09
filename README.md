# 🎞️ ASCII Video Player

A real-time terminal video player that converts **YouTube videos to ASCII art**, streams them frame-by-frame, and renders them directly in your terminal — all offline, and built from scratch.

> Think `mpv --vo=aa`, but fully custom and way more fun to break.

---

## ⚙️ Features

- 🔻 Downloads any YouTube video via `yt-dlp`
- 🧠 Extracts frames using `ffmpeg`
- 🪄 Converts each frame to ASCII using Python + Pillow (or OpenCV)
- 🚀 Plays the video frame-by-frame in your terminal while conversion happens in the background
- 💥 Fully threaded & multiprocessing optimized
- 🧼 Auto-cleans temp files (`video.mp4`, `frames/`, `asciiFrames/`) on exit

---

## 🧰 Tech Stack

- **Python**
- `yt-dlp` — YouTube video downloader
- `ffmpeg` — frame extraction
- `Pillow` — image processing (or OpenCV)
- `multiprocessing` & `threading` — real-time parallel conversion + playback
- `shutil`, `atexit`, `signal` — safe cleanup

---

### 📦 Requirements

- Python 3.10+
- [ffmpeg](https://ffmpeg.org/)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [Pillow](https://pypi.org/project/pillow/)
