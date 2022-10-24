input_text = input('Введи текст в котором нужно исключить слова с последовательностью "абв"')
print(' '.join((filter(lambda x: 'абв' not in x, input_text.split()))))