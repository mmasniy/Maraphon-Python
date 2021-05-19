def witch_hunt(suspect_sets, innocent_sets):
    if suspect_sets:
        suspect = set.intersection(*suspect_sets)
        if innocent_sets:
            innocent = set.union(*innocent_sets)
            result = suspect.difference(innocent)
            return result
        else:
            return suspect
    else:
        return set()
