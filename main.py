def fct(word,shift):
    return [word[i::shift] for i in range(shift)]
print(fct('fbboaaorz',3))
