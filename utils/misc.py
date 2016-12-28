import random
import config
from flask import request

allowed_chars = "abcdefghijklmnopqrstuvwxyz0123456789"


def generate_random_string(length=32, chars=allowed_chars):
    r = random.SystemRandom()
    return "".join([r.choice(chars) for i in range(length)])


def generate_team_key():
    return config.site_name.lower() + "_" + generate_random_string(32, allowed_chars)


def generate_confirmation_key():
    return generate_random_string(48)


def get_ip():
    return request.headers.get(config.proxied_ip_header, request.remote_addr)

