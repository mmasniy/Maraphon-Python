import re

name = r"[\w]+$"
email = r"[^@]+@[^@]+.[^@]+$"


def contacts(container, info, operator):
    if operator in ["add", "delete", "update"] or re.match(email, info["email"]) or re.match(name, info["name"]):
        pass
