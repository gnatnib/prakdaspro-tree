from tree import*

def IsMemberTree (P,X):
    if IsTreeEmpty(P):
        return False
    else:
        if Akar(P) == X:
            return True
        else:
            return IsMemberTree(Left(P), X) or IsMemberTree(Right(P), X)


S = MakePB(2,None,MakePB(3,None,MakePB(4,None,MakePB(5,None,None))))
P = MakePB(1,MakePB(2,MakePB(4, MakePB(6,None,None), None), None), None)

print(S)
print(P)
print (IsMemberTree(S,5))
print(IsMemberTree(P,7))