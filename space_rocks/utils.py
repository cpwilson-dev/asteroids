from pygame.image import load


def load_sprite(name, with_alpha=True):
    path = f"assets/sprites/{name}.png"
    load_sprite = load(path)

    if with_alpha:
        return load_sprite.convert_alpha()
    else:
        return load_sprite.convert()
