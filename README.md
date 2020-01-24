# The-Mandalorian

This game is a terminal version of Jetpack Joyride. Dodge obstacles, collect coins, and fight the fierce dragon to win the game! 

## Setup

Libraries used :

```bash
pip3 install colorama
```

## Execution

To play :

```bash
git clone https://github.com/mallika2011/The-Mandalorian.git
cd The-Mandalorian
python3 play.py
```

## Rules

**a** - To move left

**w** - To move up

**d** - To move right

**l** - To shoot

**q** - To quit

**Spacebar**- To activate shield

## Features

* Fire beams (vertical, horizontal and 45 degrees) appear through the course of the game

* Power up, speed boosters increase the speed of the game. This powerup lasts 5s

* The shield can be activated to protect mando from obstacles

* A magnet appears on the way that attracts mando both in the x and y axes (Overcome it's force else you lose)

* The last phase involves fighting the mighty dragon shooting iceballs

## Concepts Used

* Inheritance: Common attributes of the parent class inherited by the child classes. (Helps in avoiding redundant code)

```python
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
```

* Polymorphism: Utililizing the same function of a parent class for different functionalites of child classes based on the list of parameters passed

```python 
class Objects:

    def __init__(self, x, y):
        self._x = x
        self._y = y
        # self.shape=np.zeros((100), dtype='<U1000')

    def setx(self, x):
        self._x=x
    def sety(self,y):
        self._y=y
    def getx(self):
        return self._x
    def gety(self):
        return self._y

    def show(self,grid,shape,x,y):
        #POLYMORPHISM USED TO SHOW/DISPLAY ALL OBJECTS
        for i in range(x,x+len(shape)):
            for j in range(y,y+len(shape[0])):
                grid[i][j]=shape[i-x][j-y]
```

* Encapsulation: Every component on the board is an object of a class. This instantiation encapsulates the methods and attributes of the objects.

* Abstraction: The functions of each class hide the inner details of the function enabling users to use just the function name.

```python
obj_iceballs_array[i].shoot(obj_board.grid)
```
