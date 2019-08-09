# -*- coding: utf-8 -*-
"""

import pandas as pd

phy = list(map(int,input().split()))
his = list(map(int,input().split()))

x=pd.Series(phy)
y=pd.Series(his)

r=x.cov(y)/(x.std()*y.std())

beta1 = (r*y.std())/x.std()
print("Slope :",round(beta1,3))
