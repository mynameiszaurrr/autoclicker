import time
import random
import keyboard
import pyautogui

print('Привет, нацелься ровно на центр кнопки лайка на экране тиндера, когда ты нацелишься зажми на 2 секунды кнопку'
      ' ctrl + alt')

r = 30
try:
    while True:
        # Следим за координатами мыши и регистрируем нажатие ctrl + alt
        like_x, like_y = pyautogui.position()
        if keyboard.is_pressed('ctrl+alt'):

            # границы лайка
            down_border_like = [like_x, like_y + r]
            upper_border_like = [like_x, like_y - r]
            left_border_like = [like_x - r, like_y]
            right_border_like = [like_x + r, like_y]

            # границы дизлайка
            down_border_dislike = [like_x - 145, like_y + r]
            upper_border_dislike = [like_x - 145, like_y - r]
            left_border_dislike = [like_x - r - 145, like_y]
            right_border_dislike = [like_x - 115, like_y]

            # Границы "слепого лайка"
            x_blind_zone = (like_x - 115) + (left_border_like[0] - right_border_dislike[0])//2
            y_blind_zone = down_border_like[1] + 5

            print(f'Что бы остановить программу зажми и держи ctrl+shift')
            print('Я начинаю работать, можешь пока попить чаю с печеньками... ')

            # Вычисляем центр и радиус круга лайка
            x_center_like = (left_border_like[0] + right_border_like[0]) // 2
            y_center_like = (upper_border_like[1] + down_border_like[1]) // 2
            radius_like = (right_border_like[0] - left_border_like[0]) // 2

            # Вычисляем центр и радиус круга дизлайка
            x_center_dislike = (left_border_dislike[0] + right_border_dislike[0]) // 2
            y_center_dislike = (upper_border_dislike[1] + down_border_dislike[1]) // 2
            radius_dislike = (right_border_dislike[0] - left_border_dislike[0]) // 2

            like_count = 0
            dis_count = 0

            while True:
                # Делаем выбор лайка - дизлайка в соотношении 9:1
                choices = ['like', 'dislike']
                if random.randint(1, 50) == 1:
                    click = choices[1]
                    dis_count += 1
                    # Клик
                    x_rand = random.randint(x_center_dislike - radius_dislike, x_center_dislike + radius_dislike)
                    y_rand = random.randint(y_center_dislike - radius_dislike, y_center_dislike + radius_dislike)
                    pyautogui.click(x_rand, y_rand)

                    # Жмем следующее фото
                    random_number = random.randint(1, 3)
                    for i in range(random_number):
                        pyautogui.click(x_blind_zone, y_blind_zone)
                        keyboard.press_and_release('space')
                        time.sleep(random.uniform(0.1, 0.8))

                else:
                    click = choices[0]
                    like_count += 1
                    # Клик
                    x_rand = random.randint(x_center_like - radius_like, x_center_like + radius_like)
                    y_rand = random.randint(y_center_like - radius_like, y_center_like + radius_like)
                    pyautogui.click(x_rand, y_rand)

                    # Жмем следующее фото
                    random_number = random.randint(1, 3)
                    for i in range(random_number):
                        pyautogui.click(x_blind_zone, y_blind_zone)
                        keyboard.press_and_release('space')
                        time.sleep(random.uniform(0.1, 0.8))

                # Отдых от 1 до 3 сек в миллисекундых
                time.sleep(random.uniform(1, 2))
                #
                # Функция экстренной остановки программы
                if keyboard.is_pressed('ctrl+shift'):
                    print(f'Проставлено {like_count} лайков и {dis_count} дизлайков')
                    break
            break

except Exception as e:
    print(f'Ошибка - {e}\n'
          f'Свяжитесь с разработчиком по тг - @admitg')