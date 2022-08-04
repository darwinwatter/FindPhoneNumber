import CheckNumber
numbersRus, numbersBy = [], []


def fileCheck(file):
    countBy = 0
    countRus = 0
    numFile = open(file)
    line = numFile.readline()
    while line:
        line = numFile.readline()
        for i in range(len(line)):
            chunkRus = line[i:i + 15]
            # print(chunk)
            if CheckNumber.checkNumberRus(chunkRus):
                numbersRus.append(chunkRus)
                countRus += 1

        for i in range(len(line)):
            chunkBy = line[i:i + 16]
            #print(chunk)
            if CheckNumber.checkNumberBy(chunkBy):
                numbersBy.append(chunkBy)
                countBy += 1

    numFile.close()
    print(countBy, countRus)
    if countRus or countBy > 0:
        print('Найденно российских номеров: ' + str(countRus))
        print('Найденно белорусских номеров: ' + str(countBy))
    else:
        print('Номера не найдены.')

def userChooseTxt():
    file_name = input('Введите название файла:\n') + '.txt'
    fileCheck(file_name)

    while True:
        userInput = input('1 - показать российские номера\n'
                          '2 - показать белорусские номера\n'
                          '3 - записать данные в txt файл\n'
                          '4 - закрыть программу\n')
        if userInput == '1':
            print('\nРоссийские номера:\n')
            for number in numbersRus:
                print(number)
            print()
        elif userInput == '2':
            print('\nБелоруссиие номера:\n')
            for number in numbersBy:
                print(number)
            print()
        elif userInput == '3':
            userInput = input('1 - записать российские номера\n'
                              '2 - записать белорусские номера\n'
                              '3 - записать все номера\n'
                              'Нажмите любую кнопку чтобы вернуться назад\n')
            if userInput == '1':
                with open(input('Придумайте название файла:\n') + '.txt', 'w') as f_obj:
                    for number in numbersRus:
                        f_obj.write(number + '\n')
                    print('Номера успешно записаны')
            if userInput == '2':
                with open(input('Придумайте название файла:\n') + '.txt', 'w') as f_obj:
                    for number in numbersBy:
                        f_obj.write(number + '\n')
                    print('Номера успешно записаны')
            if userInput == '3':
                with open(input('Придумайте название файла:\n') + '.txt', 'w') as f_obj:
                    for number in numbersRus:
                        f_obj.write(number + '\n')
                    for number in numbersBy:
                        f_obj.write(number + '\n')
                    print('Номера успешно записаны')

        elif userInput == '4':
            print('Завершение работы.')
            break
        else:
            print('Неверная команда! Попробуйте еще раз.\n')