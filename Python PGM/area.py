from platform import java_ver
from re import I


class C2dvec:
    def __init__(self,i,j,k):
        self.icap = i
        self.jcap = j
        self.kcap = k

    def __str__(self) :
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"

class C3dvec(C2dvec):
    def __init__(self, i, j,k):
        super().__init__(i, j,k)
        self.kcap = k

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j +{self.kcap}k"

v2d=C2dvec(1,3,9)
v3d=C3dvec(1,9,7)
print(v2d)
print(v3d)
