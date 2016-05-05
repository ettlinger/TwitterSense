

import pandas as pd
import re
import sys
sent=[]
inc=[]
f = open("t2.txt", 'r')
for line in f:
    row = line.strip().split(',')
    sent.append(row)
f.close()
g = open("zincome.csv", 'r')
for i in g:
    irow = i.strip().split(',')
    inc.append(irow)
g.close()

sentf=pd.DataFrame(sent)
sentf.columns = ['sent', 'zip', 'st']
sentf[['sent']] = sentf[['sent']].astype(float)

incf=pd.DataFrame(inc)
incf.columns = ['st', 'z', 'income', 'zip']
incf[['income']] = incf[['income']].astype(float)

merg = pd.merge(incf, sentf, on ='zip')
merf = merg.groupby('zip').mean()

merg.plot()
