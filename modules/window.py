# QMainWindow класс для создания главного окна
from PyQt6.QtWidgets import QMainWindow, QFrame, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel
from .app import app



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

frame1 = QFrame(parent= main_window) 
# задаем стили в кавычках в стиле название стиля: значение
# border-radius: 20px - скругление углов на 20 пикселей
frame1.setStyleSheet("background-color: blue; border-radius: 5px")
frame1.setFixedSize(1024,800)

# QHBoxLayout - класс для создания леяута горизонтального
# QVBoxLayout - класс для создания леяута вертикального
# QGridLayout - класс для создания леяута сетки



frame1_layout = QGridLayout()
# название_фрейма.setLayout(леяут который прекрепояем)
# setLayout - устанавливает леяут
frame1.setLayout(frame1_layout)


kolya_frame = QFrame(parent=frame1)
kolya_frame.setStyleSheet("background-color: black; border-radius: 5px")
kolya_frame.setFixedSize(100,200)
frame1_layout.addWidget(kolya_frame, 1, 3)

frame10 =QFrame(frame1)
frame10.setStyleSheet("background-color:green")
frame10.setFixedSize(200,200)
frame1_layout.addWidget(frame10, 1, 4)

anya_frame = QFrame(frame1)
anya_frame.setStyleSheet("background-color: pink")
anya_frame.setFixedSize(150,200)
frame1_layout.addWidget(anya_frame, 5, 7)


# назване_лкяута.addWidget(фрейм_который добавляем в схему размещения)
# addWidget - добавляет виджет в леяут

# Назар, создать фрейм с стилями и размерами 
nazar_frame1 = QFrame(frame1)
nazar_frame1.setStyleSheet("background-color:pink; border-radius: 5px")
nazar_frame1.setFixedSize(100,200)
frame1_layout.addWidget(nazar_frame1, 2, 2)

# когда размещение сетка, указываем в метод addWidget название фрема, рядок, столбец

# QLabel - класс для создания текста
label_1 = QLabel(
    text="Hello world", # текст для отображения
    parent=frame1 # в каком фрейме разместится текст
)





