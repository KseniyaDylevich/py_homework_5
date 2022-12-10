import random

total_candies = 2017
first = random.randrange(1, 3)

if first == 1:
  second = 2
else:
  second = 1

moves_count = 1

print(f'на столе всего конфет: {total_candies}')
print(f'игру начинает игрок {first}')
while total_candies > 0:

  if moves_count % 2 != 0:
      player = first
  else:
      player = second

  while True:
      try:
          current_player = int(input(f'сколько конфет возьмет игрок {player}: '))
          if current_player > 0 and current_player <=28 and current_player <= total_candies:
              total_candies -= current_player
              moves_count += 1
              print(f'игрок {first} взял {current_player} конфет(ы), на столе осталось {total_candies} конфет')
              if total_candies == 0:
                  print(f'игрок {first} одержал победу')
              break
          elif (current_player <= 0 or current_player > 28) and current_player <= total_candies:
              print(f'нужно взять более 0, но не более 28 конфет' )
          else:
              print(f'осталось только {total_candies} конфет')
      except:
          print("количество конфет должно быть числом")
