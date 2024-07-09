import queue
import random
import time

# Створити чергу заявок
request_queue = queue.Queue()

# Ідентифікатор заявок
request_id = 0

def generate_request():
    global request_id
    request_id += 1
    request = f"Заявка #{request_id}"
    request_queue.put(request)
    print(f"Створено {request}")

def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        print(f"Обробляється {request}")
        # Імітація обробки заявки
        time.sleep(random.uniform(0.5, 2.0))
        print(f"Заявка {request} оброблена")
    else:
        print("Черга пуста, немає заявок для обробки")

def main():
    try:
        while True:
            # Генерація нових заявок
            # 70% ймовірність створення нової заявки, для змоги перевірки обробки порожньої черги
            if random.random() < 0.7:
                generate_request()
            # Обробка заявок
            process_request()
            # Чекаємо перед наступною ітерацією
            time.sleep(1)
    except KeyboardInterrupt:
        print("Завершення програми...")

if __name__ == "__main__":
    main()