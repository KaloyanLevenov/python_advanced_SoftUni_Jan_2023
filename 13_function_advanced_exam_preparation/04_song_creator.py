def add_songs(*args):
    register = dict()

    for title, lyrics in args:

        if title not in register.keys():
            register[title] = lyrics

        else:
            register[title].extend(lyrics)

    result = []

    for title, lyrics_list in register.items():
        result.append(f"- {title}")
        if lyrics_list:
            result.extend(lyrics_list)

    return '\n'.join(result)