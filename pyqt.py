import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel
import time
import threading

class ImageLabel(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(960, 540)
        self.setWindowTitle("Label Test")

        pix = QPixmap(r"D:\960x540_people0.jpg")
        self.label = QLabel(self)
        self.label.setPixmap(pix)
        self.label.setScaledContents(True)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.count = 0

    def update(self):
        path = "D:\960x540_people{0}.jpg".format(self.count)
        pix = QPixmap(path)
        self.label.setPixmap(pix)

        self.count += 1
        if(self.count == 10):
            self.count = 0

def job():
    global mainWidget

    time.sleep(1)
    while True:
        mainWidget.update()
        time.sleep(0.01)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWidget = ImageLabel()
    mainWidget.show()
    
    count = 0
    thread = threading.Thread(target = job)
    thread.start()

    sys.exit(app.exec_())
'''
    while True:
        path = "D:\960x540_people{0}.jpg".format(count)
        pix = QPixmap(r"path")
        mainWidget.update(pix)
        count += 1
        if(count == 10):
            count = 0
        time.sleep(0.1)
'''


