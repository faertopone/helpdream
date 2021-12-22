from django.core.exceptions import PermissionDenied
from typing import Callable
import functools
import time
import math

#
# # Декоратор класса
#
# def CountCalls(cls):
#     """
#        Декоратор класса. который имеет счетчик вызова функции и за счет этого , сможем на какое то количство раз вызова делать едйствие например хадержку 10 сек на каждый 5тый вызов
#        """
#
#     # Ставим счетчик 0
#     cls.num_calls = 0
#
#     @functools.wraps(cls)
#     def wrapper(*args, **kwargs):
#         cls.num_calls += 1
#         instance = cls(*args, **kwargs)
#         if cls.num_calls == 1:
#             time.sleep(20)
#             cls.num_calls = 0
#         return instance
#
#     return wrapper


class DelayIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.count_call = 0
        self.count_ip = 0
        self.start_time = time.time()
        self.end_time = 0

    def __call__(self, request):
        # Каждый запрос на открытие страницы будем увеличивать счетчик
        self.count_call += 1

        # сколько раз с 1 IP выполнили запрос
        number_counts = 5
        # Время за которое счиитаь запросы sec
        time_number = 10

        self.end_time = time.time()
        result_end = time.localtime(self.end_time)
        result_start = time.localtime(self.start_time)
        print(result_end.tm_sec, ' - сумма времени при вызове')
        print(result_start.tm_sec, ' - время начальное')
        print(time.time(), ' - время тайм при запросы')
        #Прошедшее время
        range_time = abs(result_end.tm_sec - result_start.tm_sec)
        print(range_time, ' - Прошедшее время')

        allow_ips = ["127.0.0.1"]
        ip = request.META.get('REMOTE_ADDR')
        if ip in allow_ips:
            self.count_ip += 1
        #Если number_counts выполнили запрос с IP ["127.0.0.1"] то выдаст ошибку и обнулим счетчик
        # если прошло более 10 сек
        print(range_time)
        print(self.count_ip, 'Сколько раз сделали вызов ')
        if range_time >= time_number:
            # если за это время запросов с одного IP превысило number_counts, то выдадим ерор 403
            if self.count_ip >= number_counts:
                self.count_ip = 0
                self.start_time = time.time()
                self.end_time = 0
                raise PermissionDenied
            self.count_ip = 0
            self.start_time = time.time()
            self.end_time = 0


        #Каждый пятый запрос будет выдовать 403 ошибку
        if self.count_call == 5:
            self.count_call = 0
            raise PermissionDenied

        # Каждый 7 запрос будет задержка 7 сек
        if self.count_call == 7:
            time.sleep(10)
            self.count_call = 0

        time_world = time.localtime()  # get struct_time
        time_string = time.strftime("%m/%d/%Y, %H:%M:%S", time_world)
        print(time_string, " Время запроса")

        response = self.get_response(request)

        return response