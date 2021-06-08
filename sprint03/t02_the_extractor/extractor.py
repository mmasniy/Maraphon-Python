def extractor(extractable, value_type=str):
    return dict(filter(lambda i: isinstance(i[1], value_type), extractable.items()))
