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

x = []
plot1 = []
plot2 = []

def PromptGetDateFile():
    print("\nHello, \nSelect the data you wish to View:\n")
    print("Data should be laid out:\nX,Data1\nX,Data1")
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
                x.append(timeAdd)
            except:
                timeAdd = float(0)
                x.append(timeAdd)

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


        # creating a pyqtgraph plot window
        window = pg.plot()
        
        # setting window geometry
        # left = 100, top = 100
        # width = 600, height = 500
        window.setGeometry(100, 100, 600, 500)
        
        # setting window title to plot window
        window.setWindowTitle(title)
        
        # create pyqt5graph bar graph item
        # with width = 0.6
        # with bar colors = green
        bargraph = pg.BarGraphItem(x = x, height = plot1, width = 0.6, brush ='g')
        
        # add item to plot window
        # adding bargraph item to the window
        window.addItem(bargraph)


    def btnClose_Click(self):
        sys.exit()

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()