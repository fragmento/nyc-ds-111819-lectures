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


def by_rank(number, music_list):
    for v in music_list:
        if int(number) == int(v['number']):
            return v


def by_year(year, music_list):
    same_year = []
    for v in music_list:
        if int(year) == int(v['year']):
            same_year.append(v)
    return same_year


def by_years(year1, year2, music_list):  # first year has to be smaller than second year
    same_year = []

    for v in music_list:
        if int(year1) <= int(v['year']) and int(year2) >= int(v['year']):
            same_year.append(v)
    return same_year


# first rank has to be smaller than second rank

def by_ranks(rank1, rank2, music_list):
    ranks = []

    for v in music_list:
        if int(rank1) <= int(v['number']) and int(rank2) >= int(v['number']):
            ranks.append(v)
    return ranks


def titles(key, music_list):
    title = []
    for v in music_list:
        title.append(v[key])
    return title


def most_frequent(key, music_list):
    newDict = dict()
    # creates a dictionary key = key and values = frequency
    frequent_dic = Counter(titles(key, music_list))
    dic_freq = dict(frequent_dic)  # counter type into dictionary
    for (key, value) in dic_freq.items():
        freq_list = []
        if value == max(dic_freq.values()):
            newDict[key] = value
    return list(newDict.keys())
