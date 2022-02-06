#!/usr/bin/env python
"""
Simple script to check availability of new docker images from hub.docker.com
"""
import docker

from helpers import mylogger

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
            mylogger.info("New image version pulled for %s", name)
        myimages.append(name)
    if not message:
        message = "No updates found."
        mylogger.info(message)
    else:
        message = "Following Docker images have updates:\n" + message
    return message
