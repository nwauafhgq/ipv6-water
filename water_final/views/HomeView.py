from django.contrib.auth.decorators import login_required
from django.shortcuts import render

fertilizer_de = []

@login_required(login_url='/login')
def index(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    return render(request, 'water_final/index.html', context={"username": username})


@login_required(login_url='/login')
def knowledge(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    return render(request, 'water_final/knowledge.html', context={"username": username})


@login_required(login_url='/login')
def devicecontrol(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    return render(request, 'water_final/device.html', context={"username": username})


@login_required(login_url='/login')
def irrigation_area(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    return render(request, 'water_final/irrigation_area.html', context={"username": username})


@login_required(login_url='/login')
def info(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    return render(request, 'water_final/info.html', context={"username": username})


@login_required(login_url='/login')
def fertilizer(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    if request.method == 'POST' and request.GET.get('action') == 'add_plan':
        fertilizer_de.append({})
        fertilizer_de[-1]['name'] = request.POST.get('name')
        fertilizer_de[-1]['time'] = request.POST.get('time')
        fertilizer_de[-1]['start'] = request.POST.get('start')
        fertilizer_de[-1]['end'] = request.POST.get('end')
        fertilizer_de[-1]['dan'] = request.POST.get('dan')
        fertilizer_de[-1]['lin'] = request.POST.get('lin')
        fertilizer_de[-1]['jia'] = request.POST.get('jia')
        fertilizer_de[-1]['wei'] = request.POST.get('wei')
        fertilizer_de[-1]['total'] = request.POST.get('total')
    elif request.method == 'POST' and request.GET.get('action') == 'delete_plan':
        fertilizer_de.pop(int(request.POST.get('index')))

    return render(request, 'water_final/fertilizer.html',
                      context={"username": username, "fertilizer_de": fertilizer_de})


@login_required(login_url='/login')
def auto(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    return render(request, 'water_final/auto.html', context={"username": username})


@login_required(login_url='/login')
def alerts(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    return render(request, 'water_final/alerts.html', context={"username": username})


@login_required(login_url='/login')
def data(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    return render(request, 'water_final/data.html', context={"username": username})
