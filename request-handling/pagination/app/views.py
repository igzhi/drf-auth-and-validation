from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from csv import DictReader
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from app.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    with open(BUS_STATION_CSV, encoding='cp1251') as f:
        csv_data = DictReader(f)
        stations = []
        for station in csv_data:
            stations.append(
                {
                    'Name': station['Name'],
                    'Street': station['Street'],
                    'District': station['District']
                }
            )
    paginator = Paginator(stations, 10)
    page = request.GET.get('page')

    try:
        get_station = paginator.page(page)
    except PageNotAnInteger:
        get_station = paginator.page(1)
    except EmptyPage:
        get_station = paginator.page(paginator.num_pages)

    if get_station.number == 1:
        prev_page_url = None
    else:
        prev_page_url = f'?page={get_station.previous_page_number()}'

    next_page_url = f'?page={get_station.next_page_number()}'


    return render_to_response('index.html', context={
        'bus_stations': get_station,
        'current_page': 1,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })

