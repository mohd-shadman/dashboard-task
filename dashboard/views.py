from django.http import JsonResponse
from django.shortcuts import render
from dashboard.models import DataEntry

def dashboard_view(request):
    data_entries = DataEntry.objects.all()
    context = {
        'data_entries': data_entries,
    }
    return render(request, 'dashboard.html', context)

def dashboard_data(request):
    data_entries = DataEntry.objects.all()
    data = list(data_entries.values('end_year', 'intensity', 'sector', 'topic', 'impact', 'added', 'title', 'region', 'relevance', 'likelihood', 'source', 'url'))
    return JsonResponse(data, safe=False)
