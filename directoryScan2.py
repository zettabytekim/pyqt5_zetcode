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
            df = [path, filename]
            i = I + 1

df.head()

exit(0)