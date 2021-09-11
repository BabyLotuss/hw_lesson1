duration = int(input('Введите кол-во секунд: '))
MINUTE = 60
HOUR = 3600
DAY = 86400

if duration < MINUTE:
    print(duration, 'сек')
elif MINUTE <= duration < HOUR:
    print(duration // MINUTE, 'мин', duration % MINUTE, 'сек')
elif HOUR <= duration < DAY:
    print(duration // HOUR, 'час', duration % HOUR // MINUTE, 'мин', duration % MINUTE, 'сек')
elif duration > DAY:
    print(duration // DAY, 'дн', duration % DAY // HOUR, 'час', duration % HOUR // MINUTE, 'мин', duration % MINUTE,
          'сек')