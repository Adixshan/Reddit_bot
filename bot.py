
import praw
import requests
import schedule
import time
import logging
from config import (
    REDDIT_CLIENT_ID, REDDIT_SECRET, REDDIT_USERNAME, REDDIT_PASSWORD, USER_AGENT,
    GROQ_API_URL, GROQ_API_KEY
)

# Configure logging
logging.basicConfig(
    filename="logs/bot.log", level=logging.INFO, format="%(asctime)s - %(message)s"
)

# Reddit API Authentication
def reddit_auth():
    reddit = praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_SECRET,
        username=REDDIT_USERNAME,
        password=REDDIT_PASSWORD,
        user_agent=USER_AGENT,
    )
    logging.info("Authenticated with Reddit API.")
    return reddit

# Generate content using Groq AI
def generate_content():
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}"}
    data = {
        "model": "llama3-70b-8192",  # Updated model name
        "messages": [
            {"role": "system", "content": "You are a creative assistant."},
            {"role": "user", "content": "Generate a creative post about AI"}
        ],
        "max_tokens": 100
    }
    
    try:
        response = requests.post(GROQ_API_URL, headers=headers, json=data, timeout=10)
        response.raise_for_status()
        content = response.json().get("choices", [{}])[0].get("message", {}).get("content", "Default AI-generated content.")
        logging.info("Content generated successfully.")
        return content
    except requests.exceptions.RequestException as e:
        logging.error(f"Error generating content: {e}")
        return "AI-generated content unavailable."

# Post content to Reddit
def post_to_reddit(reddit, subreddit_name):
    try:
        subreddit = reddit.subreddit(subreddit_name)
        content = generate_content()
        submission = subreddit.submit(title="AI-Generated Post", selftext=content)
        logging.info(f"Posted to r/{subreddit_name}. URL: {submission.url}")
        print(f"Post created: {submission.url}")
    except Exception as e:
        logging.error(f"Error posting to Reddit: {e}")
        print(f"Error: {e}")

# Schedule daily posts
def schedule_posts(reddit, subreddit_name, post_time):
    schedule.every().day.at(post_time).do(post_to_reddit, reddit, subreddit_name)
    logging.info(f"Scheduled daily posts to r/{subreddit_name} at {post_time}.")

    print(f"Bot is running and will post daily to r/{subreddit_name} at {post_time}.")
    while True:
        schedule.run_pending()
        time.sleep(1)

# Main Function
if __name__ == "__main__":
    reddit = reddit_auth()
    subreddit_name = input("Enter the subreddit name: ")
    post_time = "22:54"  # 9:00 PM in 24-hour format
    schedule_posts(reddit, subreddit_name, post_time)


