from tree import*

def IsSkewRight(P):
    if IsTreeEmpty(P):
        return False
    else:
        if IsUnerRight(P) == True and not IsOneElement(P):
            return IsSkewRight(Right(P))
        if IsOneElement(P):
            return True
        else:
            return False

S = MakePB(1, MakePB(3, MakePB(4, MakePB(6, None, None), None), None), None)
P = MakePB(3, MakePB(4, MakePB(5, MakePB(6, MakePB(8, None, None), MakePB(9, None, None)), None), None), None)

print(S)
print(P)
print(IsSkewRight(S))
print(IsSkewRight(P))