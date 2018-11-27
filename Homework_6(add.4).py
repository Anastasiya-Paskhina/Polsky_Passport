documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит

def people():
    number_input = input('Введите номер документа:')
    result = 'Документ не найден'
    for number_document in documents:
        if number_document['number'] == number_input:
            result = number_document['name']
            break
    print(result)


# people()

# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин"

def list_p():
    for param in documents:
        print(param['type'], param['number'], param['name'])


# # list_p()


# # s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;

def shelf():
    number_input = input('Введите номер документа')
    result = 'Документ не найден'
    for directory, documents_number in directories.items():
        if number_input in documents_number:
            result = directory
            break
    print(result)


# shelf()

# # a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.


def new_doc():
    input_number = input('введите номер документа')
    input_type = input('Введите тип документа')
    input_name = input('Введите имя владельца')
    input_shelf = input('Введите номер полки')
    for number_shelf in directories:
        if int(input_shelf) <= 3:
            directories[input_shelf].append(input_number)
            print(directories)
            documents.append({'type': input_type, 'number': input_number, 'name': input_name})
            print(documents)
            break
        else:
            print('Такой полки нет')
            return number_shelf


# new_doc()

## Дополнение по заданию из 6 лекции:

def names_of_documents():
    for document in documents:
        try:
            print(document["name"])
        except KeyError:
            print('Документ №{} не содержит поле "Имя"'.format(document["number"]))


# names_of_documents()

while True:
    user_input = input('\n Команды: p, l, s, a, nd, help.\n Для выхода введите: Выход\n Введите команду:')
    if user_input == 'p':
        people()
    elif user_input == 'l':
        list_p()
    elif user_input == 's':
        shelf()
    elif user_input == 'a':
        new_doc()
    elif user_input == 'nd':
        names_of_documents()
    elif user_input == 'Выход':
        break
    elif user_input == 'help':
        print('\n p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;\n l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";\n s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;\n a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться;\n nd - names_of_documents - команда вывода всех имен.')
    else:
        print("Ошибка")