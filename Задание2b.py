import random

total_candies = 2017
print(f'на столе всего конфет: {total_candies}')
first_bot = 0 # счетчик для проверки, ошибся ли человек в стратегии

while total_candies > 0:

  while True:
      try:
          first_player = int(input(f'сколько конфет возьмет человек: '))
          if first_player > 0 and first_player <=28 and first_player <= total_candies:
              total_candies -= first_player
              print(f'человек взял {first_player} конфет(ы), на столе осталось {total_candies} конфет')
              if total_candies == 0:
                  print(f'человек одержал победу')
              break
          elif (first_player <= 0 or first_player > 28) and first_player <= total_candies:
              print(f'нужно взять более 0, но не более 28 конфет' )
          else:
              print(f'осталось только {total_candies} конфет')
      except:
          print("количество конфет должно быть числом")

  if total_candies == 0:
    break
  
  if total_candies > 28:
    if first_bot == 0:
      if total_candies % 29 != 0:
        bot_player = total_candies- 29*(total_candies//29)
        first_bot +=1
      else:
        bot_player = random.randrange(1, 29)
    else:
        bot_player = 29-first_player
  else:
      bot_player = total_candies

  total_candies -=bot_player
  print(f'бот взял {bot_player} конфет(ы), на столе осталось {total_candies} конфет')
  if total_candies == 0:
    print(f'бот одержал победу')