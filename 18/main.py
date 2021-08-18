

def solve(l :list, word: str):
    
    for s in l:
        if word in (''.join(map(str, s))):
            return True
    
    for s in zip(*l):
        if word in (''.join(map(str, s))):
            return True

    return False



example = [['F', 'A', 'C', 'I'],['O', 'B', 'Q', 'P'],['A', 'N', 'O', 'B'],['M', 'A', 'S', 'S']]


print(solve(example, 'FOAM'))
print(solve(example, 'MASS'))
print(solve(example, 'DEAD'))
