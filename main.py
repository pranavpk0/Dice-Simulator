from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap 
from ui import Ui_MainWindow
from random import choice


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.start)

        self.show()

    def start(self):
        q = ["1", "2", "3", "4", "5", "6"]
        num = choice(q)
        print(num)
        if num == "1":
            self.label.setPixmap(QPixmap("res/1.png"))
        if num == "2":
            self.label.setPixmap(QPixmap("res/2.png"))
        if num == "3":
            self.label.setPixmap(QPixmap("res/3.png"))
        if num == "4":
            self.label.setPixmap(QPixmap("res/4.png"))
        if num == "5":
            self.label.setPixmap(QPixmap("res/5.png"))
        if num == "6":
            self.label.setPixmap(QPixmap("res/6.png"))

        self.label_2.setText("The Number is "+num)


if __name__ == '__main__':
    app = QApplication([])

    window = MainWindow()
    app.exec_()
