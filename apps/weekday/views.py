from datetime import date

from django.http import HttpResponse
from django.views import View

WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


class WeekdayView(View):
    def get(self, request):
        # weekday() 0 is monday
        today = WEEKDAYS[date.today().weekday()]
        return HttpResponse(f'Today is {today}')
