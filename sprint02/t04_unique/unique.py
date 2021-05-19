def make_unique(dict_old):
    for key in dict_old:
        dict_old[key] = sorted(list(set(dict_old[key])))
    return dict_old
