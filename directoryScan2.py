import os.path
import pandas as pd

folder = os.getcwd()

print('Current folder : %s' % folder)

df = pd.DataFrame(columns=('directory', 'file'))

i = 0
for path, dirs, files in os.walk(folder):
    #print('\nFolder: ', path)

    if files:
        for filename in files:
            #print(' Files: ', os.path.join(path, filename))
            df2 = pd.DataFrame(data=[[path, filename]], columns=('directory', 'file'))
            df = df.append(df2, ignore_index=True)

print(df.head())