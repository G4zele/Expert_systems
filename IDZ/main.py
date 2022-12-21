parametrs = {
    'days_left' : 60,
    'We_want_to_be_with_frends' : True,
    'frends_answer' : False,
    'planned' : True,
    'Family' : True,
}

def main():
    print('Задача: Как встречать Новый Год?')
    print('Сколько дней до Нового Года?')
    if parametrs['days_left'] > 45:
        print(f'Осталось {parametrs["days_left"]} дней, слишком рано, чтобы планировать')
    elif parametrs['days_left'] < 45 and parametrs['days_left'] > 0:
        print(f'Осталось {parametrs["days_left"]} дней, пора думать как провести Новый год, мы хотим праздновать с друзьями?')
        if parametrs['We_want_to_be_with_frends'] == True:
            print('Да, хотим. Друзья хотят с нами праздновать?')
            if parametrs['frends_answer'] == True:
                print('Да, хотят. Мы планироали как провести новый год?')
                if parametrs['planned'] == True:
                    print('Да, планировали. Празднуем с друзьями в соответствии с планом.')
                else:
                    print('Нет, не планировали. Планируем с друзьями, как провести новый год.')
            else:
                print('Нет, не хотят. Мы можем отпраздновать с семьёй?')
                if parametrs['Family'] == True:
                    print('Да, можем. Празднуем с семьёй.')
                else:
                    print('Нет, не можем. Празднуем одни.')
        else:
            print('Нет, не хотим. Можем отпраздновать с семьёй?')
            if parametrs['Family'] == True:
                print('Да, можем. Празднуем с семьёй.')
            else:
                print('Нет, не можем. Празднуем одни.')
    elif parametrs['days_left'] < 0:
        print(f'Осталось {parametrs["days_left"]} дней, слишком поздно размышлять, будь что будет')


if __name__ == '__main__':
    main()

