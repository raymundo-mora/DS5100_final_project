# %% 
import numpy as np
import pandas as pd
import random
# %% 
class Die:

    # Initializer
    def __init__(self,faces):
        w = list(np.full(len(faces),1.0))
        
        self._die_df = pd.DataFrame({'face':faces,
                                  'weight':w
                                  })
        return None
    # Method 1 
    def change_w(self,face,weight):
        i = self._die_df[self._die_df['face'] == face].index[0]
        self._die_df.loc[i,'weight'] = weight
        return None
    # Method 2 
    def roll(self,nrolls=1):
        outcomes = random.choices(self._die_df.face,weights=self._die_df.weight,k=nrolls)
        return outcomes
    
    # Method 3 
    def show(self):
        return self._die_df
# %% 

# %% 
class Game: 

    
    def __init__(self,die_list: list):
        l1 = []
        for die in die_list:
            l1.append(list(die._die_df.face.sort_values()))
        assert l1.count(l1[0]) == len(l1), 'EEERRRROOOOR'


        self.die_list = die_list

    # Method 1 
    def play(self,nrolls):
        self._df = pd.DataFrame()
        count = 0 
        for die in self.die_list:
            outcome = die.roll(nrolls)
            self._df[count] = outcome
            count += 1 
        return None

    # Method 2 
    def show(self,form='wide'):
        form = form.lower()
        if form == 'wide':
            return self._df
        elif form == 'narrow':
            self._df = self._df.stack()
            self._df.index.names = ['roll','die']
            return self._df


# %%
class Analyzer:



    def __init__(self,game):
        self.game = game


    def jackpot(self):
        s = self.game._df.eq(self.game._df.iloc[:, 0], axis=0).all(1)
        njackpot = s.sum()
        jackpot_df = self.game._df.loc[np.where(s==True)[0]]
        jackpot_df.index.name = 'roll_number'
        return njackpot
    

    def combo(self):
        self.combo_df = self.game._df.apply(lambda x: pd.Series(sorted(x)), 1)\
                                     .value_counts()\
                                     .to_frame('counts')
        return self.combo_df

    def face_counts_per_roll(self):
        face_counts_per_roll_df = self.game._df.apply(pd.Series.value_counts,axis=1).fillna(0)
        face_counts_per_roll_df.index.name = 'roll'
        return face_counts_per_roll_df

