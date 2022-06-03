let = {'h','e','l','o'}
def rank(word:str):
    wlet = set(word)
    score = len(wlet.difference(let))
    return score
print(rank("hello"))
print(rank("there"))