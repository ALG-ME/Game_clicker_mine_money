import tkinter as tk
from tkinter import ttk
import time

# Глобальные переменные
ruble_count = 0
start_time = None

# Функция для обновления счета рублей
def update_ruble_count(label):
    label.config(text=f"Рублей: {ruble_count}")

# Функция для обработки нажатия на кнопку "Клик"
def click_button():
    global ruble_count
    ruble_count += 1
    update_ruble_count(ruble_label)

# Функция для обработки нажатия на кнопку "Сброс"
def reset_button():
    global ruble_count, start_time
    ruble_count = 0
    start_time = time.time()
    update_ruble_count(ruble_label)

# Создание главного окна
window = tk.Tk()
window.title("Кликер")
window.geometry("300x200")

# Настройка стиля шрифта для заголовка
title_font = ("Helvetica", 24, "bold")
title_label = tk.Label(window, text="Игра Кликер", font=title_font)
title_label.pack()

# Создание метки для счета рублей
ruble_label = tk.Label(window, text=f"Рублей: {ruble_count}", font=("Helvetica", 18))
ruble_label.pack()

# Настройка стиля для кнопок
button_style = ttk.Style()
button_style.configure("TButton", font=("Helvetica", 14), padding=5, background="#4CAF50", foreground="white")

# Создание кнопки "Клик"
click_button = ttk.Button(window, text="Клик", command=click_button, style="TButton")
click_button.pack()

# Создание кнопки "Сброс"
reset_button = ttk.Button(window, text="Сброс", command=reset_button, style="TButton")
reset_button.pack()

# Запуск таймера
start_time = time.time()

# Запуск главного цикла
window.mainloop()
