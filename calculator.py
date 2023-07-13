from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QIcon
from os import system
system("cls")

app = QApplication([])
window = QWidget()
window.setGeometry(0, 0, 720, 920)
window.setWindowTitle("Calculator")
window.setWindowIcon(QIcon("C:\\Users\\HP\\Desktop\\calculator\\calculator.png"))


start = "0"
start_label = QLabel(start, window)
start_label.setGeometry(5, 25, 710, 150)
start_label.setStyleSheet("""
    color: white;
    border-radius: 15%;
    background-color: #9c94ce;
    font-size: 70px;
""")

def func_AC(label: QLabel):
    start_label.setText("0")

btn_AC = QPushButton("AC", window)
btn_AC.setGeometry(5, 215, 170, 135)
btn_AC.setStyleSheet("""
    color : #d75c4c;
    font-size: 35px;
    border-radius: 15%;
    background-color: black;
""")
btn_AC.clicked.connect(lambda: func_AC(start_label))


def func_digit(start_label: QLabel, digit: str):
    if start_label.text() != "0":
        start_label.setText(start_label.text() + digit)
    else: start_label.setText(digit)

btn_seven = QPushButton("7", window)
btn_seven.setGeometry(5, 355, 170, 135)
btn_seven.setStyleSheet("""
    color : #d75c4c;
    font-size: 35px;
    border-radius: 15%;
    background-color: black;
""")
btn_seven.clicked.connect(lambda: func_digit(start_label, "7"))

btn_four = QPushButton("4", window)
btn_four.setGeometry(5, 495, 170, 135)
btn_four.setStyleSheet("""
    color : #d75c4c;
    font-size: 35px;
    border-radius: 15%;
    background-color: black;
""")
btn_four.clicked.connect(lambda: func_digit(start_label, "4"))

btn_one = QPushButton("1", window)
btn_one.setGeometry(5, 635, 170, 135)
btn_one.setStyleSheet("""
    color : #d75c4c;
    font-size: 35px;
    border-radius: 15%;
    background-color: black;
""")
btn_one.clicked.connect(lambda: func_digit(start_label, "1"))

def func_plus_minus(start_label: QLabel):
    lst = list(start_label.text())
    if start_label.text() != "0":
        if lst[0] == "-":
            start_label.setText("".join(lst[1:]))
        else:
            start_label.setText("-" + "".join(lst))

btn_plus_minus = QPushButton("+/-", window)
btn_plus_minus.setGeometry(5, 775, 170, 135)
btn_plus_minus.setStyleSheet("""
    color : #d75c4c;
    font-size: 35px;
    border-radius: 15%;
    background-color: black;
""")
btn_plus_minus.clicked.connect(lambda: func_plus_minus(start_label))

def func_remove(start_label: QLabel):
    lst = list(start_label.text())
    if start_label.text() != "0":
        if len(start_label.text()) > 1:
            start_label.setText("".join(lst[:len(lst)-1]))
        else:
            start_label.setText("0")

btn_remove = QPushButton("<=", window)
btn_remove.setGeometry(180, 215, 170, 135)
btn_remove.setStyleSheet("""
    color : #d75c4c;
    font-size: 35px;
    border-radius: 15%;
    background-color: black;
""")
btn_remove.clicked.connect(lambda : func_remove(start_label))

btn_eight = QPushButton("8", window)
btn_eight.setGeometry(180, 355, 170, 135)
btn_eight.setStyleSheet("""
    color : #d75c4c;
    font-size: 35px;
    border-radius: 15%;
    background-color: black;
""")
btn_eight.clicked.connect(lambda: func_digit(start_label, "8"))

btn_five = QPushButton("5", window)
btn_five.setGeometry(180, 495, 170, 135)
btn_five.setStyleSheet("""
    color : #d75c4c;
    font-size: 35px;
    border-radius: 15%;
    background-color: black;
""")
btn_five.clicked.connect(lambda: func_digit(start_label, "5"))

btn_two = QPushButton("2", window)
btn_two.setGeometry(180, 635, 170, 135)
btn_two.setStyleSheet("""
    color : #d75c4c;
    font-size: 35px;
    border-radius: 15%;
    background-color: black;
""")
btn_two.clicked.connect(lambda: func_digit(start_label, "2"))

