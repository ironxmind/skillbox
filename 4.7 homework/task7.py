print('Задача 7. Поездка по кругу')

# Вася решил потренироваться перед марафоном и покататься вокруг Москвы на скорость.
# Длина дороги — 115 километров.
# Вася стартует с нулевого километра и едет со скоростью v километров в час. 
# На какой отметке он остановится через t часов?
# 
# Реализуйте программу, 
# которая спрашивает у пользователя v и t,
# и выводит целое число от 0 до 114 — номер километра, на котором остановится Вася.
# Учтите, что он может прокатиться больше одного круга.
v, t = int(input('Введите скорость велосипедиста: ')), int(input('Введите время остановки: '))
long = 115
dist = (v / t) % long
print('Текущий километр дистанции: ', dist)