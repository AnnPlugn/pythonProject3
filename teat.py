from datetime import datetime


def brth_days_count(strok):
    brth = strok

    # Разбиваем строку на отдельные части
    day, month, year = map(int, brth.split(':'))

    # Создаем объект datetime
    birthday = datetime(year=year, month=month, day=day)
    # Текущая дата
    today = datetime.now()

    # Вычисляем разницу между текущей датой и днем рождения
    days_since_birthday = str((today - birthday).days)

    print(f"Со дня вашего рождения прошло {days_since_birthday} дней")
    return days_since_birthday

print(brth_days_count('13:08:2005'))