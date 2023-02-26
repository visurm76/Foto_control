import os

def searchFile(filename):
    """
    Функиция определения пути расположения файла по его названию
    """

    for root, dirnames, filenames in os.walk('/home/viktor/'):
        for file in filenames:
            if file == filename:
                return os.path.join(root, file)