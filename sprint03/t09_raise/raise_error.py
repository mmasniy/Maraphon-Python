def raise_error(key, msg):
    if key == "value":
        raise ValueError(msg)
    elif key == "key":
        raise KeyError(msg)
    elif key == "index":
        raise IndexError(msg)
    elif key == "memory":
        raise MemoryError(msg)
    elif key == "name":
        raise NameError(msg)
    elif key == "eof":
        raise EOFError(msg)
    else:
        raise ValueError('No error with such key.')
