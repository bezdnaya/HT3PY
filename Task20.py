'''
В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с английским алфавитом 
очки распределяются так:
● A, E, I, O, U, L, N, S, T, R – 1 очко;
● D, G – 2 очка;
● B, C, M, P – 3 очка;
● F, H, V, W, Y – 4 очка;
● K – 5 очков;
● J, X – 8 очков;
● Q, Z – 10 очков.
А русские буквы оцениваются так:
● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
● Д, К, Л, М, П, У – 2 очка;
● Б, Г, Ё, Ь, Я – 3 очка;
● Й, Ы – 4 очка;
● Ж, З, Х, Ц, Ч – 5 очков;
● Ш, Э, Ю – 8 очков;
● Ф, Щ, Ъ – 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается 
только одно слово, которое содержит либо только английские, либо только русские буквы.


'''
data_one = ['a', 'e', 'i', 'o', 'u', 'l', 'n', 's', 't', 'r', 'а', 'в', 'е', 'и', 'н', 'о', 'р', 'с', 'т']
data_two = ['d', 'g', 'д', 'к', 'л', 'м', 'п', 'у']
data_three = ['b', 'c', 'm', 'p', 'б', 'г', 'ё', 'ь', 'я']
data_four = ['f', 'h', 'v', 'w', 'y', 'й', 'ы']
data_five = ['k', 'ж', 'з', 'х', 'ц', 'ч']
data_eight = ['j', 'x', 'ш', 'э', 'ю']
data_ten = ['q', 'z', 'ф', 'щ', 'ъ']
word = input('Введите слово для Скрабл ').lower()
score = 0
for i in range (len(word)):
    if (word[i] in data_one):
        score += 1
    elif (word[i] in data_two):
        score += 2
    elif (word[i] in data_three):
        score += 3
    elif (word[i] in data_four):
        score += 4
    elif (word[i] in data_five):
        score += 5
    elif (word[i] in data_eight):
        score += 8
    elif (word[i] in data_ten):
        score += 10
print (f'Ваше слово дает {score} очков')

