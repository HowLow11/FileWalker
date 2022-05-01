"""Case-study Файловая система
Разработчики:
Лынник Д.О. 70% , Ячин Д.В. 40%.

"""
import os


def main():
    menu = '1.Просмотр каталога\n2.На уровень вверх\n3.На уровень вниз\n' \
           '4.Количество файлов и каталогов\n5.Размер текущего каталога (в байтах)\n' \
           '6.Поиск файла\n7.Выход из программы'

    while True:
        print("[]                 MENU                    []")
        print(os.getcwd())
        print(menu)
        print("[]                                         []")
        command = acceptCommand()
        if str(command).lower() == 7:
            print('Работа программы завершена.')
            break
        runCommand(command)


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
    os.chdir(os.getcwd()[:os.getcwd().rfind('\\')])


def moveDown(currentDir):
    """Moves down in the path to the inputed dir"""
    os.chdir(catalog()[1][currentDir])


def countFiles():
    """Counts the amount of files in current dir"""
    files_ = []
    dirs_ = []
    for paths, dirnames, filenames in os.walk(os.getcwd(), topdown=True, onerror=None, followlinks=False):
        for file in filenames:
            files_.append(file)
        for dir in dirnames:
            dirs_.append(dir)
    result = 'Файлов: '+str(len(files_))+'\nПапок: '+str(len(dirs_))
    return result


def countBytes():
    bytes = 0
    c_path = os.getcwd()
    moveUp()
    path = os.getcwd()
    for paths, dirnames, filenames in os.walk(path, topdown=True, onerror=None, followlinks=False):
        for dir in dirnames:
            bytes += os.stat(dir).st_size
    os.chdir(c_path)
    return "Объем всех файлов в текущей папке: "+str(bytes)


def findFiles(target, path, files_):
    files = os.listdir(path)
    for file in files:
        file = str(file)
        dir = str(path)+'\\'+str(file)
        if not os.path.isdir(dir):
            if file.find(target) != -1:
                files_.append(dir)
        else:
            try:
                findFiles(target, dir, files_)
            except PermissionError:
                continue
    return files_


def runCommand(command):
    if command == 1:
        j = -1
        print("CATALOG")
        print('Папки:')
        for i in catalog()[1]:
            j += 1
            print(str(j)+') ' + i)
        print('Файлы:')
        for i in catalog()[0]:
            j += 1
            print(str(j)+') ' + i)
    if command == 2:
        moveUp()
    if command == 3:
        try:
            moveDown(int(input('Введите номер подкаталога: ')))
        except IndexError:
            print('Ошибка. Значение не относится к подкаталогу.')
            return runCommand(3)
    if command == 4:
        print(countFiles())
    if command == 5:
        print(countBytes())
    if command == 6:
        files_ = []
        path = os.getcwd()
        files_ = findFiles(str(input('Введите имя искомого файла: ')), path, files_)
        if not files_:
            print('Отсутсвуют файлы с данным названием')
        else:
            print('Пути к файлам с данным названием:')
            a = -1
            for file in files_:
                a += 1
                print(str(a)+') '+file)


main()
