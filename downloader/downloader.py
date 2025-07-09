import subprocess

def download_video(url):
    output_path = 'downloads/video.mp4'
    cmd = [
        'yt-dlp',
        '-f', 'mp4',
        '-o', output_path,
        url
    ]
    subprocess.run(cmd, check=True)