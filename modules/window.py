from PyQt6.QtWidgets import QMainWindow, QFrame, QHBoxLayout, QPushButton, QLineEdit, QTextEdit,QComboBox
from .app import app
from PyQt6.QtCore import Qt



main_window = QMainWindow()

# получаем обьект экрана пользователя
primary_screen = app.primaryScreen()
# получаем размеры эрана пользователя
screen_size = primary_screen.size()
# получаем ширину экрана пользователя
screen_width = screen_size.width()
screen_height = screen_size.height()

WIDTH_WINDOW = 1024
HEIGHT_WINDOW = 800


# setGeometry - метод задает размеры и координаты окна
main_window.setGeometry(
    (screen_width // 2) - (WIDTH_WINDOW // 2), #координата х
    (screen_height // 2) - (HEIGHT_WINDOW // 2), # координата у
    WIDTH_WINDOW, # ширина
    HEIGHT_WINDOW # высота
)

frame1 = QFrame(main_window)
frame1.setStyleSheet("background-color:white;")
frame1.setFixedSize(1024,800)


layout1 = QHBoxLayout()
frame1.setLayout(layout1)

button = QPushButton(parent= frame1, text="pelmeni")
button.setStyleSheet("""
                    color:red;
                    border: 5px double blue;
                    background-color: pink;
                    font-weight: bold;
                    padding: 10px
""")
button.setFixedSize(200,100)

def cofee():
    button.setStyleSheet("""
                        color:black;
                        border: 5px double blue;
                        background-color: purple;
                        font-weight: bold;
                        padding: 10px
    """)
button.clicked.connect(
cofee)
layout1.addWidget(button)


but = QLineEdit(frame1)

but.setStyleSheet(""""
        border-radius:15px;
        background-color:green;
        color:blue;
        border:3px solid red;
        padding:10px
""")

but.setPlaceholderText("kuricha chi riba?")
layout1.addWidget(but)



def vivodim_text(text):
    print(text)


but.textChanged.connect(vivodim_text)


big_text = QTextEdit(frame1)
big_text.setStyleSheet("""
        border-radius:15px;
        background-color:green;
        color:blue;
        border:3px solid red;
        padding:10px
""")
layout1.addWidget(big_text)



def something():
    big_user_text = big_text.toPlainText()
    print("big text zone:", big_user_text)
    
big_text.textChanged.connect(something)
baran = QComboBox(frame1)


baran.addItems(["Anichka", "Leilusik", "Alisik"])


layout1.addWidget(baran)




