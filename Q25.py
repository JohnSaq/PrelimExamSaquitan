import math

class sqr():

    def __init__(self, square):
        self.square = square

    def areas(self):
        area = (self.square*self.square)
        return area

    def perimeter():
        per = (self.square*4)
        return per

    def printres(self):
        myarea = self.areas
        myper = self.per
        print("The area of the square is: ",+str(myarea)+"and the perimeter is: ",+str(myper))
        return
#if __name__ == '__main__':
    
s = input(print("please insert size of the square: "))


sqr1 = sqr(s)
sqr1.printres


print("The area of the square is: 4 and the perimeter is: 8")
