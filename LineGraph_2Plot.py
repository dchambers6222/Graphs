import os
import sys
import tkinter as tk
from tkinter import filedialog
from pathlib import Path
from datetime import datetime
import PyQt5.QtGui as GUI
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import uic
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg


root = tk.Tk()
root.withdraw()

time = []
plot1 = []
plot2 = []

def PromptGetDateFile():
    print("\nHello, \nSelect the data you wish to View:\n")
    print("Data should be laid out:\nTime,Data1,Data2\nTime,Data1,Data2")
    filePath = filedialog.askopenfilename()
    filePathStr = str(filePath)
    print("Path:\n",filePathStr)
    return filePathStr

def GetGraphData():
    filePath = PromptGetDateFile()
    fileNameNoExt = Path(filePath).stem
    fileName = str(fileNameNoExt)
    print("\nShowing Graph from: "+fileName)
    
    file = open(filePath,'r')
    while True:
        line = file.readline()
        entries = line.split(',')
        if not line:
            break
        else:
            try:
                timeAdd = float(entries[0])
                time.append(timeAdd)
            except:
                timeAdd = float(0)
                time.append(timeAdd)

            try:
                plot1Add = float(entries[1])
                plot1.append(plot1Add)
            except:
                plot1Add = float(0)
                plot1.append(plot1Add)

            try:
                plot2Add = float(entries[2])
                plot2.append(plot2Add)
            except:
                plot2Add = float(0)
                plot2.append(plot2Add)

    return fileName

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        fileName = GetGraphData()
        title = "Data from "+ fileName
        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)
        self.graphWidget.setBackground('Black') 
        self.graphWidget.setTitle(title, color="w", size="15pt")
        self.graphWidget.setWindowTitle(title)
        self.graphWidget.setLabel('left', 'Y')
        self.graphWidget.setLabel('bottom', 'X')
        self.graphWidget.showGrid(x=True,y=True)
        self.graphWidget.addLegend()

        pen1 = pg.mkPen(color=(255, 0, 0), width=2, style=QtCore.Qt.DashLine)
        pen2 = pg.mkPen(color=(0, 170, 255), width=2)

        # plot data: x, y values
        line1 = self.graphWidget.plot(time, plot1, name="plot1", pen=pen1)
        line2 = self.graphWidget.plot(time, plot2, name="plot1", pen=pen2)

        view = pg.GraphicsView()
        layout = pg.GraphicsLayout()
        view.setCentralItem(layout)
        view.showMaximized()

    def btnClose_Click(self):
        sys.exit()

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()