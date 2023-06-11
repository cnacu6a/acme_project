import time


def time_of_function(func):
    def wrapper():
        start_time = time.time()
        print('Время пошло')
        result = func()
        execution_time = round(time.time() - start_time, 1)
        print(f'Через {execution_time} сек. функция вернула «{result}»')
        return result
    return wrapper


@time_of_function  # Декорируем!
def sleep_one_sec():
    time.sleep(1)
    return 'Результат первой функции'


sleep_one_sec()











from django.contrib.auth.decorators import login_required


# Встроенный в Django декоратор @login_required проверит пользователя
# и вернёт страницу только залогиненному пользователю.
# А незалогиненный будет отправлен на страницу логина.

@login_required  # Как можно не любить сахар!
def birthday_create(request):
    # Полезный код функции.
    ...
