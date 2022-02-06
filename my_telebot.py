#!/usr/bin/env python
"""
Simple telegram bot. Registered as systemd service on my server.
"""
import telebot

import docker_checker
from mysecrets import CHANNEL_ID, TOKEN

bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(
    commands=["docker"], func=lambda message: message.chat.id == CHANNEL_ID
)
def run_docker_checker_py(message):
    """
    Handle incoming messages
    """
    docker_checker.pull_images()
    mymessage = docker_checker.check_updated()
    bot.send_message(message.chat.id, mymessage)


@bot.message_handler(commands=["help"])
def get_helo(message):
    pass


def run():
    """
    Just run script
    """
    bot.infinity_polling()


if __name__ == "__main__":
    run()
