def song(verses, chorus):
    song_list = []
    for item in verses:
        for line in item:
            song_list.append(line)
        for line in chorus:
            song_list.append(line)
    for line in chorus:
        song_list.append(line)
    return tuple(song_list)
