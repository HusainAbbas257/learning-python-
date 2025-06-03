from instagrapi import Client

# Credentials
userid = 'itchy__balls'
with open('C:/Users/DELL/Desktop/api-keys/instagram_paasword.txt') as f:
    password = f.read().strip()

# Login
cl = Client()
cl.login(userid, password)

# Get your latest media
media = cl.account_medias(amount=1)[0]
media_id = media.id

# Get comments
comments = cl.media_comments(media_id)

# Reply to each
for comment in comments:
    username = comment.user.username
    text = f"@{username} thanks bro!"
    cl.media_comment(media_id, text)
