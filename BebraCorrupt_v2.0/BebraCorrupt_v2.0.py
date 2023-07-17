import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Combobox
import shutil
import random

# Путь к файлу с логотипом
LOGO_PATH = "C:/Users/Axand/OneDrive/Рабочий стол/BebraCorrupt_v2.0/assets/logo.png"

# Список доступных алгоритмов
ALGORITHMS = [
    "Incrementer Algorithm",
    "Randomizer Algorithm",
    "Scrambler Algorithm",
    "Copier Algorithm",
    "Titler Algorithm",
    "Smoother Algorithm",
    "Blender Algorithm"
]


def corrupt_file():
    try:
        file_path = file_entry.get()
        start_value = int(start_entry.get())
        end_value = int(end_entry.get())
        inc_value = int(inc_entry.get())
        selected_algorithm = algorithm_combobox.get()

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

                # Применяем выбранный алгоритм повреждения файла
                byte = apply_algorithm(selected_algorithm, byte, start_value, end_value, inc_value)

                file.seek(byte_position)
                file.write(byte)

        messagebox.showinfo("Success", "Файл успешно поврежден: " + file_copy_path)
    except Exception as e:
        messagebox.showerror("Error", "Ошибка при повреждении файла: " + str(e))


def apply_algorithm(algorithm, byte, start_value, end_value, inc_value):
    if algorithm == "Incrementer Algorithm":
        return incrementer_algorithm(byte, start_value, end_value, inc_value)
    elif algorithm == "Randomizer Algorithm":
        return randomizer_algorithm(byte, start_value, end_value, inc_value)
    elif algorithm == "Scrambler Algorithm":
        return scrambler_algorithm(byte, start_value, end_value, inc_value)
    elif algorithm == "Copier Algorithm":
        return copier_algorithm(byte, start_value, end_value, inc_value)
    elif algorithm == "Titler Algorithm":
        return titler_algorithm(byte, start_value, end_value, inc_value)
    elif algorithm == "Smoother Algorithm":
        return smoother_algorithm(byte, start_value, end_value, inc_value)
    elif algorithm == "Blender Algorithm":
        return blender_algorithm(byte, start_value, end_value, inc_value)


def incrementer_algorithm(byte, start_value, end_value, inc_value):
    new_byte = (byte + inc_value) % (end_value - start_value + 1) + start_value
    return bytes([new_byte])


def randomizer_algorithm(byte, start_value, end_value, inc_value):
    new_byte = random.randint(start_value, end_value)
    return bytes([new_byte])


def scrambler_algorithm(byte, start_value, end_value, inc_value):
    binary_string = bin(byte)[2:].zfill(8)
    scrambled_string = "".join(random.sample(binary_string, len(binary_string)))
    new_byte = int(scrambled_string, 2)
    return bytes([new_byte])


def copier_algorithm(byte, start_value, end_value, inc_value):
    return bytes([byte])


def titler_algorithm(byte, start_value, end_value, inc_value):
    new_byte = start_value
    return bytes([new_byte])


def smoother_algorithm(byte, start_value, end_value, inc_value):
    if byte > start_value:
        new_byte = byte - inc_value
    else:
        new_byte = byte + inc_value
    return bytes([new_byte])


def blender_algorithm(byte, start_value, end_value, inc_value):
    blend_amount = random.uniform(0, 1)
    new_byte = int((byte * (1 - blend_amount)) + (start_value * blend_amount))
    return bytes([new_byte])


def browse_file():
    file_path = filedialog.askopenfilename()
    file_entry.delete(0, tk.END)
    file_entry.insert(tk.END, file_path)


# Создание графического интерфейса
window = tk.Tk()
window.title("File Corruptor")

# Загрузка логотипа
logo_image = tk.PhotoImage(file=put directory here)

# Создание метки с логотипом
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

algorithm_label = tk.Label(window, text="Выберите алгоритм:")
algorithm_label.pack()

algorithm_combobox = Combobox(window, values=ALGORITHMS)
algorithm_combobox.pack()

corrupt_button = tk.Button(window, text="Corrupt", command=corrupt_file)
corrupt_button.pack()

window.mainloop()
