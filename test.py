#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this program, we can press on a button with
a left mouse click or drag and drop the button
with the right mouse click.

author: Jan Bodnar
website: zetcode.com
last edited: January 2015
"""

from PyQt5.QtCore import QMimeData
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from image import *


class Button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)

    def mouseMoveEvent(self, e):

        if e.buttons() != Qt.RightButton:
            return

        mimeData = QMimeData()

        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos() - self.rect().topLeft())

        dropAction = drag.exec_(Qt.MoveAction)

    def mousePressEvent(self, e):

        QPushButton.mousePressEvent(self, e)
        print(e)
        if e.button() == Qt.LeftButton:
            print('press')


class Example(QWidget):
    def __init__(self):
        super().__init__()
        # self.fruits=None
        self.imageViewer = ImageViewer()
        self.initUI()

    def get_resize(self, e):
        print(e.size())

    def initUI(self):
        self.setAcceptDrops(True)
        self.setWindowTitle('Click or Move')
        self.setGeometry(100, 100, 800, 600)
        self.file_list = QListWidget()
        btn_del = QPushButton('删除')
        btn_add = QPushButton('添加')

        # self.setLayout(h_box)
        v_box = QVBoxLayout()
        v_box.addWidget(btn_del)
        v_box.addWidget(btn_add)

        v_box.addStretch(1)
        h_box = QHBoxLayout()
        h_box.addWidget(self.file_list)
        h_box.addWidget(self.imageViewer)
        h_box.addLayout(v_box)
        # v_box.addLayout(h_box)
        # self.fruits.show()
        self.setLayout(h_box)
        btn_del.clicked.connect(self.item_del)
        btn_add.clicked.connect(self.item_add)
        print(self.imageViewer.size())
        self.imageViewer.resizeEvent = self.get_resize
        self.file_list.itemClicked.connect(self.open_image)

    def open_image(self, item):
        self.imageViewer.open_image(item.text())

    def item_del(self):
        if QMessageBox.warning(self, u'确认', u'确定要删除?', QMessageBox.Ok | QMessageBox.Cancel) == QMessageBox.Ok:
            item_deleted = self.file_list.takeItem(self.file_list.currentRow())
            # 将读取的值设置为None
            item_deleted = None

    def item_add(self):
        fileNames, filetype = QFileDialog.getOpenFileNames(self,
                                                           "选取文件",
                                                           "C:/",
                                                           "All Files (*);;Text Files (*.txt)")  # 设置文件扩展名过滤,注意用双分号间隔
        for file in fileNames:
            self.file_list.addItem(file)

    # file_list.

    def dragEnterEvent(self, e):
        print('drap')
        e.accept()

    def dropEvent(self, e):
        print(e)
        help(e)
        position = e.pos()
        print(len(e.mimeData().text()))
        # print()
        for url in e.mimeData().urls():
            self.file_list.addItem(url.toLocalFile())
            # self.button.move(position)
            #
            # e.setDropAction(Qt.MoveAction)
            # e.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()
