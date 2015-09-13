# -*- coding: utf-8 -*-

import os
import sys
import time
import datetime

import click
import pyglet


@click.command()
@click.option('--package', help='Repo of sounds')
def tell_hour(package):
    files = os.listdir(os.path.dirname(package))
    hour = datetime.datetime.now().hour
    package = os.path.abspath(os.path.dirname(package))

    hour_file = [file for file in files if str(hour) == file.split('.')[0]][0]
    prefix_file = 'past.mp3'

    pyglet.resource.path = [package]
    pyglet.resource.reindex()
    player = pyglet.media.Player()
    prefix = pyglet.resource.media(prefix_file)
    hour = pyglet.resource.media(hour_file)
    player.queue(prefix)
    player.queue(hour)
    player.play()

    def exiter(dt):
        pyglet.app.exit()

    pyglet.clock.schedule_once(exiter, prefix.duration + hour.duration)
    pyglet.app.run()


if __name__ == '__main__':
    tell_hour()
    time.sleep(3)
    sys.exit(0)
