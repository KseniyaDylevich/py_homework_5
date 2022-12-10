import random

first = random.randrange(1, 3)

if first == 1:
  second = 2
else:
  second = 1

total_candies = 2017

print(f'на столе всего конфет: {total_candies}')
print(f'игру начинает игрок {first}')
while total_candies > 0:

  while True:
      try:
          first_player = int(input(f'сколько конфет возьмет игрок {first}: '))
          if first_player > 0 and first_player <=28 and first_player <= total_candies:
              total_candies -= first_player
              print(f'игрок {first} взял {first_player} конфет(ы), на столе осталось {total_candies} конфет')
              if total_candies == 0:
                  print(f'игрок {first} одержал победу')
              break
          elif (first_player <= 0 or first_player > 28) and first_player <= total_candies:
              print(f'нужно взять более 0, но не более 28 конфет' )
          else:
              print(f'осталось только {total_candies} конфет')
      except:
          print("количество конфет должно быть числом")

  if total_candies == 0:
    break

  while True:
      try:
          second_player = int(input(f'сколько конфет возьмет игрок {second}: '))
          if second_player > 0 and second_player <=28 and second_player <= total_candies:
              total_candies -= second_player
              print(f'игрок {second} взял {second_player} конфет(ы), на столе осталось {total_candies} конфет')
              if total_candies == 0:
                  print(f'игрок {second} одержал победу')
              break
          elif (second_player <= 0 or second_player > 28) and second_player <= total_candies:
              print(f'нужно взять более 0, но не более 28 конфет' )
          else:
              print(f'осталось только {total_candies} конфет')
      except:
          print("количество конфет должно быть числом")