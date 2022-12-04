from tree import*


def LevelOfX(P,X):
    if not IsMemberTree(P,X):
        return 0
    else:
        if IsBiner(P):
            return 1 + LevelOfX(Left(P), X) + (LevelOfX(Right(P), X))
        elif IsUnerLeft(P):
            return 1 + LevelOfX(Left(P),X)
        elif IsUnerRight(P):
            return 1 + LevelOfX(Right(P),X)

P = MakePB(2,MakePB(3,MakePB(1,None,None), MakePB(5, None, None)), MakePB(3,MakePB(2,None,None), MakePB(4, None, None)))
print (P)
print (LevelOfX(P,3))