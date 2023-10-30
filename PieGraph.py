import sys
import tkinter as tk
from tkinter import filedialog
from pathlib import Path
from datetime import datetime
import PyQt5.QtGui as GUI
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import uic
from PyQt5 import QtCharts
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QPen
from PySide6.QtWidgets import QMainWindow, QApplication

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

class MyChart(QtChart.QChart):

    def __init__(self, datas, parent=None):
        super(MyChart, self).__init__(parent)
        self._datas = datas

        self.legend().hide()
        self.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

        self.outer = QtCharts.QPieSeries()
        self.inner = QtCharts.QPieSeries()
        self.outer.setHoleSize(0.35)
        self.inner.setPieSize(0.35)
        self.inner.setHoleSize(0.3)

        self.set_outer_series()
        self.set_inner_series()

        self.addSeries(self.outer)
        self.addSeries(self.inner)

    def set_outer_series(self):
        slices = list()
        for data in self._datas:
            slice_ = QtCharts.QPieSlice(data.name, data.value)
            slice_.setLabelVisible()
            slice_.setColor(data.primary_color)
            slice_.setLabelBrush(data.primary_color)

            slices.append(slice_)
            self.outer.append(slice_)

        # label styling
        for slice_ in slices:
            color = 'black'
            if slice_.percentage() > 0.1:
                slice_.setLabelPosition(QtCharts.QPieSlice.LabelInsideHorizontal)
                color = 'white'

            label = "<p align='center' style='color:{}'>{}<br>{}%</p>".format(
                color,
                slice_.label(),
                round(slice_.percentage()*100, 2)
                )
            slice_.setLabel(label)

    def set_inner_series(self):
        for data in self._datas:
            slice_ = self.inner.append(data.name, data.value)
            slice_.setColor(data.secondary_color)
            slice_.setBorderColor(data.secondary_color)