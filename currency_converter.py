from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit, QComboBox
from PyQt6.QtCore import Qt
import requests
from bs4 import BeautifulSoup

def currency_calculator(in_currency, out_currency):
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1"
    r = requests.get(url).text
    soup = BeautifulSoup(r, "html.parser")
    soup1 = soup.find("span", class_="ccOutputRslt").get_text()
    rate = float(soup1[:-4])
    return rate

def currency_converter():
    input_text=float(text.text())

    in_cur=in_combo.currentText()
    target_cur=target_combo.currentText()

    rate=currency_calculator(in_cur, target_cur)

    output=round(input_text * rate, 2)
    results= f"{input_text} {in_cur} is {output} {target_cur}"
    output_label.setText(str(results))

app=QApplication([])
window=QWidget()
window.setWindowTitle('Currency Converter')

layout= QVBoxLayout()
layout1=QHBoxLayout()
layout.addLayout(layout1)

output_label=QLabel('')
layout.addWidget(output_label)

layout2=QVBoxLayout()
layout1.addLayout(layout2)

layout3=QVBoxLayout()
layout1.addLayout(layout3)

in_combo=QComboBox()
currencies=['USD', 'EUR', 'INR', 'CZK']
in_combo.addItems(currencies)
layout2.addWidget(in_combo)

target_combo=QComboBox()
target_combo.addItems(currencies)
layout2.addWidget(target_combo)

text=QLineEdit()
layout3.addWidget(text)

btn=QPushButton('Convert')
layout3.addWidget(btn)
btn.clicked.connect(currency_converter)

window.setLayout(layout)

window.show()
app.exec()