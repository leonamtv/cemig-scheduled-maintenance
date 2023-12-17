from random import choice
from .user_agents import user_agents


def get_headers():
    return {'User-Agent': choice(user_agents)}

