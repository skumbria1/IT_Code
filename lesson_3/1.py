from datetime import datetime
from calendar import monthrange


def print_current_date_and_temp(day: int, month: int, temp: int) -> None:
    if not isinstance(day, int):
        print('day must be int')
        return None
    if not isinstance(month, int):
        print('month must be int')
        return None
    if not isinstance(temp, int):
        print('temp must be int')
        return None
    if not (1 <= month <= 12):
        print('month must be valid')
        return None

    current_year: int = datetime.now().year
    if 0 < day <= monthrange(current_year, month)[1]:
        print(f'Сегодня {day}.{month}. На улице {temp} градусов.')
    else:
        print('day must be valid')
        return None
    if temp < 0:
        print('Холодно, лучше остаться дома')
    return None


if __name__ == '__main__':
    day: int = 1
    month: int = 1
    temperature: int = 0
    print_current_date_and_temp(day, month, temperature)

    day = -15
    print_current_date_and_temp(day, month, temperature)

    day = 31
    temperature = -5
    print_current_date_and_temp(day, month, temperature)
