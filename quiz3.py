import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from nataliiii import Ui_MainWindow
from PyQt5.QtCore import Qt


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



        self.ui.pushButton.clicked.connect(lambda: self.show_page(self.ui.page))
        self.ui.pushButton_2.clicked.connect(lambda: self.show_page(self.ui.page_2))
        self.ui.pushButton_3.clicked.connect(lambda: self.show_page(self.ui.page_3))
        self.ui.pushButton_4.clicked.connect(lambda: self.show_page(self.ui.page_4))
        self.ui.pushButton_5.clicked.connect(lambda: self.show_page(self.ui.page_5))
        self.ui.pushButton_6.clicked.connect(lambda: self.show_page(self.ui.page_6))

        self.ui.checkBox_7.stateChanged.connect(self.college_info)
        self.ui.checkBox_3.stateChanged.connect(self.college_info)
        self.ui.checkBox_4.stateChanged.connect(self.college_info)
        self.ui.checkBox_5.stateChanged.connect(self.college_info)
        self.ui.checkBox_2.stateChanged.connect(self.college_info)
        self.ui.checkBox_6.stateChanged.connect(self.college_info)
        self.ui.page.setVisible(False)





    def show_page(self, pageToShow):
        for page in [self.ui.page, self.ui.page_2, self.ui.page_3,
                         self.ui.page_4, self.ui.page_5, self.ui.page_6]:
            page.setVisible(False)

        for label in [self.ui.label, self.ui.label_2, self.ui.label_3,
                              self.ui.label_4, self.ui.label_5, self.ui.label_6,
                              self.ui.label_7, self.ui.label_8, self.ui.label_9]:
            label.setVisible(False)
        for button in [self.ui.pushButton, self.ui.pushButton_2, self.ui.pushButton_3,
                       self.ui.pushButton_4, self.ui.pushButton_5, self.ui.pushButton_6]:
            button.setVisible(False)

        pageToShow.setVisible(True)

        self.ui.pushButton_8.clicked.connect(self.show_main)
        self.ui.pushButton_7.clicked.connect(self.show_main)
        self.ui.pushButton_9.clicked.connect(self.show_main)
        self.ui.pushButton_10.clicked.connect(self.show_main)
        self.ui.pushButton_11.clicked.connect(self.show_main)
        self.ui.pushButton_12.clicked.connect(self.show_main)
        self.ui.label_12.setText('Name: Caitlin Clark\nJersey Number: 22\nAge: 23\nPosition: Guard\nCollege: Iowa\nPoints: 19.0')
        self.ui.label_21.setText('Name: Sophie Cunningham\nJersey Number: 8\nAge: 28\nPosition: Guard\nCollege: Missouri\nPoints: 6.5')
        self.ui.label_15.setText('Name: Aliyah Boston\nJersey Number: 7\nAge: 23\nPosition: Forward\nCollege: South Carolina\nPoints: 16.8')
        self.ui.label_17.setText('Name: Lexie Hull\nJersey Number: 10\nAge: 25\nPosition: Guard\nCollege: Stanford\nPoints: 10.2')
        self.ui.label_24.setText('Name: Kelsey Mitchell\nJersey Number: 0\nAge: 29\nPosition: Guard\nCollege: Ohio State\nPoints: 16.3')
        self.ui.label_27.setText('Name: DeWanna Bonner\nJersey Number: 25\nAge: 37\nPosition: Forward\nCollege: Auburn\nPoints: 7.3')
    def show_main(self):
        for page in [self.ui.page, self.ui.page_2, self.ui.page_3,
                         self.ui.page_4, self.ui.page_5, self.ui.page_6]:
            page.setVisible(False)

        for label in [self.ui.label, self.ui.label_2, self.ui.label_3,
                              self.ui.label_4, self.ui.label_5, self.ui.label_6,
                              self.ui.label_7, self.ui.label_8, self.ui.label_9]:
            label.setVisible(True)
        for button in [self.ui.pushButton, self.ui.pushButton_2, self.ui.pushButton_3,
                       self.ui.pushButton_4, self.ui.pushButton_5, self.ui.pushButton_6]:
            button.setVisible(True)



    def college_info(self, state):
        if self.ui.checkBox_7.isChecked():
            self.ui.label_27.setText('DeWanna Bonner played for Auburn from\n'
'2005 to 2009. She was a three-time All-\n'
'SEC pick and led the team in scoring,\n'
'finishing with over 2,000 career pts.\n'
)
        elif self.ui.checkBox_3.isChecked():
            self.ui.label_15.setText('Aliyah Boston starred at South Carolina\n'
'from 2019 to 2023, winning a national\n'
'title in 2022 and several top awards.\n'
'She became one of the program’s best.\n'

)
        elif self.ui.checkBox_4.isChecked():
            self.ui.label_17.setText('Lexie Hull played for Stanford from\n'
'2018 to 2022. She helped win the 2021\n'
'national title and earned All-Pac-12\n'
'honors for strong defense and scoring.\n'
)
        elif self.ui.checkBox_5.isChecked():
            self.ui.label_21.setText('Sophie Cunningham played at Missouri\n'
'from 2015 to 2019. She was a key star\n'
'in the SEC, earning multiple honors\n'
'and scoring over 2,000 career points.\n'
)
        elif self.ui.checkBox_6.isChecked():
            self.ui.label_24.setText('Kelsey Mitchell starred at Ohio State\n'
'from 2014 to 2018. She became one of\n'
'the NCAA’s all-time scoring leaders,\n'
'finishing with 3,402 total points.\n'
)
        elif self.ui.checkBox_2.isChecked():
            self.ui.label_12.setText('Caitlin Clark played at Iowa from 2020\n'
'to 2024, leading the NCAA in scoring\n'
'multiple times and setting records for\n'
'assists and three-pointers made.\n'

)
        else:
            self.ui.label_12.setText(
                'Name: Caitlin Clark\nJersey Number: 22\nAge: 23\nPosition: Guard\nCollege: Iowa\nPoints: 19.0')
            self.ui.label_21.setText(
                'Name: Sophie Cunningham\nJersey Number: 8\nAge: 28\nPosition: Guard\nCollege: Missouri\nPoints: 6.5')
            self.ui.label_15.setText(
                'Name: Aliyah Boston\nJersey Number: 7\nAge: 23\nPosition: Forward\nCollege: South Carolina\nPoints: 16.8')
            self.ui.label_17.setText(
                'Name: Lexie Hull\nJersey Number: 10\nAge: 25\nPosition: Guard\nCollege: Stanford\nPoints: 10.2')
            self.ui.label_24.setText(
                'Name: Kelsey Mitchell\nJersey Number: 0\nAge: 29\nPosition: Guard\nCollege: Ohio State\nPoints: 16.3')
            self.ui.label_27.setText(
                'Name: DeWanna Bonner\nJersey Number: 25\nAge: 37\nPosition: Forward\nCollege: Auburn\nPoints: 7.3')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())