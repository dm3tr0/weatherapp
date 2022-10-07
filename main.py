from PyQt5 import QtCore, QtGui, QtWidgets
import pyowm

class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(334, 173)
        MainWindow.setWindowIcon(QtGui.QIcon('icons/icon.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 310, 61))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 70, 311, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)

        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)

        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 130, 311, 31))
        self.pushButton.setObjectName("pushButton")
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Weather"))
        self.label.setText(_translate("MainWindow", "Напишіть назву свого міста"))
        self.label_2.setText(_translate("MainWindow", ""))
        self.label_3.setText(_translate("MainWindow", ""))
        self.label_4.setText(_translate('MainWindow', ""))
        self.pushButton.setText(_translate("MainWindow", "Кнопка"))
        self.pushButton.clicked.connect(self.weather)

    def weather(self):
        owm = pyowm.OWM('589502ea3775041ca1c364b589c0ce26')
        place = self.lineEdit.text()
        manager = owm.weather_manager()
        observation = manager.weather_at_place(place)
        weather = observation.weather
        t_1 = weather.temperature("celsius")
        t_2 = t_1['temp']
        status = weather.status
        icon_cloud = QtGui.QPixmap('icons/icon_cloudy')
        icon_clear = QtGui.QPixmap('icons/icon_clear')
        icon_rain = QtGui.QPixmap('icons/icon_rainy')
        self.label_2.setText(f'{round(t_2)} ℃')
        self.label_3.setText(status)
        if status == 'Clouds':
            ic2 = icon_cloud.scaledToHeight(40)
            ic2 = icon_cloud.scaledToWidth(50)
            self.label_4.setPixmap(ic2)
        elif status == 'Rain':
            ic2 = icon_rain.scaledToHeight(40)
            ic2 = icon_rain.scaledToWidth(50)
            self.label_4.setPixmap(ic2)
        elif status == 'Clear':
            ic2 = icon_clear.scaledToHeight(40)
            ic2 = icon_clear.scaledToWidth(50)
            self.label_4.setPixmap(ic2)
        else:
            self.label_4.setText('?')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())