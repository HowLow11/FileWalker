import os
m = 'C:\\Users\\Ts\\Desktop\\МИНАК'
menu = '1.Просмотр каталога\n2.На уровень вверх\n3.На уровень вниз\n' \
       '4.Количество файлов и каталогов\n5.Размер текущего каталога (в байтах)\n' \
       '6.Поиск файла\n7.Выход из программы'
#os.chdir(m)  # меняет текущую директорию на другую (m)
# print(os.getcwd())  # текущая рабочая директория
# print(os.listdir())  # показывает все файлы и папки текущей директории

def main():
    while True:
        print("[]                 MENU                    []")
        print(os.getcwd())
        print(menu)
        print("[]                                         []")
        command = acceptCommand()
        if str(command).lower() in [exit, quit, '7']:
            print('Работа программы завершена.')
            break
        runCommand(command)
# доработать
def acceptCommand():
    print('Введите Комманду:', end=' ')
    com = str(input())
    if com.lower() == '1':
        return 1
    elif com.lower() == '2':
        return 2
    elif com.lower() == '3':
        return 3
    elif com.lower() == '4':
        return 4
    elif com.lower() == '5':
        return 5
    elif com.lower() == '6':
        return 6
    elif com.lower() == '7':
        return 7
    else:
        print('Неизвестная комманда.', end=' ')
        return acceptCommand()

def catalog():
    """Returns list [filenames, dirnames] from current dir"""
    for path, dirnames, filenames in os.walk(os.getcwd()):
        return [filenames, dirnames]
def moveUp():
    """Moves up in the path"""
    os.chdir(os.getcwd()[:os.getcwd().rfind('\\')])  # *** ВЫЙТИ НА ДИСК С:
def moveDown(currentDir):
    """Moves down in the path to the inputed dir"""
    os.chdir(catalog()[1][currentDir])


def countFiles(path):
    if len(os.listdir()) > 0:
        for i in catalog()[1]:
            b = len(os.listdir())
            moveDown(i)
            if len(catalog()[1]) != 0:
                return int(b/len(catalog()[1])) + countFiles(os.getcwd())
            else:
                return countFiles(os.getcwd())
    else:
        moveUp()
        return 0




def runCommand(command):
    if command == 1:
        j = -1
        print("CATALOG")
        print('Dirnames:')
        for i in catalog()[1]:
            j += 1
            print(str(j)+') ' + i)
        print('Filenames:')
        for i in catalog()[0]:
            j += 1
            print(str(j)+') ' + i)
    if command == 2:
        moveUp()
    if command == 3:
        try:
            moveDown(int(input("Введите номер подкаталога: ")))
        except IndexError:
            print("Ошибка. Значение не относится к подкаталогу.")
            return runCommand(3)
    if command == 4:
        print(countFiles(os.getcwd()))


main()
