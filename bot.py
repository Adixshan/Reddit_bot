import praw
import requests
import schedule
import time
import logging
from config import (
    REDDIT_CLIENT_ID, REDDIT_SECRET, REDDIT_USERNAME, REDDIT_PASSWORD, USER_AGENT,
    GROQ_API_URL, GROQ_API_KEY
)

# Setting up logging to keep track of errors and actions
logging.basicConfig(
    filename="logs/bot.log", level=logging.INFO, format="%(asctime)s - %(message)s"
)

# Function to connect to Reddit (authentication)
def reddit_connect():
    reddit_instance = praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_SECRET,
        username=REDDIT_USERNAME,
        password=REDDIT_PASSWORD,
        user_agent=USER_AGENT,
    )
    logging.info("Connected to Reddit successfully.")
    return reddit_instance

# Generate content using Groq API
def create_content():
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}"}
    payload = {
        "model": "llama3-70b-8192",  # The model used for content generation
        "messages": [
            {"role": "system", "content": "You're a cool creative assistant."},
            {"role": "user", "content": "Write something cool about AI!"}
        ],
        "max_tokens": 100  # Maximum token limit
    }
    
    try:
        response = requests.post(GROQ_API_URL, headers=headers, json=payload, timeout=10)
        response.raise_for_status()  # Will throw an error for any status code > 400
        content = response.json().get("choices", [{}])[0].get("message", {}).get("content", "Oops, no content generated.")
        logging.info("Content generated successfully.")
        return content
    except requests.exceptions.RequestException as err:
        logging.error(f"Problem generating content: {err}")
        return "AI-generated content not available."

# Function to post content to Reddit
def post_on_reddit(reddit_instance, subreddit):
    try:
        sub = reddit_instance.subreddit(subreddit)  # Access the subreddit
        content = create_content()  # Generate content
        post = sub.submit(title="AI Generated Post", selftext=content)  # Post content
        logging.info(f"Posted on r/{subreddit}. URL: {post.url}")
        print(f"Post created! Check it here: {post.url}")
    except Exception as err:
        logging.error(f"Error posting to Reddit: {err}")
        print(f"Error occurred: {err}")

# Function to schedule posts
def schedule_posts_daily(reddit_instance, subreddit, post_time):
    schedule.every().day.at(post_time).do(post_on_reddit, reddit_instance, subreddit)  # Schedule the post
    logging.info(f"Scheduled posts to r/{subreddit} at {post_time} daily.")

    print(f"Bot is working and will post to r/{subreddit} at {post_time} every day.")
    while True:
        schedule.run_pending()  # Run any scheduled tasks
        time.sleep(1)  # Sleep for a second to avoid high CPU usage

# Main function to start everything
if __name__ == "__main__":
    reddit_instance = reddit_connect()  # Get Reddit instance
    subreddit_input = input("Enter the name of the subreddit: ")  # Ask user for subreddit
    post_time_input = "22:54"  # Set post time to 10:54 PM (24-hour format)
    schedule_posts_daily(reddit_instance, subreddit_input, post_time_input)
