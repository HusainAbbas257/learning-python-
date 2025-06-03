# we are gonna use moviepy i learned from it docs how to basically use it
import os
import random
from moviepy import *

# Define paths
MEME_DIR = "C:/Users/DELL/Desktop/learning-python-/Mega project 1 - MEME-BOT/memes"
MUSIC_DIR = "C:/Users/DELL/Desktop/learning-python-/Mega project 1 - MEME-BOT/musics"
OUTPUT_DIR = "C:/Users/DELL/Desktop/learning-python-/Mega project 1 - MEME-BOT/videos"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Select random meme and music
try:
    meme_file = random.choice(os.listdir(MEME_DIR))
    music_file = random.choice(os.listdir(MUSIC_DIR))
except Exception:
    import reddit_scrapper
    meme_file = random.choice(os.listdir(MEME_DIR))
    music_file = random.choice(os.listdir(MUSIC_DIR))
meme_path = os.path.join(MEME_DIR, meme_file)
music_path = os.path.join(MUSIC_DIR, music_file)

# Duration of the video (in seconds)
VIDEO_DURATION = 10

# Load image and with duration
clip = ImageClip(meme_path).with_duration(VIDEO_DURATION)
clip = clip.resized(height=1080)  # Resize to fit Insta Reels 
clip = clip.with_position("center")

# Load audio and cut to duration
audio = AudioFileClip(music_path).subclipped(0, VIDEO_DURATION)

# with audio to clip
final_video = clip.with_audio(audio)

# Export the final video
output_path = os.path.join(OUTPUT_DIR, f"{os.path.splitext(meme_file)[0]}.mp4")
final_video.write_videofile(output_path, fps=24)
print(f"Video created: {output_path}")

# save the logs:
with open('C:/Users/DELL/Desktop/learning-python-/Mega project 1 - MEME-BOT/logs/video_log.txt','a') as f:
    f.write(f'meme={meme_path},music={music_path},video={output_path}\n')
print('logs saved')
# now delete the meme file to prevent further video with same meme:

os.remove(meme_path)
print('deleted meme')
