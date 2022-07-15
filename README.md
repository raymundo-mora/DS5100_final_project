# DS5100_final_project

## Metadata
**Author**: Raymundo Mora <br>
**Project**: Monte Carlo Simulator
Class: DS5100

## Synopsis
### 1.0 Installation
After cloning the repo you can install it by typing <br>
`pip intsall -e .` <br>
from the root directory.<br>

### 1.1 Importing
You can import the python module by typing running the following after installation<br>
**1.11** `from montecarlo.montecarlo import *` <br>
**1.12** `from montecarlo.montecarlo import [CLASSNAME]`<br>
You can use **1.11** to import the entire module or **1.12** to import individual classes simply by replacing [CLASSNAME] with that of the one you wish to import. <br>

### 1.2 Creating Dice
To create a die instantiate it by passing a list of faces to the **monetecarlo.montecarlo.Die** class. <br>
`from montecarlo.montecarlo import Die` <br>
`die1 = Die(['heads','tails])`<br>

### 1.3 Playing Games
A at least one **Die** has to have been instantiated to play a game. You must pass a list of die to instantiate an object of type **Game**. The die passed to **Game** can be identical. To play game use the `.play()` method and pass the number of rolls you wish to play as an argument. Use the code below as a guide.<br>
`import numpy as np`<br>
`from montecarlo.montecarlo import *`<br>
`die1 = Die(['heads','tails])`<br>
`game1 = Game(np.full(5,die1))`<br>
`game1.play(5)`<br>
To see the results try the following: <br>
`game1.show()`<br>
![image](https://user-images.githubusercontent.com/92943544/179162591-c677d2f8-ef66-4a05-a5d2-0dcafd234dbf.png)
<br>

### 1.4 Analyzing Games




<br>
This repository contains all of the files for my final project submission for DS5100. 





## Directory Structure 
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