btn_zero = QPushButton("0", window)
btn_zero.setGeometry(180, 775, 170, 135)
btn_zero.setStyleSheet("""
    color : #d75c4c;
    font-size: 35px;
    border-radius: 15%;
    background-color: black;
""")
btn_zero.clicked.connect(lambda: func_digit(start_label, "0"))

def func_order(start_label: QLabel, sign: str):
    start_label.setText(start_label.text() + sign)

btn_percent = QPushButton("%", window)
btn_percent.setGeometry(355, 215, 170, 135)
btn_percent.setStyleSheet("""
    color : #d75c4c;
    font-size: 35px;
    border-radius: 15%;
    background-color: black;
""")
btn_percent.clicked.connect(lambda: func_order(start_label, "%"))

btn_nine = QPushButton("9", window)
btn_nine.setGeometry(355, 355, 170, 135)
btn_nine.setStyleSheet("""
    color : #d75c4c;
    font-size: 35px;
    border-radius: 15%;
    background-color: black;
""")
btn_nine.clicked.connect(lambda: func_digit(start_label, "9"))

btn_six = QPushButton("6", window)
btn_six.setGeometry(355, 495, 170, 135)
btn_six.setStyleSheet("""
    color : #d75c4c;
    font-size: 35px;
    border-radius: 15%;
    background-color: black;
""")
btn_six.clicked.connect(lambda: func_digit(start_label, "6"))

btn_three = QPushButton("3", window)
btn_three.setGeometry(355, 635, 170, 135)
btn_three.setStyleSheet("""
    color : #d75c4c;
    font-size: 35px;
    border-radius: 15%;
    background-color: black;
""")
btn_three.clicked.connect(lambda: func_digit(start_label, "3"))

def func_point(start_label):
    if start_label.text() != "0":
        start_label.setText(start_label.text() + ".")

btn_point = QPushButton(".", window)
btn_point.setGeometry(355, 775, 170, 135)
btn_point.setStyleSheet("""
    color : #d75c4c;
    font-size: 35px;
    border-radius: 15%;
    background-color: black;
""")
btn_point.clicked.connect(lambda: func_point(start_label))

btn_divide = QPushButton("/", window)
btn_divide.setGeometry(530, 215, 170, 135)
btn_divide.setStyleSheet("""
    color : #d75c4c;
    font-size: 35px;
    border-radius: 65%;
    background-color: black;
""")
btn_divide.clicked.connect(lambda: func_order(start_label, "/"))

btn_multiple = QPushButton("*", window)
btn_multiple.setGeometry(530, 355, 170, 135)
btn_multiple.setStyleSheet("""
    color : #d75c4c;
    font-size: 35px;
    border-radius: 65%;
    background-color: black;
""")
btn_multiple.clicked.connect(lambda: func_order(start_label, "*"))

btn_minus = QPushButton("-", window)
btn_minus.setGeometry(530, 495, 170, 135)
btn_minus.setStyleSheet("""
    color : #d75c4c;
    font-size: 35px;
    border-radius: 65%;
    background-color: black;
""")
btn_minus.clicked.connect(lambda: func_order(start_label, "-"))

btn_plus = QPushButton("+", window)
btn_plus.setGeometry(530, 635, 170, 135)
btn_plus.setStyleSheet("""
    color : #d75c4c;
    font-size: 35px;
    border-radius: 65%;
    background-color: black;
""")
btn_plus.clicked.connect(lambda: func_order(start_label, "+"))

def func_equal(start_label: QLabel):
    start_label.setText(str(eval(start_label.text())))
    # lst = list(start_label.text())
    # if lst[len(lst)-1] != "-" and lst[len(lst)-1] != "+" and lst[len(lst)-1] != "*" and lst[len(lst)-1] != "/" and lst[len(lst)-1] != "%":
    #     result = list()
    #     sum = 0
    #     number = str()
        
    #     for s in lst:
    #         if s != '*' and s != '-' and s != '+' and s != '/' and s != '%' and s != "!":
    #             number += s
    #         result.append(number)
    #         number = str()

btn_equal = QPushButton("=", window)
btn_equal.setGeometry(530, 775, 170, 135)
btn_equal.setStyleSheet("""
    color : #d75c4c;
    font-size: 35px;
    border-radius: 65%;
    background-color: black;
""")
btn_equal.clicked.connect(lambda: func_equal(start_label))

window.show()
app.exec_()