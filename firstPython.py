#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %%
from sklearn import datasets 
# %%
bank_df = pd.read_csv("bank-full.csv")
# %%
bank_df.head()
# %%
bank_df.dtypes
# %%
bank_df.shape
# %%
