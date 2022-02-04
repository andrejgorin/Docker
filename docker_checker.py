#!/usr/bin/env python
"""
Simple script to check availability of new docker images from hub.docker.com
"""
import logging
import sys

import docker
import telebot

from mysecrets import CHANNEL_ID, TOKEN

logger = logging.getLogger() # TODO
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter(
    "%(asctime)s - docker_checker - %(levelname)s - %(message)s"
)
handler.setFormatter(formatter)
logger.addHandler(handler)

bot = telebot.TeleBot(TOKEN, parse_mode=None)

client = docker.from_env()


def get_name(image):
    """
    Get image name from "image" object
    """
    name = image.attrs["RepoDigests"][0]
    name = name.split("@")
    name = name[0]
    return name


def pull_images():
    """
    Pull images from hub.docker.com
    """
    image_list = client.images.list()
    for image in image_list:
        name = get_name(image)
        client.images.pull(name)


def check_updated():
    """
    Check if there are more than one image version pulled
    """
    image_list = client.images.list()
    message = ""
    myimages = []
    for image in image_list:
        name = get_name(image)
        if name in myimages:
            message += name
            message += "\n"
            logger.info("New image version pulled for %s", name)
        myimages.append(name)
    if message:
        bot.send_message(CHANNEL_ID, message)


def run():
    """
    Just run script
    """
    pull_images()
    check_updated()


if __name__ == "__main__":
    run()
