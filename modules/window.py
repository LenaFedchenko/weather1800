# QMainWindow класс для создания главного окна
from PyQt6.QtWidgets import QMainWindow
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
