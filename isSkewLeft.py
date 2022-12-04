from tree import*

def IsSkewLeft(P):
    if IsTreeEmpty(P):
        return False
    else:
        if IsUnerLeft(P) == True and not IsOneElement(P):
            return IsSkewLeft(Left(P))
        if IsOneElement(P):
            return True
        else:
            return False

S = MakePB(1, MakePB(2, MakePB(4, MakePB(6, None, None), None), None), None)
P = MakePB(1, MakePB(2, MakePB(4, MakePB(6, MakePB(8, None, None), MakePB(9, None, None)), None), None), None)

print(S)
print(P)
print(IsSkewLeft(S))
print(IsSkewLeft(P))