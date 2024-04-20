import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.loc[data['whoAmI']=='robot', 'whoAmI'] = '0'
data.loc[data['whoAmI']=='human', 'whoAmI'] = '1'
data.head(20)