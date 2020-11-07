import numpy as np

#Базовая функция угадывания
def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    predict = np.random.randint(1,101)
    while number != predict:
        count+=1
        if number > predict: 
            predict += 1
        elif number < predict: 
            predict -= 1
    return(count) # выход из цикла, если угадали

#Усовершенствованна функция угадывания
def game_core_v3(number):
    '''В отличие от v2 не просто предлагаем случайное число в качестве ответа, а берем середину диапазона, в котором загадано число, 
	тем самым вдвое уменьшая этот диапазон при каждой попытке.
    Функция принимает загаданное число и возвращает число попыток'''
    
    count = 1
    l_border = 0 # Нижняя граница диапазона,не входит в диапазон, за счет этого упрощаем алгоритм.
    u_border = 101 #Верхняя граница диапазона, по традиции, не входит в диапазон 
    
    
    predict = (u_border - l_border) // 2
	
    while number != predict:
        print('Predict={} l_border={} u_border={}'.format(predict,l_border,u_border))
        count += 1
        
        if number > predict:
            l_border = predict
            predict += (u_border - l_border) // 2
            #predict += 1
        elif number < predict: 
            u_border=predict
            predict -= (u_border - l_border) // 2
        if count > 101:
            break
    print('Загаданное число=',predict)
    return(count) # выход из цикла, если угадали


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)