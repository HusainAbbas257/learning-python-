import schedule
import time as t

def job():
    print("Posting new meme...")
    # call your upload logic here
    import instagram_post

schedule.every().day.at("12:00").do(job)  # change time here
schedule.every().day.at("6:00").do(job)
while True:
    schedule.run_pending()
    t.sleep(300)
