from logging import exception, raiseExceptions
import settings

def height_prct(value):
    if value < 100:
        return (settings.HEIGHT * value) / 100
    else:
        raise Exception("Sorry, no numba")

def width_prct(value):
    if value < 100:
        return (settings.WIDTH * value) / 100
    else:
        raise Exception("Sorry, no numba")
