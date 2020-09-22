bigdata = []
log = input('Start, Quit, devmode: ')
while log != 'Quit':
    if log == "Start":
        classes = int(input('How many classes do we have?: '))
        for stream in range(classes):
            streams = int(input('How many subclasses do we have?: '))
            alphabet = ['а', 'б', "в", "г", "д", "е", "ё", "ж", "з"]
            for class_singular in range(streams):
                amount = int(input(f'How many people are in class {stream+1} {alphabet[class_singular]}: '))
                for i in range(amount):
                    name = input('Name: ')
                    surname = input('Surname: ')
                    data_main = [stream + 1, alphabet[class_singular], name, surname]
                    bigdata.append(data_main)
            print(bigdata)
            break
    elif log == 'devmode':
        clas = int(input('Class: '))
        class_letter = input('Class letter: ')
        name = input('Name: ')
        surname =input('Surname: ')
        data_main = [clas, class_letter, name, surname]
        bigdata.append(data_main)
        log = input('Log: ')
    else:
        print(bigdata)
        log = input('Log: ')
