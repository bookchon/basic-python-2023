# 푸시버튼
import sys
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton('&Button1', self)
        btn1.setCheckable(True)
        btn1.toggle()

        btn2 = QPushButton(self)
        btn2.setText('Button&2')

        btn3 = QPushButton('Button3', self)
        btn3.setEnabled(False)


        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)

        self.setLayout(vbox)

        # 필수 설정
        self.setWindowTitle('절대 배치')
        self.setGeometry(300, 300, 300, 300)
        self.show()


if __name__ == '__main__':
    app =  QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())