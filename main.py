from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow
from main_window import MainWindow
import sys 

app = QApplication(sys.argv)

# Создаём виджет Qt — окно.
window = MainWindow()
window.show()  # Важно: окно по умолчанию скрыто.

# Запускаем цикл событий.
app.exec()