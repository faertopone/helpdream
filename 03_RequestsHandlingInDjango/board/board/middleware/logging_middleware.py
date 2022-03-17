from django.core.exceptions import PermissionDenied
import time
import os
from datetime import datetime, date, time



class LogginsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Созадим папку, где будем хранить наши логи, и добавим эту папку в гит игнор)
        if not os.path.isdir("history_log"):
            os.mkdir("history_log")

    def __call__(self, request):
        # записывает дату в формате  день, месяц, год  часы минут секунды (29.08.2021 01:11:10)
        dt_now = datetime.today().strftime("%d.%m.%Y %H:%M:%S")
        method_request = request.META.get('REQUEST_METHOD')
        data_request = request.META.get('REMOTE_ADDR')
        url_request = request.META.get('PATH_INFO')
        url_host = request.META.get('HTTP_HOST')
        full_url = url_host + url_request

        string_full_info = 'Дата и время: ' + dt_now + '\n' + 'Ip-adress:' + data_request + '\n' + 'Метод: ' + method_request + '\n' + 'URL страницы :' + full_url




        with open('history_log/loggins_data.txt', 'a', encoding='utf-8') as file:
            file.write(string_full_info)
            file.write('\n\n')

        response = self.get_response(request)

        return response