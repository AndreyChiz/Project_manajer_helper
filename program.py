import Project_build.GUI.page1 as p


if __name__ == '__main__':
    window1 = p.FileSelectorApp()
    window1.run()
    print(window1.template_file_path)
    print(window1.list_file_path)