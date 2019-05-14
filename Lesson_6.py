

'''
1. Создайте классы Noun и Verb.
2. Настройте наследование от Word.
3. Добавьте защищенное свойство «Грамматические характеристики».
4. Перестройте работу метода show класса Sentence.
5. Перестройте работу метода show_part класса Sentence, чтобы он показывал грамматические характеристики.
'''


# Родительский класс 'Word' имеет защищенное свойство, хранящее словарь
# грамматических характеристик для существительного, глагола и прилагательного.
# При создании дочерних объектов для слов в качестве параметров передаются
# само слово и индекс его грамматической характеристики. Текст характеристики
# извлекается из словаря путем обращения к функции 'get_grammar_feature()'
# родительского класса.

class Word:

    __grammar_features = {
        0: 'единственное число',
        1: 'множественное число',
        2: 'настоящее время',
        3: 'прошедшее время',
        4: 'будущее время',
        5: 'качественное',
        6: 'относительное',
        7: 'притяжательное'
    }

    def __init__(self, text, grammar_features_index):
        self.text = text
        self.grammar_features_index = grammar_features_index

    def get_grammar_feature(self):
        return self.__grammar_features[self.grammar_features_index]


class Noun(Word):

    part_of_speech = 'существительное'

    def __init__(self, text='', grammar_features_index=0):
        super().__init__(text, grammar_features_index)


class Verb(Word):

    part_of_speech = 'глагол'

    def __init__(self, text='', grammar_features_index=0):
        super().__init__(text, grammar_features_index)


class Adjective(Word):

    part_of_speech = 'прилагательное'

    def __init__(self, text='', grammar_features_index=0):
        super().__init__(text, grammar_features_index)


class Sentence:

    def __init__(self, words_list, words_order):
        self.words_list = words_list
        self.words_order = words_order

    def show(self):
        sentence = ''
        for i in range(len(self.words_order)):
            sentence = sentence + self.words_list[self.words_order[i]].text + ' '
        return sentence.rstrip().capitalize() + '.'

    # Функция 'show_parts()' возвращает либо части речи, либо грамматические
    #  характеристики слов в зависимости от входного параметра 'info_type'
    def show_parts(self, info_type=''):

        if info_type == 'parts_of_speech':
            parts_of_speech = []
            for i in range(len(self.words_order)):
                parts_of_speech.append(self.words_list[self.words_order[i]].part_of_speech)
            return parts_of_speech

        elif info_type == 'grammar_features':
            grammar_features = []
            for i in range(len(self.words_order)):
                word = self.words_list[self.words_order[i]]
                word = word.get_grammar_feature()
                grammar_features.append(word)
            return grammar_features


w1 = Noun('гряда', 0)
w2 = Adjective('летучая', 5)
w3 = Noun('облаков', 1)
w4 = Verb('редеет', 2)

words_list = [w1, w2, w3, w4]
words_order = [3, 2, 1, 0]
s = Sentence(words_list, words_order)

print('show():', s.show())
print('show_parts():', s.show_parts('parts_of_speech'))
print('show_parts():', s.show_parts('grammar_features'))


# Результат:
#
# show(): Редеет облаков летучая гряда.
# show_parts(): ['глагол', 'существительное', 'прилагательное', 'существительное']
# show_parts(): ['настоящее время', 'множественное число', 'качественное', 'единственное число']
