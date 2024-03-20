from multiprocessing import Process, Manager, Lock


class WarehouseManager:

    def __init__(self):
        self.data = Manager().dict()
        self.lock = Lock()

    def run(self, requests):
        all_process = []
        for request in requests:
            process = Process(target=self.process_request, args=(request,))
            all_process.append(process)
            process.start()

        for process in all_process:
            process.join()

    def process_request(self, request):
        with self.lock:
            product, action, quantity = request
            if action == "receipt":
                if product in self.data:
                    self.data[product] += quantity
                else:
                    self.data[product] = quantity
            elif action == "shipment":
                if product in self.data and self.data[product] >= quantity:
                    self.data[product] -= quantity


if __name__ == '__main__':
    # Создаем менеджера склада
    manager = WarehouseManager()

    # Множество запросов на изменение данных о складских запасах
    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 40),
        ("product3", "receipt", 220),
        ("product2", "shipment", 60)
    ]

    # Запускаем обработку запросов
    manager.run(requests)

    # Выводим обновленные данные о складских запасах
    print(manager.data, flush=True)