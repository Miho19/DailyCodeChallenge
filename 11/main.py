
def _step(l: list, steps, n, climb_amount):

    if steps == n:
        print(str(l))
        return
    if steps > n:
        return
    
    for step in climb_amount:
        ans = l.copy()
        ans.append(step)
        _step(ans, steps + step, n, climb_amount)

def step_climb(n, X=[1, 2]):
    ans = []

    _step(ans, 0, n, X)


step_climb(4, [1, 2, 3])