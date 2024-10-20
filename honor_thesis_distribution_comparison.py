# -*- coding: utf-8 -*-
"""Honor Thesis Distribution Comparison.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xzRitENejrkXF23yq8-975C9tqqhtyW4
"""

from scipy import stats
from scipy.stats import f_oneway
import pandas as pd
import numpy as np
from statsmodels.stats.multicomp import pairwise_tukeyhsd

group_1 = [4.3, 3.9, 2.45, 4.4, 4.6, 3.7, 3.95, 4.75, 3.2, 4.25]
group_2 = [4.65, 4.2, 3.95, 4.35, 4.25, 4.9, 4.5, 4.25, 4.35, 4.7]
group_3 = [4.1, 4.4, 3.75, 3.95, 4.6, 4.05, 3.8, 3.85, 3.5, 4.35]

df = pd.DataFrame(columns = ['system', 'mean', 'variance'])
df.loc[0] = ['score-based', np.mean(group_1), np.std(group_1)]
df.loc[1] = ['content-based', np.mean(group_2), np.std(group_2)]
df.loc[2] = ['collaborative', np.mean(group_3), np.std(group_3)]
df

stats.kruskal(group_1, group_2, group_3)

f_oneway(group_1, group_2, group_3)

df = pd.DataFrame({'score': [4.3, 3.9, 2.45, 4.4, 4.6, 3.7, 3.95, 4.75, 3.2, 4.25,
                             4.65, 4.2, 3.95, 4.35, 4.25, 4.9, 4.5, 4.25, 4.35, 4.7,
                             4.1, 4.4, 3.75, 3.95, 4.6, 4.05, 3.8, 3.85, 3.5, 4.35],
                   'group': np.repeat(['group_1', 'group_2', 'group_3'], repeats=10)})

tukey_result = pairwise_tukeyhsd(endog=df['score'], groups=df['group'], alpha=0.1)

print(tukey_result)

import matplotlib.pyplot as plt
  
data_wide = pd.DataFrame({'group_1': group_1, 'group_2': group_2, 'group_3': group_3})
data_wide.plot.density(figsize = (7, 7),
                       linewidth = 4)
  
plt.xlabel("score")
