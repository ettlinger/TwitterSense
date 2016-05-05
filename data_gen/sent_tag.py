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
sentf=pd.DataFrame(sent)
sentf.columns = ['sent', 'zip', 'st']
sentf[['sent']] = sentf[['sent']].astype(float)

