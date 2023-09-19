# Platzibot clone
### Telegram Bot with OpenAI Integration

This repository contains a Telegram bot capable of responding to chat messages using the OpenAI language model. It continuously checks for new messages in a Telegram chat and generates responses based on user input.

The fine tuning was carried out with the openAI platform, the dataset contains numerous questions and answers about Platzi, an educational website in the Spanish language.

## Getting Started

To run this bot, you'll need to have the following libraries and tools installed:

- Python 3.6 or higher
- `openai` library (install using `pip install openai`)
- `requests` library (install using `pip install requests`)
- You will also need to create a new chatbot with using `Telegram BotFather`

## Usage
- The bot responds to any message received in the Telegram chat.
- User messages are used as prompts for the OpenAI language model to generate responses.
- You can customize the behavior of the bot by modifying the model settings in main.py

## Deploy
You can deploy the chatbot using [telegram bot api](https://tdlib.github.io/telegram-bot-api/build.html?os=Windo)