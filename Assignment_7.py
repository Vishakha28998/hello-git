import numpy as np
import pandas as pd
#question no1:
data = {'Name':['Tom','jack','steve','ricky'],'Age':[28,22,29,42],'Email':['tom98@gmail.com','jack119@gmail.com','stv900@facebook.com','ricky554@yahoo.com'],'pno':[980765,907854,789643,755543]}
df= pd.DataFrame(data)
#adding friend's info
df.loc[4]=['jake',22,'jake44@gamil.com',980659]
df.loc[5]=['Ashley',25,'ash6565@gamil.com',673453]
df.loc[6]=['lilly',30,'lil1921@gmail.com',623145]

print(df)
