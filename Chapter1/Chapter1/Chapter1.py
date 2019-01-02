import os
import pandas as pd
import requests

PATH = "C:/Users/Yin/Documents/DataPy"

r = requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')

with open(PATH + 'Iris.data', 'w') as f:
    f.write(r.text)

#print(os.listdir(PATH))    #打印 PATH 所在地址的目录
os.chdir(PATH)       #改变当前工作目录到指定的路径

df = pd.read_csv(PATH + 'iris.data', names=["sepal length", "sepal width", "petal length", "petal width", "class"])

#df.head() # 顶部
#df.ix[:4,:2]
#df.ix[:3, [x for x in df.columns if 'width' in x]]     #df.ix[:3, ['sepal width','petal width']]
#df['class'].unique()
#df[df['class']=='Iris-virginica'].reset_index(drop=True)
print()