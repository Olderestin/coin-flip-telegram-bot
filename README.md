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
## Launch the bot:

### Through virtual environment

1. Clone the repository:
   ```bash
   git clone https://github.com/Olderestin/coin-flip-telegram-bot.git

3. Navigate to the project directory:
   ```bash
   cd coin-flip-telegram-bot
   
1. Create virtual environment:
    ```bash
    python -m venv venv

2. Activate venv:
    ```bash
    venv\Scripts\activate

3. Install pip:
    ```bash
    python -m pip install --upgrade pip

4. Install dependencies:
    ```bash
    pip install -r requirements.txt

5. Create a .env file based on the provided example (<font color='red'>**don't forget to insert the token there**</font>):
   ```bash
   cd src
   cp .env.example .env

6. Run the bot:
    ```bash
    python main.py

### Through Docker

1. Clone the repository:
   ```bash
   git clone https://github.com/Olderestin/coin-flip-telegram-bot.git

3. Navigate to the project directory:
   ```bash
   cd coin-flip-telegram-bot/src    

5. Create a .env file based on the provided example (<font color='red'>**don't forget to insert the token there**</font>):
   ```bash
   cp .env.example .env

6. Run bot with docker:
   ```bash
   cd ..
   docker compose up

___
## Note:

- sqlite3 database is used to save usage statistics. Database folder `src/storage` 




