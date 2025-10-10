import yt_dlp

url = "https://www.youtube.com/watch?v=Y3dkavmod0M&"

ydl_opts = {
    'format': 'bestaudio', # You can choose 'bestaudio', 'bestvideo', etc.
    'verbose': False,
    'quiet': True,
    'skip_download': True
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        print (f"Video Title: {info_dict.get('title')}\nChannel: {info_dict.get('channel')}\nDuration: {info_dict.get('duration_string')}")
except yt_dlp.utils.DownloadError as e:
    print(f"An error occurred: {e}")
