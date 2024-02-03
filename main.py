# a=[int(i) for i in ent.get().split(",")]

import tkinter as tk

def calculate_temperatures():
    # Отримати введені температури та вивести їх у консоль
    input_temperatures = entry.get()
    temperatures = [int(i) for i in input_temperatures.split(",")]

    # Обчислити мінімальну та максимальну температури
    min_temperature = min(temperatures)
    max_temperature = max(temperatures)

    # Підрахунок кількості днів з температурою вище 0 градусів
    above_zero_days = sum(temp > 0 for temp in temperatures)

    # Вивести результати у консоль
    print(f"Введені температури: {temperatures}")
    print(f"Мінімальна температура: {min_temperature}")
    print(f"Максимальна температура: {max_temperature}")
    print(f"Днів з температурою вище 0 градусів: {above_zero_days}")
    # Додайте код для інших обчислень тут

    # Вивести результати на вікно програми
    result_label.config(text=f"Мінімальна температура: {min_temperature}\n"
                             f"Максимальна температура: {max_temperature}\n"
                             f"Днів з температурою вище 0 градусів: {above_zero_days}")

# Створити головне вікно
root = tk.Tk()
root.title("Обчислення температур")

# Додати текстове поле для введення температур
entry_label = tk.Label(root, text="Введіть температури через кому:")
entry_label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

# Додати кнопку для обчислення
calculate_button = tk.Button(root, text="Обчислити", command=calculate_temperatures)
calculate_button.pack(pady=10)

# Вивести результати
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Запустити головний цикл програми
root.mainloop()