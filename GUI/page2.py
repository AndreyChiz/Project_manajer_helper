import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class ComboboxWindow(tk.Tk):
    """Окно приложения с Combobox."""

    def __init__(self):
        super().__init__()
        self.title("Окно с Combobox")
        self.list1 = ['Элемент 1', 'Элемент 2', 'Элемент 3', 'Элемент 4']
        self.list2 = ['Пункт A', 'Пункт B', 'Пункт C', 'Пункт D', 'ауаца']
        self.index_list_main = []
        self.index_list_row = []
        self.save_folder = ""

    def on_select(self, event):
        """Обработчик выбора элемента Combobox."""
        selected_item = event.widget.get()
        print(f'Выбранный элемент: {selected_item}')

    def create_combobox(self, parent, values):
        """Создает Combobox с заданными значениями."""
        combo = ttk.Combobox(parent, values=values)
        combo.current(0)
        combo.bind('<<ComboboxSelected>>', self.on_select)
        return combo

    def truncate_text(self, text, max_length):
        """Обрезает текст до заданной длины и добавляет многоточие, если необходимо."""
        if len(text) > max_length:
            return text[:max_length-3] + "..."
        return text

    def create_index_list(self):
        """Создает список индексов выбранных элементов."""
        self.index_list_main = [combobox.current() for combobox in self.comboboxes]
        self.index_list_row = [combobox.current() for combobox in self.combobox_row]
        self.save_folder = self.save_folder_entry.get()
        print(f'Список индексов (Главный): {self.index_list_main}')
        print(f'Список индексов (Строка): {self.index_list_row}')
        print(f'Папка для сохранения: {self.save_folder}')

    def choose_folder(self):
        """Открывает диалоговое окно для выбора папки сохранения."""
        folder_path = filedialog.askdirectory()
        self.save_folder_entry.delete(0, tk.END)
        self.save_folder_entry.insert(tk.END, folder_path)

    def run(self):
        """Запускает основной цикл приложения."""
        self.comboboxes = []

        for i, item in enumerate(self.list1):
            truncated_item = self.truncate_text(item, 24)
            label = tk.Label(self, text=truncated_item, anchor='w')
            label.grid(row=i, column=0, padx=10, pady=5, sticky='w')
            combobox = self.create_combobox(self, self.list2)
            combobox.grid(row=i, column=1, padx=10, pady=5, sticky='we')
            self.comboboxes.append(combobox)

        label_row = tk.Label(self, text="Строка с Combobox")
        label_row.grid(row=len(self.list1), column=0, padx=10, pady=5, sticky='w')

        self.combobox_row = []
        for i in range(3):
            combobox = self.create_combobox(self, self.list2)
            combobox.grid(row=len(self.list1), column=i+1, padx=10, pady=5, sticky='we')
            self.combobox_row.append(combobox)

        save_folder_label = tk.Label(self, text="Сохранить в:")
        save_folder_label.grid(row=len(self.list1)+1, column=0, padx=10, pady=5, sticky='w')

        self.save_folder_entry = tk.Entry(self)
        self.save_folder_entry.grid(row=len(self.list1)+1, column=1, columnspan=2, padx=10, pady=5, sticky='we')

        browse_button = tk.Button(self, text="Обзор", command=self.choose_folder)
        browse_button.grid(row=len(self.list1)+1, column=3, padx=10, pady=5, sticky='e')

        button = tk.Button(self, text="Создать список индексов", command=self.create_index_list)
        button.grid(row=len(self.list1)+2, column=0, columnspan=4, padx=10, pady=10)

        self.mainloop()

# Создаем экземпляр класса ComboboxWindow и запускаем приложение
window = ComboboxWindow()
window.run()
