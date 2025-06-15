from pygame import Vector2
from pygame.image import load


def load_sprite(name, with_alpha=True):
    path = f"assets/sprites/{name}.png"
    load_sprite = load(path)

    if with_alpha:
        return load_sprite.convert_alpha()
    else:
        return load_sprite.convert()


def wrap_position(position, surface):
    x, y = position
    w, h = surface.get_size()
    return Vector2(x % w, y % h)
