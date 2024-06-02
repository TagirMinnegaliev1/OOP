from builtins import print as original_print

def print(*args):
    text = ' '.join(map(str, args))
    original_print(text.upper())

print('Нельзя ли потише?')