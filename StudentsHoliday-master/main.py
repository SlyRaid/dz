import csv

filecsv = r'D:\PyCharm\StudentsHoliday-master\travel-notes.csv'


def write_holiday_cities(first_letter):
    visited_cities = set()
    wish_list_cities = set()
    all_cities = set()

    with open(filecsv, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            name, visited, wish_list = row[0], row[1].split(';'), row[2].split(';')
            if name.startswith(first_letter):
                visited_cities.update(visited)
                wish_list_cities.update(wish_list)
                all_cities.update(visited)
                all_cities.update(wish_list)

    never_visited_cities = all_cities - visited_cities
    next_city = sorted(wish_list_cities)[0] if all_cities else None

    with open('holiday.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Посетили: '] + sorted(visited_cities))
        writer.writerow(['Хотят посетить: '] + sorted(wish_list_cities))
        writer.writerow(['Никогда не были в: '] + sorted(never_visited_cities))
        writer.writerow(['Следующим городом будет: '] + [next_city] if next_city else [])


write_holiday_cities('L')
