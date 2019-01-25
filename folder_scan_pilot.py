import sys
import os.path
import pandas as pd
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication


class MyWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        actbtn = QPushButton('Action', self)
        actbtn.clicked.connect(self.buttonClicked)
        actbtn.resize(actbtn.sizeHint())
        actbtn.move(70, 40)

        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(70, 80)

        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle('Scanning Folder')
        self.show()

    def buttonClicked(self):
        folder = '/TEMP'
        print('Scan folder : %s' % folder)

        df = pd.DataFrame(columns=('no', 'directory', 'd_link', 'file', 'f_link'))

        i = 1
        for path, dirs, files in os.walk(folder):
            if files:
                for filename in files:
                    df2 = pd.DataFrame(
                        data=[
                            [i, path, f'=HYPERLINK("{path}", "Dir 보기")',
                             filename, f'=HYPERLINK("{filename}", "File 보기")']
                        ], columns=('no', 'directory', 'd_link', 'file', 'f_link'))
                    df = df.append(df2, ignore_index=True)
                    i += 1

        df.to_excel('folder_scan.xlsx', sheet_name='Scan Result', index=False, header=True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    sys.exit(app.exec_())