from config import SEED


def get_formatted_name(name: str):
    return "{0}_{1}".format(SEED, name)
