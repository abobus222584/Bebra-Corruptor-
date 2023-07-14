import tkinter as tk
from tkinter import filedialog, messagebox
import shutil
import random

def corrupt_file():
    try:
        file_path = file_entry.get()
        start_value = int(start_entry.get())
        end_value = int(end_entry.get())
        inc_value = int(inc_entry.get())

        # Создаем копию файла
        file_copy_path = file_path + ".corrupted"
        shutil.copy2(file_path, file_copy_path)

        # Открываем копию файла в двоичном режиме
        with open(file_copy_path, "rb+") as file:
            file_size = file.seek(0, 2)
            file.seek(0)

            # Повреждаем содержимое файла
            while file.tell() < file_size:
                byte_position = file.tell()
                byte = file.read(1)

                # Изменяем случайный байт в файле
                new_byte = random.randint(start_value, end_value)
                file.seek(byte_position)
                file.write(bytes([new_byte]))

        messagebox.showinfo("Success", "Файл успешно поврежден: " + file_copy_path)
    except Exception as e:
        messagebox.showerror("Error", "Ошибка при повреждении файла: " + str(e))


def browse_file():
    file_path = filedialog.askopenfilename()
    file_entry.delete(0, tk.END)
    file_entry.insert(tk.END, file_path)


# Создание графического интерфейса
window = tk.Tk()
window.title("Bebra Corruptor")

# Загрузка логотипа
logo_image = tk.PhotoImage(file="C:/Users/Axand/OneDrive/Рабочий стол/BebraCorrupt_v1.0/assets/logo.png")  # Укажите путь к файлу с логотипом

# Создание элемента Label для логотипа
logo_label = tk.Label(window, image=logo_image)
logo_label.pack()

file_label = tk.Label(window, text="Выберите файл:")
file_label.pack()

file_entry = tk.Entry(window, width=50)
file_entry.pack()

browse_button = tk.Button(window, text="Обзор", command=browse_file)
browse_button.pack()

start_label = tk.Label(window, text="Start Value:")
start_label.pack()

start_entry = tk.Entry(window, width=10)
start_entry.pack()

end_label = tk.Label(window, text="End Value:")
end_label.pack()

end_entry = tk.Entry(window, width=10)
end_entry.pack()

inc_label = tk.Label(window, text="Inc Value:")
inc_label.pack()

inc_entry = tk.Entry(window, width=10)
inc_entry.pack()

corrupt_button = tk.Button(window, text="Corrupt", command=corrupt_file)
corrupt_button.pack()

window.mainloop()
