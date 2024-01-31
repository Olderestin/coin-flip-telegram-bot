# Test task: Telegram bot for tossing a coin

This bot is built using the `python-telegram-bot` library and provides three commands: `Flip`, `Stats` and `About`.

## Description of commands:

### 1. Flip

The `Flip` command is intended for flipping a coin. The bot simulates a random coin toss and responds with the result - "Heads" or "Tails".

### 2. Stats

The `Stats` command displays coin toss statistics for each user. The bot tracks the number of flips and results for each user.

### 3. About

The `About` command displays information about the bot.

___

## Prerequisites

- **Required**: Python 3.x, Docker
- **For pip method**: pip
- **For poetry method**: poetry
- **For Docker method**: only Docker
___
## Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/Olderestin/coin-flip-telegram-bot.git

2. Navigate to the project directory:
   ```bash
   cd coin-flip-telegram-bot

3. Create a .env file based on the provided example (<font color='red'>**don't forget to fill it**</font>):
   ```bash
   cp .env.example .env

___

## Method 1: Using pip

1. Install dependencies:
    ```bash
    pip install -r requirements.txt

2. Up the database with docker:
    ```bash
    docker compose -f docker-compose-local.yml up --build -d

3.  Run the bot:
    ```bash
    python -m bot

___

## Method 2: Using Poetry

1. Install dependencies:
    ```bash
    poetry install

2. Up the database with docker:
    ```bash
    docker compose -f docker-compose-local.yml up --build -d

3.  Run the bot:
    ```bash
    poetry run python -m bot

___

## Method 3: Using Docker

1. Build and run bot with Docker container:
   ```bash
   docker compose up --build

___
## Note:

- Redis database is used to save usage statistics. Database folder `bot/storage`
- logs folder `bot/storage`
