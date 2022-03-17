from django.core.exceptions import PermissionDenied
import time
import os
from django.urls import path, include

from datetime import datetime, date, time, timedelta

from app_helpdream.models import WriteDeam, Profile, TotalBoxDream




class TimedeltaDays:

    def __init__(self, get_response):
        self.get_response = get_response
        self.date = datetime.now()
        self.count = 0

        #Созаддим нашу базу
        if not TotalBoxDream.objects.filter(id=1).exists():
            TotalBoxDream.objects.create(balance=0)


    def __call__(self, request):
        # записывает дату в формате день, месяц, год  часы минут секунды (29.08.2021 01:11:10)
        dt_now = datetime.now()
        old_time = self.date
        dt_now_str = dt_now.strftime("%d/%m/%y")
        dt_now_obj = datetime.strptime(dt_now_str, "%d/%m/%y")

        #обновлять данные 1 раз в день
        if (dt_now_str != old_time.strftime("%d/%m/%y")) or (self.count == 0):
            self.count = 1
            self.date = dt_now
            dreams = WriteDeam.objects.select_related('who_dream').all()
            profiles = Profile.objects.select_related('user').all()

            # обновления сроков размещения
            for i_dr in dreams:
                end_dt_time_str = i_dr.creadet_at_dream_time.strftime("%d/%m/%y")
                end_dt_time_obj = datetime.strptime(end_dt_time_str, "%d/%m/%y")
                delta_time = end_dt_time_obj - dt_now_obj
                delta_time = delta_time.days.real
                i_dr.days_end = delta_time
                if delta_time <= 0:
                    i_dr.dream_is_active = False
                    i_dr.dream_is_complete = True
                    i_dr.days_end = 0

                i_dr.save()

            # обновления возраста профилей
            for i_age in profiles:
                # обновляем даты, там где они внесены
                if i_age.birthday:
                    delta_age = dt_now.year.real - i_age.birthday.year
                    i_age.age = delta_age
                    i_age.save()


        response = self.get_response(request)

        return response