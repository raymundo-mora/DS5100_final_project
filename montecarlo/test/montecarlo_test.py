# Class: DS5100
# Assignment: Final Project
# Author: Raymundo Mora



# Import packages
import unittest
import numpy as np
from random import randint
from montecarlo.montecarlo import *


class DieTestSuite(unittest.TestCase):
    

    # Test Die.change_w()
    def test_1_die_change_w(self):
        
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

        # Instantiate Die object
        die1 = Die(['jack','queen','king','ace'])

        nrolls = randint(1,50)
        outcomes = die1.roll(nrolls=nrolls)

        self.assertEqual(len(outcomes),nrolls)

    def test_3_die_show(self):

        # Instantiate Die object
        faces = ['jack','queen','king','ace']
        die1 = Die(faces)
        df = die1.show()
        self.assertEqual(df.shape,(len(faces),2))


    def test_4_game_play(self):


        # Instantiate Game object 
        die1 = Die(['jack','queen','king','ace'])
        die2 = Die(['jack','queen','king','ace'])
        game1 = Game([die1,die2])

        nrolls = randint(1,50)
        ndie = len(game1.die_list)
        game1.play(nrolls)

        self.assertEqual(game1._df.shape, (nrolls,ndie))

    def test_5_game_show_wide(self):

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
