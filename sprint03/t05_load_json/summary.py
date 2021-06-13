import json


def summary(filename, summarize_by):
    summary_returned = dict()
    with open(filename, "r") as file:
        try:
            json_file = json.load(file)
            for item in json_file:
                key = item.get(summarize_by)
                try:
                    hash(key)
                except TypeError:
                    key = "unhashable"
                if key in summary_returned:
                    summary_returned[key] += 1
                else:
                    summary_returned[key] = 1
            return dict(sorted(summary_returned.items(), key=lambda x: x[1], reverse=True))
        except json.decoder.JSONDecodeError:
            return "Error in decoding JSON."
