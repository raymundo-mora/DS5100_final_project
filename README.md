# DS5100_final_project

## 0. Metadata
**Author**: Raymundo Mora <br>
**Project**: Monte Carlo Simulator
Class: DS5100

## 1. Synopsis
### 1.0 Installation
After cloning the repo you can install it by typing <br>
```bash 
pip intsall -e .
```
on your terminal from the root directory.<br>

### 1.1 Importing
You can import the python module by typing running the following after installation<br>
**1.11** `from montecarlo.montecarlo import *` <br>
**1.12** `from montecarlo.montecarlo import [CLASSNAME]`<br>
You can use **1.11** to import the entire module or **1.12** to import individual classes simply by replacing [CLASSNAME] with that of the one you wish to import. <br>

### 1.2 Creating Dice
To create a die instantiate it by passing a list of faces to the **monetecarlo.montecarlo.Die** class. <br>
```python
from montecarlo.montecarlo import Die
die1 = Die(['heads','tails])
```

### 1.3 Playing Games
A at least one **Die** has to have been instantiated to play a game. You must pass a list of die to instantiate an object of type **Game**. The die passed to **Game** can be identical. To play game use the `.play()` method and pass the number of rolls you wish to play as an argument. Use the code below as a guide.<br>
```python
import numpy as np
from montecarlo.montecarlo import *
die1 = Die(['heads','tails])
game1 = Game(np.full(5,die1))
game1.play(5)`<br>
```
To see the results try the following: <br>
```python
game1.show()
```
![image](https://user-images.githubusercontent.com/92943544/179162591-c677d2f8-ef66-4a05-a5d2-0dcafd234dbf.png)
<br>

### 1.4 Analyzing Games
To analyze a game you must instantiate a **Game** object. You can use methods of the **Analyzer** class to <br>
<ol>
  <li>Get the number of jackpots the game returned. </li>
  <li>Get a dataframe for the different combinations that the game rolled and how many times each appeared</li>
  <li>Get a data frame of how many times each face appeared in a given roll</li>
</ol>

<br>

You can test these methods with the code below. <br>
**Instantiate an Analyzer object** <br>
```python
import numpy as np
from montecarlo.montecarlo import *
die1 = Die(['heads','tails'])
game1 = Game(np.full(5,die1))
game1.play(5)
print(game1.show())
analyze1 = Analyzer(game1)
```
**Call the methods on analyze1**<br>
```python
print("njackpots: ",analyze1.jackpot())
print(analyze1.combo())
print(analyze1.face_counts_per_roll())
```

![image](https://user-images.githubusercontent.com/92943544/179264290-6876539b-bc3e-4e0d-a54f-a9ffb0f1baaf.png)

<br>

## 2. API description

### 2.0 Documentation for Classes of the module along with their methods.

### 2.1 montecarlo.montecarlo.Die
```python
class Die:
    """Object with nfaces each with weights that default to 1 but can be changed and that can 
    be rolled n times.   

    Returns:
        montecarlo.montecarlo.Die: 
        _pandas.DataFrame_: Dataframe of length(nfaces) with two columns. A column for the face 
        (int,float,str) and column for the weight that face has (int or float). 
     """
     
        def __init__(self,faces):
            """Die initializer. 
            Args:
                faces (list: int,float, or str): The list of faces that the Die will have. 
            Returns:
                 None:
            """
        def change_w(self,face,weight) ->None:
            """Change the weight of a face in the Die. Changes the value in the private internal
            data frame of the Die.  

            Args:
                face (int,float,str): The face that will have its weight changed.
                weight (int,float): The new weight of the face.

            Returns:
                None:
            """
        def roll(self,nrolls=1)-> list:

            """Rolls the Die n times and returns a list of the face 
            that landed for each roll.

            Args:
                nrolls (int, optional): Number of times the Die should be rolled.
                 Defaults to 1.

            Returns:
                list: list of the 
            """
            
        def show(self) -> pd.DataFrame:
            """Displays and returns the pandas.DataFrame that describes
            the die. (i.e. The data frame of its faces and associated 
            weights.)

            Returns:
                pandas.DataFrame: Data frame describing the Die, that is,
                the data frame of its faces and associated weights. 
            """
```
<br>

### 2.2 montecarlo.montecarlo.Game
```python
class Game: 
    """Groups a list of die to roll n times for a game and saves 
    the results. 
    """
    
    def __init__(self,die_list: list):
        """Game initializer. 

        Args:
            die_list (list): The list of Die objects that will be used for the game.
            All Die objects must have the same faces and the same amount of each face.
            The weights for each Die object may be diffrent. 
        Returns:
            None:
        """
     def play(self,nrolls:int) -> None:
        """Rolls each die n times and saves the results into a private
        internal pandas.DataFrame object.

        Args:
            nrolls (int): The amount of times each Die object should
            be rolled. 

        Returns:
            None:
        """
     def show(self,form='wide')-> pd.DataFrame:
        """Displays the data frame of the results after 
        `Die.play()` has been called. The Data frame does
        not exist if `Die.play()` has not been called. 

        Args:
            form (str, optional): Options ['wide','narrow'].
            The format in which the private data frame of the 
            results from `Game.play()` should be displayed.
            Defaults to 'wide'.

        Returns:
            pd.DataFrame: Data frame displaying the results of
            `Game.play()`
        """
```
<br>

### 2.3 montecarlo.montecarlo.Analyzer
```python
class Analyzer:
    """Class to provide quick analysis of `montecarlo.montecarlo.Game` objects.

    """
    def __init__(self,game: Game) -> None:
        """Initialize Analyzer.

        Args:
            game (Game): Instance of Game.

        Returns:
            None:
        """
    def jackpot(self) -> int:
        """Returns the number of jackpots rolled in the game. 

        Returns:
            int: Number of jackpots rolled in the game. 
        """
     def combo(self)-> pd.DataFrame:
        """Displays how many times each different type of combination 
        landed in a dataframe. The multiindex is the combination and 
        the 'counts' column is how many times that combination landed. 

        Returns:
            pandas.DataFrame: Sorted DataFrame displaying how many times
            each combination was rolled with the combination as the index. 
        """
    def face_counts_per_roll(self) -> pd.DataFrame:
        """Returns a data frame that shows how many times
        each face was appeared in a roll.

        Returns:
            pandas.DataFrame: DataFrame with faces as columns, roll_number as its index
            the number of times each face appeared in that roll as the elemets. 
        """ 
```

## 3. Manifest / Directory Structure 
.
<br>
├── ***montecarlo***<br>
│   ├── \_\_init\_\_.py<br>
│   ├── montecarlo.py<br>
│   └── ***test***<br>
│       ├── \_\_init\_\_.py<br>
│       ├── montecarlo_test.py<br>
│       └── montecarlo_test.txt<br>
├── .gitignore<br>
├── LICENSE<br>
├── README.md<br>
├── montecarlo_demo.ipynb<br>
└── setup.py<br>
<br>
2 directories, 10 files<br>
