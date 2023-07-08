from tkinter import Tk, Button, Label, filedialog

class FileSelectorApp:
    def __init__(self):
        self.template_file_path = None
        self.list_file_path = None

        self.root = Tk()
        self.root.title("Выбор файлов")

        self.template_button = Button(self.root, text="Выбрать файл шаблона", command=self.select_template_file)
        self.template_button.pack()

        self.template_label = Label(self.root, text="Шаблон не выбран")
        self.template_label.pack()

        self.list_button = Button(self.root, text="Выбрать файл списка", command=self.select_list_file)
        self.list_button.pack()

        self.list_label = Label(self.root, text="Список не выбран")
        self.list_label.pack()

        self.load_button = Button(self.root, text="Загрузить", command=self.load_files)
        self.load_button.pack()

    def select_template_file(self):
        self.template_file_path = filedialog.askopenfilename(title="Выберите файл шаблона")
        self.template_label.config(text=self.template_file_path)

    def select_list_file(self):
        self.list_file_path = filedialog.askopenfilename(title="Выберите файл списка")
        self.list_label.config(text=self.list_file_path)

    def load_files(self):
        print("Выбранный файл шаблона:", self.template_file_path)
        print("Выбранный файл списка:", self.list_file_path)
        self.root.destroy()  # Закрываем текущее окно
        self.create_assembly_window()

    def create_assembly_window(self):
        assembly_window = Tk()
        assembly_window.title("Сборка")
        # Добавьте нужные элементы в новое окно сборки
        assembly_window.mainloop()

    def run(self):
        self.root.mainloop()

# Create an instance of the app and run it
app = FileSelectorApp()
app.run()