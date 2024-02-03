import tkinter as tk
from tkinter import END
from random import randint

class TemperatureApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Метереологічні дослідження")
        self.master.geometry("350x230")  # Зменшено ширину вікна в 3 рази

        # Заповнення списку температур випадковими значеннями
        self.temperatures = [randint(-5, 8) for _ in range(7)]

        # Створення трьох колонок
        self.temperature_label = tk.Label(master, text="Температура")
        self.temperature_label.grid(row=0, column=0, padx=2, pady=10, sticky="w")

        self.warm_days_label = tk.Label(master, text="Теплі дні")
        self.warm_days_label.grid(row=0, column=1, padx=2, pady=10, sticky="w")

        self.calculate_button = tk.Button(master, text="Обчислити", command=self.calculate_temperatures)
        self.calculate_button.grid(row=0, column=2, pady=10, padx=2, sticky="w")

        self.temperature_listbox = tk.Listbox(master)
        self.temperature_listbox.grid(row=1, column=0, padx=2, pady=10)

        self.warm_days_listbox = tk.Listbox(master)
        self.warm_days_listbox.grid(row=1, column=1, padx=2, pady=10)

        # Інформація про температури
        self.max_label = tk.Label(master, text="max=")
        self.max_label.grid(row=1, column=2, padx=2, pady=2, sticky="w")

        self.min_label = tk.Label(master, text="min=")
        self.min_label.grid(row=2, column=2, padx=2, pady=2, sticky="w")

        self.warm_days_count_label = tk.Label(master, text="k=")
        self.warm_days_count_label.grid(row=3, column=2, padx=2, pady=2, sticky="w")

        # Заповнення Listbox температурами
        for temp in self.temperatures:
            self.temperature_listbox.insert(END, temp)

    def calculate_temperatures(self):
        # Отримання температур з Listbox
        temperatures = [int(self.temperature_listbox.get(i)) for i in range(self.temperature_listbox.size())]

        # Заповнення Listbox теплими днями та обчислення їх кількості
        warm_days = [temp for temp in temperatures if temp > 0]
        warm_days_count = len(warm_days)

        # Виведення результатів в Listbox
        self.warm_days_listbox.delete(0, END)
        for warm_day in warm_days:
            self.warm_days_listbox.insert(END, warm_day)

        # Виведення інформації про температури
        if temperatures:
            max_temp = max(temperatures)
            min_temp = min(temperatures)
            self.max_label.config(text=f"max={max_temp}")
            self.min_label.config(text=f"min={min_temp}")
            self.warm_days_count_label.config(text=f"k={warm_days_count}")

# Створення головного вікна
root = tk.Tk()
app = TemperatureApp(root)

# Запуск головного циклу програми
root.mainloop()