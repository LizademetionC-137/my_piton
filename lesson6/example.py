l = [1,2,4]
s = [2,5,7]

def intersect(seq1,seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res

print(intersect(l,s))

