'''
Author: RaymundoMora 
@linkedin: https://www.linkedin.com/in/raymundo-mora/ 
@github: https://github.com/raymundo-mora 
@url: 

Description: This file contains of the classes created for the 
Monte Carlo Simulator. This is for the final project of DS5100.

Created: 2022-07-08
Modified 2022-07-15
''' 
# %% 
import numpy as np
import pandas as pd
import random
class Die:
    """Object with nfaces each with weights that default to 1 but can be changed and that can 
    be rolled n times.   

    Returns:
        montecarlo.montecarlo.Die: 
        _pandas.DataFrame_: Dataframe of length(nfaces) with two columns. A column for the face 
        (int,float,str) and column for the weight that face has (int or float). 
    """

    # Initializer
    def __init__(self,faces):
        """Die initializer. 
        Args:
            faces (list: int,float, or str): The list of faces that the Die will have. 
        Returns:
             None:
        """
        w = list(np.full(len(faces),1.0))
        
        self._die_df = pd.DataFrame({'face':faces,
                                  'weight':w
                                  })
        self._die_df.index.name = 'roll_num'
        return None
    # Method 1 
    def change_w(self,face,weight) ->None:
        """Change the weight of a face in the Die. Changes the value in the private internal
        data frame of the Die.  

        Args:
            face (int,float,str): The face that will have its weight changed.
            weight (int,float): The new weight of the face.

        Returns:
            None:
        """

        ## Validate arguments
        face_val = face in list(self._die_df['face'])
        wtypes = [int,float]
        wval = type(weight) in wtypes
        if face_val== False:
            raise Exception(f'{face} is not a face in this `Die`')
        elif wval == False:
            raise TypeError(f'Expected weight of type `int` or `float` not {type(weight)}.')
        else:
            i = self._die_df[self._die_df['face'] == face].index[0]
            self._die_df.loc[i,'weight'] = weight
            return None
    # Method 2 
    def roll(self,nrolls=1)-> list:
        
        """Rolls the Die n times and returns a list of the face 
        that landed for each roll.

        Args:
            nrolls (int, optional): Number of times the Die should be rolled.
             Defaults to 1.

        Returns:
            list: list of the 
        """
        isint = type(nrolls) == int
        if isint == False:
            raise TypeError(f'Expected nrolls of type `int` not {type(nrolls)}.')   
        outcomes = random.choices(self._die_df.face,weights=self._die_df.weight,k=nrolls)
        return outcomes
    
    # Method 3 
    def show(self) -> pd.DataFrame:
        """Displays and returns the pandas.DataFrame that describes
        the die. (i.e. The data frame of its faces and associated 
        weights.)

        Returns:
            pandas.DataFrame: Data frame describing the Die, that is,
            the data frame of its faces and associated weights. 
        """
        return self._die_df
# %% 
die1 = Die(['heads','tails'])
die1._die_df
# %% 
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
        # Make sure all Die in list are of same kind and similarly defined. 
        l1 = []
        for die in die_list:
            l1.append(list(die._die_df.face.sort_values()))
        assert l1.count(l1[0]) == len(l1), 'All "Die" objects must have the same faces\
                                            and the same amount of each face.'


        self.die_list = die_list

        return None

    # Method 1 
    def play(self,nrolls:int) -> None:
        """Rolls each die n times and saves the results into a private
        internal pandas.DataFrame object.

        Args:
            nrolls (int): The amount of times each Die object should
            be rolled. 

        Returns:
            None:
        """
        self._df = pd.DataFrame()
        count = 0 
        for die in self.die_list:
            outcome = die.roll(nrolls)
            self._df[count] = outcome
            count += 1 
        return None

    # Method 2 
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
        if hasattr(self,'_df') == False:
            raise Exception("Must call `self.play()` before `self.show()")
        form = form.lower()
        if form == 'wide':
            return self._df
        elif form == 'narrow':
            self._df = self._df.stack()
            self._df.index.names = ['roll','die']
            return self._df

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

        self.game = game
        return None
    # Method 1 
    def jackpot(self) -> int:
        """Returns the number of jackpots rolled in the game. 

        Returns:
            int: Number of jackpots rolled in the game. 
        """
        s = self.game._df.eq(self.game._df.iloc[:, 0], axis=0).all(1)
        njackpot = s.sum()
        jackpot_df = self.game._df.loc[np.where(s==True)[0]]
        jackpot_df.index.name = 'roll_number'
        return njackpot
    

    def combo(self)-> pd.DataFrame:
        """Displays how many times each different type of combination 
        landed in a dataframe. The multiindex is the combination and 
        the 'counts' column is how many times that combination landed. 

        Returns:
            pandas.DataFrame: Sorted DataFrame displaying how many times
            each combination was rolled with the combination as the index. 
        """
        self.combo_df = self.game._df.apply(lambda x: pd.Series(sorted(x)), 1)\
                                     .value_counts()\
                                     .to_frame('counts')
        return self.combo_df

    def face_counts_per_roll(self) -> pd.DataFrame:
        """Returns a data frame that shows how many times
        each face was appeared in a roll.

        Returns:
            pandas.DataFrame: DataFrame with faces as columns, roll_number as its index
            the number of times each face appeared in that roll as the elemets. 
        """
        face_counts_per_roll_df = self.game._df.apply(pd.Series.value_counts,axis=1).fillna(0)
        face_counts_per_roll_df.index.name = 'roll_number'
        return face_counts_per_roll_df