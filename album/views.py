from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt

def photo(request):
    return render(request, 'photo.html')

def image_today(request):
    date = dt.date.today()
    return render(request, 'images/today-image.html', {"date": date,})

def convert_dates(dates):
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    day = days[day_number]
    return day

def past_days_image(request,past_date):
    try:
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(image_of_day)

    return render(request, 'images/past-image.html', {"date": date})