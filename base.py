import numpy as np

#Усовершенствованна функция угадывания
def game_core_v3(number):
    '''В отличие от v2 не просто предлагаем случайное число в качестве ответа, а берем середину диапазона, в котором загадано число, 
    тем самым вдвое уменьшая этот диапазон при каждой попытке.
    Функция принимает загаданное число и возвращает число попыток'''
    
    count = 1 #счетчик попыток
    low_border = 0 # Нижняя граница диапазона,не входит в диапазон.
    up_border = 101 # Верхняя граница диапазона, по традиции, не входит в диапазон 
    
    if number >= up_border:
        print('Загаданное число больше верхней границы диапазона.')
        return(0)
    if number <= low_border:
        print('Загаданное число меньше нижней границы диапазона.')
        return(0)
    
    predict = (up_border - low_border) // 2 # получаем середину диапазона
    while number != predict:
        #print(f"Predict={predict} low_border={low_border} up_border={up_border}")
        count += 1
        
        if number > predict:
            low_border = predict  # сдвигаем нижнюю границу
            predict += (up_border - low_border) // 2
        elif number < predict: 
            up_border=predict # сдвигаем верхнюю границу
            predict -= (up_border - low_border) // 2
			
        if count > 101: # Ограничиваем число попыток , если что-то пойдет не так.
            break
			
    return(count) # выход из цикла, если угадали



def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  #  фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)
	


score_game(game_core_v3)

