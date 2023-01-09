from datetime import datetime, timedelta

def change_day(cur_year_bd):

    if cur_year_bd.weekday() == 5:
        cur_year_bd = cur_year_bd.replace(day=cur_year_bd.day + 2)    # добавляет 2д к дате если Сб
    if cur_year_bd.weekday() == 6:
        cur_year_bd = cur_year_bd.replace(day=cur_year_bd.day + 1)    # добавляет 1д к дате если Вс
    return cur_year_bd

def get_birthdays_per_week(users, n):

    upcoming_bd = {}
    end_day = datetime.now().date() + timedelta(days=n)
    delta = end_day - datetime.now().date()
    period_bd = [datetime.now().date() + timedelta(days=i) for i in range(delta.days)]
    for user in users:
        user_bd = datetime.strptime(user["birthdate"], "%Y-%m-%d").date()   # перевод др(str) в др(datetime)
        cur_year_bd = user_bd.replace(year=datetime.now().year)    # присвоение др настоящего года
        user["birthdate"] = cur_year_bd

        if user["birthdate"] in period_bd: # если др попадает в заданній период n
            cur_year_bd = change_day(cur_year_bd)
            if not upcoming_bd.get(cur_year_bd):
                upcoming_bd[cur_year_bd] = [user["name"]]
            else:
                upcoming_bd[cur_year_bd].append(user["name"])
    for k, v in upcoming_bd.items():  # печатает кого нужно поздравить
        print(f'{k.strftime("%A")} : {", ".join(v)}')


if __name__ == "__main__":

    n = 7
    get_birthdays_per_week(users, n)

# users = [
#     {"name": "Bill", "birthdate": "1990-01-15"},
#     {"name": "Gill", "birthdate": "1990-01-08"},
#     {"name": "Till", "birthdate": "1990-01-15"},
#     {"name": "Dill", "birthdate": "1990-01-09"},
#     {"name": "Bilg", "birthdate": "1990-01-12"},
#     {"name": "Gilg", "birthdate": "1990-01-16"},
#     {"name": "Tilg", "birthdate": "1990-01-08"},
#     {"name": "Tilm", "birthdate": "1990-01-10"},
#     {"name": "Diig", "birthdate": "1990-01-07"},
#     {"name": "Digg", "birthdate": "1990-01-09"},
# ]
