# coding: utf-8
import codecs
import locale
import re

locale.setlocale(locale.LC_ALL, 'ru-RU')

ka = [[1, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 26],
      [27, 26, 27, 27, 2, 27, 27, 27, 27, 21, 27, 27, 27, 27, 27, 27],
      [27, 27, 27, 27, 27, 3, 7, 11, 15, 27, 27, 27, 27, 27, 27, 27],
      [27, 27, 4, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27],
      [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
      [27, 26, 27, 6, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27],
      [27, 27, 27, 27, 27, 27, 7, 11, 15, 27, 22, 27, 27, 27, 27, 27],
      [27, 27, 8, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27],
      [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
      [27, 26, 27, 10, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27],
      [27, 27, 27, 27, 27, 3, 27, 11, 15, 27, 27, 27, 27, 27, 27, 27],
      [27, 27, 12, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27],
      [13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13],
      [27, 26, 27, 14, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27],
      [27, 27, 27, 27, 27, 3, 7, 27, 15, 27, 27, 27, 27, 27, 27, 27],
      [27, 27, 16, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27],
      [27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 17, 18, 19, 27, 27],
      [27, 26, 27, 20, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27],
      [27, 26, 27, 20, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27],
      [27, 26, 27, 20, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27],
      [27, 27, 27, 27, 27, 3, 7, 11, 27, 27, 22, 27, 27, 27, 27, 27],
      [27, 26, 27, 27, 27, 3, 27, 27, 15, 27, 22, 27, 27, 27, 27, 27],
      [27, 27, 23, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27],
      [24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24],
      [27, 26, 27, 25, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27],
      [27, 27, 27, 27, 27, 3, 27, 27, 15, 27, 27, 27, 27, 27, 27, 27],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

str = []
exitstr = []

with codecs.open('input.txt', encoding='utf-8') as finput:  # считывание в str паттерна
    str = finput.read()
finput.close()


print("Исходная строка: ")
str = re.sub('\s{2,}', ' ', str)
print(str)

length = len(re.findall(r'\{(.*?)\}', str))

foutput = open("output.txt", 'w')
for i in range(length):  # цикл разбивающий всё на секции, работает с одной секцией за раз

    # START CICLE

    tempstr = re.search(r'(\{)(.*?)(?=\{)', str)  # получение текущей секции
    if i != length - 1:
        tempstr = tempstr.group()
    else:
        tempstr = str
    print("Текущий кусок: ")
    print(tempstr)

    # получение текста после секции отдельно
    literal = re.search(r'(?<=})(.*?)(?=$)', tempstr)
    literal = literal.group()
    print("Текст для редактирования: ")
    print(literal)

    # кодирование текста отдельным кодом
    exitstr = tempstr.replace(literal, "15 ")
    # а остальные спец символы другими для КА
    exitstr = exitstr.replace("{", "0 ")
    exitstr = exitstr.replace("}", " 1 ")
    exitstr = exitstr.replace("=", "2 ")
    exitstr = exitstr.replace(",", " 3 ")
    exitstr = exitstr.replace("SECT", "4 ")
    exitstr = exitstr.replace("col", "5 ")
    exitstr = exitstr.replace("line", "6 ")
    exitstr = exitstr.replace("indent", "7 ")
    exitstr = exitstr.replace("align", "8 ")
    exitstr = exitstr.replace("TABLE", "9 ")
    exitstr = exitstr.replace("width", "10 ")
    exitstr = exitstr.replace("r", "11 ")
    exitstr = exitstr.replace("l", "12 ")
    exitstr = exitstr.replace("c", "13 ")
    # оказался ненужен, но в автомате он есть, пусть будет
    exitstr = exitstr.replace("|", "14 ")

    # получение из текстового набора цифр, числовой массив
    print("Массив токенов: ")
    tokens = [int(x) for x in exitstr.split()]
    print(tokens)

    # удаление из исходной строки ту часть что мы отработали
    str = str.replace(tempstr, "")
    print("Остаток файла: ")
    print(str)
    print('\n')

    # МЕСТО для вписывания текста
    # переменные счетчик и параметры по умолчанию
    s = 0
    isTable = 0
    indent = 1
    width = 1
    col = 1
    line = 1
    # цикл(КА) в котором идет получение нужных токенов для будущей логики
    for token in tokens:
        s = ka[s][token]
        if s == 5:
            print("col = ", token)
            col = token
        elif s == 9:
            print("line = ", token)
            line = token
        elif s == 13:
            print("indent = ", token)
            indent = token
        elif s == 17:
            print("align = r")
            align = 'r'
        elif s == 18:
            print("align = l")
            align = 'l'
        elif s == 19:
            print("align = c")
            align = 'c'
        elif s == 24:
            print("width = ", token)
            width = token
        elif s == 21:
            isTable = 1
    # ----------------
    if isTable == 0:  # если секция а не таблица
        words = literal.split()  # получение слов из строки
        c = 1  # счетчики col and line
        l = 0
        result = []  # создание и очистка результата
        result.append('\x20' * (indent - 1))
        # тут в массив слова добавляются элементв построения строк и рузельтата
        for word in words:
            if c != col:
                result.append(word)
                c += 1
            else:
                result.append(word)
                result.append('\n')
                result.append('\x20' * (indent - 2))
                c = 1
                l += 1
                if l == line:
                    result.append('\n')
                    result.append('\x20' * (indent - 2))
                    l = 0
        result = ' '.join(result)  # получение цельной строки из набора слов
        result_str = result.split('\n')  # разбиение по строкам
        for s in result_str:  # вывод-запись по критерию выравнивания
            if align == 'l':
                foutput.write(s + '\n')
            if align == 'c':
                foutput.write(s.center(90) + '\n')
            if align == 'r':
                foutput.write('{:>100}'.format(s) + '\n')
    # ----------------------------
    if isTable == 1:  # анлогичный блок только для таблицы
        words = literal.split('|')
        k = 1
        j = 0
        result = []

        for word in words:  # выравнивание по ширине максимального столбца
            if len(word) > width:
                width = len(word)

        result.append(' ' + '_' * (width * col + 4 * col) + '\n')

        for word in words:
            if k != col:
                result.append('|')
                if align == 'l':
                    result.append(word)
                elif align == 'r':
                    result.append(' ' * (width - len(word)))
                    result.append(word)
                elif align == 'c':
                    result.append(' ' * int(((width - len(word)) / 2)))
                    result.append(word)
                    result.append(' ' * (width - len(word) -
                                  int(((width - len(word)) / 2))))
                if len(word) < width and align == 'l':
                    result.append(' ' * (width - len(word)))
                k += 1
                j += 1
                if j == len(words) and (len(words) % col) != 0:
                    tmp = len(words)
                    result.append('|')
                    while (tmp % col) != 0:
                        if align == 'c':
                            result.append(' ' * (width + 2) + ' |')
                        else:
                            result.append(' ' * (width + 2) + '|')
                        tmp += 1
                    result.append('\n')
            else:
                result.append('|')
                if align == 'l':
                    result.append(word)
                elif align == 'r':
                    result.append(' ' * (width - len(word)))
                    result.append(word)
                elif align == 'c':
                    result.append(' ' * int(((width - len(word)) / 2)))
                    result.append(word)
                    result.append(' ' * (width - len(word) -
                                  int(((width - len(word)) / 2))))
                if len(word) < width and align == 'l':
                    result.append(' ' * (width - len(word)))
                result.append('|' + '\n')
                result.append('_' * (width * col + 4 * col) + '\n')
                k = 1
                j += 1
        result = ' '.join(result)  # запись и т д
        result_str = result.split('\n')
        for s in result_str:
            if align == 'l':
                foutput.write(s + '\n')
            if align == 'c':
                foutput.write(s.center(90) + '\n')
            if align == 'r':
                foutput.write('{:>100}'.format(s) + '\n')
foutput.close()

# END CICLE
