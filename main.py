from modules import app, main_window

def main():
    try:
        # show - показывает (запускает) обьект главного окна
        main_window.show()
        # exec - запускает наш обьект приложения (двигатель) 
        # он всегда после метода шоу
        app.exec()
    except Exception as error:
        print(error)

if __name__ == "__main__":
    main()
