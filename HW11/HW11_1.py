import random
sentenseList = [1,2,3,4,5]
words = []
nouns = []
verbs = []
def listsCreating(textName):
    text = textRead(textName)
    words = text.split(',')
    for i in range(10):
        nouns.append(words[10+i])
    for i in range(10):
        verbs.append(words[i])
def sentence_1():                   # Утвердительное предложение
    sentence = noun_1() + ' ' + verb_1() + '.'
    return sentence
def sentence_2():                   # Вопросительное предложение
    sentence = noun_1() + ' ' + verb_1() + '?'
    return sentence
def sentence_3():                   # Отрицательное предложение
    sentence = noun_1() + ' не ' + verb_1() + '!'
    return sentence
def sentence_4():                   # Условное предложение
    sentence = noun_1() + ' бы ' + verb_1() + '.'
    return sentence
def sentence_5():                   # Побудительное предложение
    sentence = noun_1() + ', ' + verb_1() + '!'
    return sentence
def noun_1():                       # Подлежащее
    noun = random.choice(nouns)
    return noun
def verb_1():                         # Глагол прошедшего времени
    verb = random.choice(verbs)
    return verb
def create_sentences():
    for i in range(5):
        number = random.choice(sentenseList)
        sentenseList.remove(number)
        if number == 1:
            print(sentence_1())
        elif number == 2:
            print(sentence_2())
        elif number == 3:
            print(sentence_3())
        elif number == 4:
            print(sentence_4())
        else:
            print(sentence_5())
def textRead(textName):
    textName = textName + '.txt'
    f = open(textName, encoding='utf-8')
    text = f.read()
    f.close()
    return text
def main():
    textRead('text')
    listsCreating('text')
    create_sentences()
if __name__ == '__main__':
    main()
