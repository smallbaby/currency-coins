# -*- coding: utf-8 -*-
# pandas test

import pandas as pd
import numpy as np
df = pd.DataFrame(pd.read_csv('../huobi/data/xrpbtc-m3-huobi.csv',header=0))
print(df.info())
print(df.dtypes)
#print(df.columns)
print(df.tail)
df.sort_values(by=['timestamp'])

# 数据提取
# loc,iloc和ix，
# loc函数按标签值进行提取，
# iloc按位置进行提取，
# ix可以同时按标签和位置进行提取。
print(pd.Index)
pd.merge