from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt

def photo(request):
    return render(request, 'photo.html')

def image_of_day(request):
    date = dt.date.today()

    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1> Image for {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)

def convert_dates(dates):
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    day = days[day_number]
    return day
