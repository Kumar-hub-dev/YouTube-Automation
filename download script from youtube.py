import yt_dlp
import os

# Set the FFmpeg location explicitly in yt-dlp options
ffmpeg_path = r"D:\\Downloads\\ffmpeg-7.1.1-essentials_build\\ffmpeg-7.1.1-essentials_build\\bin"

def download_youtube_video(url, output_path='D:\\python learning\\YouTube automation'):
    ydl_opts = {
        'ffmpeg_location': ffmpeg_path,  # Explicitly set ffmpeg location
        'format': 'bestvideo+bestaudio/best',  # Best video and best audio format
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Output template
        'merge_output_format': '.mp4',  # Merge audio and video into MP4
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': '.mp4',  # Convert to MP4 format
        }],
    }
    
    # Use yt-dlp to download the video and merge the formats
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Example usage
download_youtube_video("https://www.youtube.com/shorts/b_X9JYZKsuI")