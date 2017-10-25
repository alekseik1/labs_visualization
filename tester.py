import numpy as np
import random as rd
import pandas as pd

frame = pd.DataFrame({'s': range(0, 100)})
frame['t'] = frame['s'].apply(lambda x: x**2*np.sin(np.exp(x*2/30+5)) + rd.randint(1, 100)/1000)

frame.to_csv("sample2.csv")
