import os
import google.auth.transport.requests
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Set the scopes required for uploading to YouTube
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

# Authenticate and get credentials
flow = InstalledAppFlow.from_client_secrets_file(
    '''D:\\python learning\\YouTube automation\\scripting_file_auto\\client_secret_517530866582-2202pflk80vd5ji90mlb8jbtgv6ir8em.apps.googleusercontent.com.json''', SCOPES
)

credentials = flow.run_local_server(port=0)

# Build the YouTube API client
youtube = build("youtube", "v3", credentials=credentials)

# Video details
request_body = {
    "snippet": {
        "title": "Top Finance Tip in 60 Seconds!",
        "description": "Finance knowledge on emergency fund #Finance #MoneyTips #Shorts",
        "tags": ["Finance", "Money", "Podcast", "Shorts","US"],
        "categoryId": "22"  # '22' = People & Blogs; '26' = How-to; '24' = Entertainment
    },
    "status": {
        "privacyStatus": "public",
        "selfDeclaredMadeForKids": False
    }
}

# Upload your video file
media = MediaFileUpload('''D:\\python learning\\YouTube automation\\DAVE RAMSEY IS CLUELESS WHEN IT COMES TO THE $1,000 EMERGENCY FUND STRATEGY..mp4..mp4''', chunksize=-1, resumable=True, mimetype="video/*")

# Upload the video
upload_request = youtube.videos().insert(
    part="snippet,status",
    body=request_body,
    media_body=media
)

response = upload_request.execute()
print("✅ Video uploaded! Video ID:", response.get("id"))
