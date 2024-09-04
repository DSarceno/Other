import subprocess
import os


class Report:
    def __init__(self) -> None:
        self.bat = '.\dockerrun.bat'

    def delShitFiles(self, name : str) -> None:
        # creamos la lista de archivos a eliminar
        files_to_delete = [name + ext for ext in ['.aux', '.bbl', '.log', '.blg', '.out', '.toc']]

        # se eliminan los archivos
        for file in files_to_delete:
            try:
                os.remove(file)
            except FileNotFoundError:
                print(f'{file} not found')
                continue


if __name__ in "__main__":
    rep = Report()

    rep.delShitFiles('main')
