#   Моделирование работы сети кафе с несколькими столиками и потоком посетителей, прибывающих для заказа пищи
# и уходящих после завершения приема.
#
#   Есть сеть кафе с несколькими столиками. Посетители приходят, заказывают еду, занимают столик,
# употребляют еду и уходят. Если столик свободен, новый посетитель принимается к обслуживанию, иначе он
# становится в очередь на ожидание.
#
# Создайте 3 класса:
#   Table - класс для столов, который будет содержать следующие атрибуты: table_number(int) - номер стола,
# is_busy(bool) - занят стол или нет.
#
#   Cafe - класс для симуляции процессов в кафе. Должен содержать следующие атрибуты и методы:
#   Атрибуты queue - очередь посетителей (создаётся внутри init), tables список столов (поступает из вне).
#   Метод customer_arrival(self) - моделирует приход посетителя(каждую секунду).
#   Метод serve_customer(self, customer) - моделирует обслуживание посетителя. Проверяет наличие свободных столов,
# в случае наличия стола - начинает обслуживание посетителя (запуск потока), в противном случае - посетитель
# поступает в очередь. Время обслуживания 5 секунд.
#   Customer - класс (поток) посетителя. Запускается, если есть свободные столы.
#
# Так же должны выводиться текстовые сообщения соответствующие событиям:
#   Посетитель номер <номер посетителя> прибыл.
#   Посетитель номер <номер посетителя> сел за стол <номер стола>. (начало обслуживания)
#   Посетитель номер <номер посетителя> покушал и ушёл. (конец обслуживания)
#   Посетитель номер <номер посетителя> ожидает свободный стол. (помещение в очередь)

import threading
import time
import queue


class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False


class Cafe:
    def __init__(self, tables):
        self.queue = queue.Queue()
        self.tables = tables

    def customer_arrival(self):
        for i in range(20):
            time.sleep(1)
            customer = Customer(i + 1, self)
            self.queue.put(customer.number)
            customer.start()

    def serve_customer(self, customer):
        for table in self.tables:
            if not table.is_busy:
                iz_ocheredi = self.queue.get(customer.number)
                table.is_busy = True
                print(f"Посетитель {iz_ocheredi} сел за стол {table.number}", flush=True)
                time.sleep(5)
                print(f"Посетитель {iz_ocheredi} покушал и ушёл.", flush=True)
                table.is_busy = False
                return
        print(f'Посетитель {customer.number} ожидает свободный стол.', flush=True)


class Customer(threading.Thread):
    def __init__(self, number, cafe):
        threading.Thread.__init__(self)
        self.number = number
        self.cafe = cafe

    def run(self):
        print(f"Посетитель номер {self.number} прибыл")
        self.cafe.serve_customer(self)


if __name__ == "__main__":
    tables = [Table(i+1) for i in range(3)]
    cafe = Cafe(tables)
    cafe.customer_arrival()
