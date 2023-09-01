# YouTube Subtitle Summarizer Bot

## Overview

The YouTube Subtitle Summarizer Bot is a Telegram bot that allows users to send YouTube video links and receive summarized versions of the video's subtitles. The bot utilizes the ChatGPT API to generate concise summaries and offers an optional translation feature for the generated summaries.

## Features

- Receive YouTube video links from users.
- Download subtitles from the provided YouTube video.
- Generate a summary of the subtitles using the ChatGPT API.
- Optionally translate the summary to another language.
- Seamless integration with Telegram for a user-friendly experience.

## Getting Started

### Prerequisites

Before you can run this Telegram bot, you'll need the following:

- Python 3.x
- Telegram bot token (obtained by creating a bot on Telegram)
- OpenAI GPT-3 API key (for ChatGPT integration)
- Dependencies listed in `requirements.txt`
- You may have some problems with googletrans library, because it has not been updated for a long time. This [answer](https://stackoverflow.com/questions/72796594/attributeerror-module-httpcore-has-no-attribute-synchttptransport) helped me.

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yaroslavpoltoran/youtube_subtitle_summarizer_bot.git
   cd youtube-subtitle-summarizer-bot
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root directory and add your Telegram bot token and GPT-3 API key. See .example_env for an example.

   ```python
   OPENAI_API_KEY=
   TELEGRAM_TOKEN=
   ```

### Usage

1. Start the bot by running the following command:

   ```bash
   python bot.py
   ```

2. Open Telegram and search for your bot by its username.

3. Start a conversation with the bot and send a YouTube video link.

4. The bot will download the subtitles, generate a summary using ChatGPT, and optionally translate it (if configured).

5. Enjoy the summarized content!

## Configuration

You can customize the bot's behavior by modifying the configuration options in `config.py`. You may want to adjust the language settings, translation preferences, summary length, generating settings and more to suit your requirements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Telegram Bot API](https://core.telegram.org/bots/api)
- [OpenAI GPT-3](https://beta.openai.com/)

## Contributing

If you'd like to contribute to this project, please open an issue or submit a pull request. We welcome your input!

## Contact

For any questions or feedback, feel free to contact the project maintainer:

Yaroslav Poltoran

Telegram me: https://t.me/yaroslavpoltoran

Happy summarizing! 🚀