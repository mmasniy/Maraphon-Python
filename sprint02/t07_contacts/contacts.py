import re


def contacts(container, info, operator):
    name_re = r"[\w]+$"
    email_re = r"[^@]+@[^@]+.[^@]+$"

    if "email" in info and "name" in info \
            and re.match(email_re, info.get("email")) \
            and re.match(name_re, info.get("name")):
        if operator == "add":
            container[info.pop("email")] = info
            return True
        elif operator == "update" and info.get("email") in container:
            email = info.pop("email")
            for key, value in info.items():
                key_container = container[email].get(key)
                if key_container and value != container[email].get(key) or not key_container:
                    container[email][key] = info.get(key)
            return True
        elif operator == "delete" and info.get("email") in container:
            container.pop(info.get("email"))
            return True
        else:
            return False
    else:
        return False
