import utils.messages as messages

def select_language():
    print(messages.SELECT_LANGUAGE_MESSAGE)
    print(messages.ENGLISH_OPTION_MESSAGE)
    print(messages.SPANISH_OPTION_MESSAGE)

    language = input(messages.ENTER_NUMBER_MESSAGE)

    if language == '1':
        print()
        return "EN"
    elif language == '2':
        print()
        return "ES"
    else:
        print(messages.INVALID_OPTION_MESSAGE)
        return select_language()
