'''
Author: RaymundoMora 
@linkedin: https://www.linkedin.com/in/raymundo-mora/ 
@github: https://github.com/raymundo-mora 
@url: 

Description: This file contains tests for the classes created for the 
Monte Carlo Simulator. This is for the final project of DS5100.

Created: 2022-07-08
Modified 2022-07-15
''' 
# Import packages
import unittest
import numpy as np
from random import randint
from montecarlo.montecarlo import *


class montecarloTestSuite(unittest.TestCase):
    """Provides unit tests for the montecarlo package. 

    """
    

    # Test Die.change_w()
    def test_1_die_change_w(self):
        """Checks if the face in the dataframe was updated with the correct 
        new weight. 
        """
        
        # Instantiate Die object
        die1 = Die(['jack','queen','king','ace'])

        # Use `change_w` method to change the weight of the face 'queen' 
        new_weight = 3.2
        die1.change_w('queen',new_weight)

    
        queen_index = np.where(die1._die_df['face'] == 'queen')[0][0]
        queen_weight = die1._die_df['weight'][queen_index]
        self.assertEqual(queen_weight,new_weight)
        
    # Test Die.roll()
    def test_2_die_roll(self):
        """Checks that the number of outcomes reported 
        is equal to nrolls passed. 
        """

        # Instantiate Die object
        die1 = Die(['jack','queen','king','ace'])

        nrolls = randint(1,50)
        outcomes = die1.roll(nrolls=nrolls)

        self.assertEqual(len(outcomes),nrolls)

    def test_3_die_show(self):
        """Checks that the shape of the data frame returned
        is as expected. 
        """

        # Instantiate Die object
        faces = ['jack','queen','king','ace']
        die1 = Die(faces)
        df = die1.show()
        self.assertEqual(df.shape,(len(faces),2))


    def test_4_game_play(self):
        """Checks that the shape of the data frame returned
        is as expected.
        """


        # Instantiate Game object 
        die1 = Die(['jack','queen','king','ace'])
        die2 = Die(['jack','queen','king','ace'])
        game1 = Game([die1,die2])

        nrolls = randint(1,50)
        ndie = len(game1.die_list)
        game1.play(nrolls)

        self.assertEqual(game1._df.shape, (nrolls,ndie))

    def test_5_game_show_wide(self):
        """Checks that the shape of the data frame returned
        is as expected.
        """

        # Instantiate Game object 
        die1 = Die(['jack','queen','king','ace'])
        die2 = Die(['jack','queen','king','ace'])
        die3 = Die(['jack','queen','king','ace'])
        game1 = Game([die1,die2,die3])

        nrolls = randint(1,50)
        ndie = len(game1.die_list)
        game1.play(nrolls)
        self.assertEqual(game1.show().shape, (nrolls,ndie))
    
    def test_6_game_show_narrow(self):
        """Checks that the shape of the data frame returned 
        is as expected.
        """

        # Instantiate Game object 
        die1 = Die(['jack','queen','king','ace'])
        die2 = Die(['jack','queen','king','ace'])
        die3 = Die(['jack','queen','king','ace'])
        game1 = Game([die1,die2,die3])

        nrolls = randint(1,50)
        ndie = len(game1.die_list)
        game1.play(nrolls)
        self.assertEqual(game1.show('narrow').shape, (nrolls*ndie,))

    def test_7_analyzer_jackpot(self):
        """Asserts that the number of jackpots returned
        is correct by calculating it in the test. 
        """
        # Instantiate Analyzer object 
        die1 = Die(['jack','queen','king','ace'])
        die2 = Die(['jack','queen','king','ace'])
        die3 = Die(['jack','queen','king','ace'])
        game1 = Game([die1,die2,die3])
        game1.play(300)
        analyzer1 = Analyzer(game1)
        njackpots = game1._df.eq(game1._df.iloc[:, 0], axis=0).all(axis=1).sum()
        self.assertEqual(analyzer1.jackpot(),njackpots)


    def test_8_analyzer_combo(self):
        """Checks if the sum of the numbers of each
        combination is equal to nrolls. This makes 
        sure nothing was counted twice or missed. 
        """

        # Instantiate Analyzer object 
        die1 = Die(['jack','queen','king','ace'])
        die2 = Die(['jack','queen','king','ace'])
        die3 = Die(['jack','queen','king','ace'])
        game1 = Game([die1,die2,die3])
        nrolls = randint(1,300)
        game1.play(nrolls)
        analyzer1 = Analyzer(game1)

        sum_combos = analyzer1.combo().counts.sum()

        self.assertEqual(nrolls,sum_combos)


    def test_9_analyzer_face_counts_per_roll(self):
        """Makes sure that the sum of the number each
        face was rolled is equal to the total number 
        of rolls in the game. 
        """

        # Instantiate Analyzer object 
        die1 = Die(['jack','queen','king','ace'])
        die2 = Die(['jack','queen','king','ace'])
        die3 = Die(['jack','queen','king','ace'])
        game1 = Game([die1,die2,die3])
        nrolls = randint(1,300)
        game1.play(nrolls)
        analyzer1 = Analyzer(game1)
        df = analyzer1.face_counts_per_roll()


        nfaces = len(game1.die_list) * nrolls
        face_count = sum([df[col].sum() for col in df.columns])
        self.assertEqual(nfaces,face_count)
if __name__ == '__main__':
    unittest.main(verbosity=3)
