from headers import *

class Person():

    #Class defining generic 
    def __init__(self, x_cood, y_cood):
        #Protected variables to be inherited
        self._x_cood=x_cood                 
        self._y_cood=y_cood

    def getx(self):
        return self._x_cood

    def setx(self,x):
        self._x_cood=x

    def gety(self):
        return self._y_cood

    def sety(self,y):
        self._y_cood=y