import math

def solution2(x, y, d):
    diff = y - x
    if diff == 0:
        return 0
    elif diff > 0:
        div = diff / float(d)
        return int(round(math.ceil(div)))
