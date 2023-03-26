def concatenate(*args, **kwargs):
    concatenated_text = ''.join(args)
    for key, value in kwargs.items():
        concatenated_text = concatenated_text.replace(key, value)
    return concatenated_text

