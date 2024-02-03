import tkinter as tk

def calculate_temperatures():
    temperatures = entry.get().split(',')
    
    # Конвертуємо введені дані в числа
    temperatures = [float(temp.strip()) for temp in temperatures]

    # Виводимо результати
    result_label.config(text=f"Температури: {temperatures}\n"
                              f"Мінімальна температура: {min(temperatures)}\n"
                              f"Максимальна температура: {max(temperatures)}\n"
                              f"Днів з температурою вище 0 градусів: {sum(temp > 0 for temp in temperatures)}")

# Створюємо головне вікно
root = tk.Tk()
root.title("Обчислення температур")

# Додаємо елементи вікна
label = tk.Label(root, text="Введіть температури через кому:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

calculate_button = tk.Button(root, text="Обчислити", command=calculate_temperatures)
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Запускаємо головний цикл програми
root.mainloop()