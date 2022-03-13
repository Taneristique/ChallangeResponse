"Simplified version of code in main.ipynb:)"
def fct(word,shift):
    return [word[0+i:len(word):shift] for i in range(shift)]
print(fct('fbboaaorz',3))
