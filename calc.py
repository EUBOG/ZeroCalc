import tkinter as tk

def click(event):
    current = entry.get()
    if event.widget.cget("text") == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Ошибка")
    elif event.widget.cget("text") == "C":
        entry.delete(0, tk.END)  # Очищаем поле ввода
    else:
        entry.insert(tk.END, event.widget.cget("text"))

# Создаем главное окно
root = tk.Tk()
root.title("Калькулятор")

# Создаем поле ввода
entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# Создаем кнопки
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# Размещаем кнопки в сетке
row = 1
col = 0
for button in buttons:
    btn = tk.Button(root, text=button, font=("Arial", 18), width=4, height=2)
    btn.grid(row=row, column=col)
    btn.bind("<Button-1>", click)  # Привязываем событие нажатия кнопки
    col += 1
    if col > 3:
        col = 0
        row += 1

# Запускаем главный цикл
root.mainloop()