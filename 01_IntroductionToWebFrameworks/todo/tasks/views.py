from django.http import HttpResponse

from django.views import View

import random


class ToDoView(View):

    def get(self, request, *args, **kwargs):
        temp = ['<li>Установить python</li>',
                '<li>Установить django</li>',
                '<li>Запустить сервер</li>',
                '<li>Порадоваться результату</li>',
                '<li>Конец</li>']
        send_text = []
        for i in range(len(temp)):
            temp_1 = random.choice(temp)
            send_text.append(temp_1)
            temp.pop(temp.index(temp_1))
        send_text_last = '<ul>' + send_text[0] + send_text[1] + send_text[2] + send_text[3] + send_text[4] + '</ul>'

        return HttpResponse(send_text_last)
