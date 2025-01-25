# Reddit AI Bot

This project is a Reddit bot that automatically generates content using Groq AI and posts it to a subreddit of your choice. It runs on a schedule and posts once a day at the time you specify. The bot uses the **Reddit API** to make posts and **Groq AI** to generate the content.

## Features

- **Automatic daily posts**: The bot will post AI-generated content to a subreddit once per day at your chosen time.
- **Groq AI-powered content generation**: It pulls creative content using Groq's API to keep your posts fresh and engaging.
- **Error handling and logging**: If something goes wrong during the process, errors are logged so you can quickly troubleshoot.
- **Customizable**: You can choose the subreddit and specify exactly when you want the posts to go live.

## Requirements

Before getting started, make sure you have the following:

- Python 3.x installed.
- The `requests` library (to make API calls).
- The `praw` library (to interact with Reddit).
- The `schedule` library (to run the bot on your desired schedule).
- **Groq API Key** for generating AI content.
- **Reddit API credentials** (Client ID, Secret, Username, Password).
- Make logs folder and place the bot.log file inside it

## Getting Started

Follow these steps to get the bot up and running:

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/reddit-ai-bot.git
cd reddit-ai-bot
