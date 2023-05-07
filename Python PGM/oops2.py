from tkinter import N


class Number:
    def _inti_(self, num):
        self.num=num

    def __add__(self,num2):
        print("Lets add")
        return self.num + num2.num      
n1 = Number(5) 
n2 = Number(6)
sum = n1 + n2
print(sum)