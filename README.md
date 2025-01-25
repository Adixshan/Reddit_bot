# Reddit AI Bot

This project is a Reddit bot that automatically generates content using the Groq AI and posts it to a specified subreddit. The bot runs on a schedule, posting once daily at the specified time. The project uses the **Reddit API** for posting and **Groq AI** for content generation.

## Features

- **Automated daily posts**: The bot will post AI-generated content to a subreddit at a user-specified time every day.
- **Content generation using Groq AI**: The bot uses Groq's API to generate creative and engaging content.
- **Basic error handling and logging**: Errors during API requests are logged and handled gracefully.
- **Configurable subreddit and post time**: The user can choose the subreddit and specify the time at which posts should be made.

## Requirements

- Python 3.x
- `requests` library for making HTTP requests.
- `praw` library for interacting with Reddit.
- `schedule` library for scheduling the bot to post content at a specific time.
- **Groq API Key** for generating AI content.
- **Reddit API credentials** (Client ID, Secret, Username, Password).

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/reddit-ai-bot.git
cd reddit-ai-bot
