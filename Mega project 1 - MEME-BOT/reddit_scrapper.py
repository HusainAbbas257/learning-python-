import praw # reddit is a pice of shiiii it cant be scrapped by beutifulsoup it it javascript baase so we use its sepciall api praw
import requests
import os
import threading



# Setup folders
os.makedirs("Mega project 1 - MEME-BOT/memes", exist_ok=True)
os.makedirs("Mega project 1 - MEME-BOT/logs", exist_ok=True)

# Reddit API credentials (get from https://www.reddit.com/prefs/apps)
reddit = praw.Reddit(
    client_id="haQBtBOjtfw2HJHaYGLtNw",
    client_secret="H8GAzxEpUSpriEnndqzE3AmTsh-b1w",
    user_agent="husain abbas"
)

# Load posted meme IDs
if os.path.exists("Mega project 1 - MEME-BOT/logs/meme_log.txt"):
    with open("Mega project 1 - MEME-BOT/logs/meme_log.txt", "r") as f:
        posted = set(f.read().splitlines())
        
else:
    posted = set()
print(posted)
# Subreddits to fetch memes from
subs = ["memes", "dankmemes", "me_irl",'funny','brainrot','facts','ipl','sports','chess']
limit = 100
def grab_meme(sub):
    for post in reddit.subreddit(sub).hot(limit=limit):
        if post.id in posted:
            continue
        elif post.id not in posted and post.url.endswith((".jpg", ".png")):
            print(f"Downloading: {post.title}")
            img_data = requests.get(post.url).content
            file_path = f"Mega project 1 - MEME-BOT/memes/{post.id}.jpg"
            with open(file_path, "wb") as f:
                f.write(img_data)
            with open("Mega project 1 - MEME-BOT/logs/meme_log.txt", "a") as f:
                f.write(post.id + "\n")
            break
tasks=[]
for i,sub in enumerate(subs):
    # Create some threads
    tasks.append( threading.Thread(target=grab_meme, args=(sub,)))
    tasks[i].start()
for task in tasks:
    task.join()
print("All downloawding done!")

        
