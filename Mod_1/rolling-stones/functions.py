def by_name(album, music_list):
    for v in music_list:
        if album == v['album']:
            return v


def by_artist(artist, music_list):  # returns all albums by the same artist
    hits = []
    for v in music_list:
        if artist == v['artist']:
            hits.append(v['album'])
    return hits
