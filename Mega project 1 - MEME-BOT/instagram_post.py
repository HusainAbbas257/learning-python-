#   to interact with the instagram we need instagrapi
from instagrapi import Client
import os
import random
import time


# firrst we got to login
userid='itchy__balls'
password=''
with open('C:/Users/DELL/Desktop/api-keys/instagram_paasword.txt') as f:
    password=f.read().strip()

account=Client()
account.login(userid,password)

#  now we gotto post video
caption='''No problem! Here's the information about the Mercedes CLR GTR:

The Mercedes CLR GTR is a remarkable racing car celebrated for its outstanding performance and sleek design. Powered by a potent 6.0-liter V12 engine, it delivers over 600 horsepower. 🔧

Acceleration from 0 to 100 km/h takes approximately 3.7 seconds, with a remarkable top speed surpassing 320 km/h. 🥇

Incorporating advanced aerodynamic features and cutting-edge stability technologies, the CLR GTR ensures exceptional stability and control, particularly during high-speed maneuvers. 💨

Originally priced around $1.5 million, the Mercedes CLR GTR is considered one of the most exclusive and prestigious racing cars ever produced. 💰

Its limited production run of just five units adds to its rarity, making it highly sought after by racing enthusiasts and collectors worldwide.
#meme #reels #funny '''

#  now selecting A random video
video_file='Mega project 1 - MEME-BOT/videos'
video=''
def fetch_logs():
    mp4 = []
    with open('Mega project 1 - MEME-BOT/logs/uploads.txt') as f:
        uploaded = set(line.strip() for line in f.readlines())  # split by lines, remove \n, store in set
    for v in os.listdir(video_file):
        if v.endswith('.mp4') and v not in uploaded:
            mp4.append(v)
            print(v)
    return mp4

mp4_list = fetch_logs()
if len(mp4_list) > 0:
    video = random.choice(mp4_list)
else:
    print('no video found creating one:')
    import create_video
    mp4_list = fetch_logs()
    video = random.choice(mp4_list)

video_path=os.path.join(video_file,video)
# uploding that video


media=account.clip_upload(video_path, caption=caption)
print('video saved')
# now i want it to comment automatically

account.media_comment(media.pk, "🔥🔥🔥")

# now saving the logs:
with open('Mega project 1 - MEME-BOT/logs/uploads.txt','a') as f:
    f.write(video+'\n')
print('logs saved')

# deleting junks:

for _ in range(10):  # try 10 times
    try:
        print(video_path)
        os.remove(video_path)
        os.remove(video_path+'.jpg')
        print("Video deleted.")
        break
    except PermissionError:
        print("Waiting for file to unlock...")
        time.sleep(10)

