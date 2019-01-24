import os.path
import pandas as pd

folder = os.getcwd()

print('Current folder : %s' % folder)

df = pd.DataFrame(columns=('directory', 'file', 'full_name'))

i = 0
for path, dirs, files in os.walk('/Test'):
    print('\nFolder: ', path)

    if files:
        for filename in files:
 #           print(' Files: ', os.path.join(path, filename))
 #           print(' Files: ', filename)
            df2 = pd.DataFrame([path, filename], columns=('directory', 'file', 'full_name'))
            df.append(df2, ignore_index=True)
df.head()

exit(0)