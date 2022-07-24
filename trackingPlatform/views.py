from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Lot
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def check_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        chk_user = authenticate(request, username=username, password=password)
        if chk_user is None:
            messages.success(request, "Username or password is incorrect, please try again.")
            return redirect('login')
        else:
            login(request, chk_user)
            return redirect('home')
    else:
        return render(request, 'trackingPlatform/login.html')


def home(request):
    search = request.POST.get('search')
    if request.user.is_authenticated:
        if search == '' or search is None:
            lots_obj = Lot.objects.all()
            paginator = Paginator(lots_obj, 5)
            page = request.GET.get('page')
            try:
                lots = paginator.page(page)
            except PageNotAnInteger:
                lots = paginator.page(1)
            except EmptyPage:
                lots = paginator.page(paginator.num_pages)

        else:
            lots_obj = Lot.objects.filter(track_code=search)
            paginator = Paginator(lots_obj, 1)
            page = 1
            lots = paginator.page(page)
        return render(request, 'trackingPlatform/home.html', {'lots': lots, 'page': page})
    return render(request, 'trackingPlatform/login.html')


def new_user(request):
    if request.method == 'POST':
        User.objects.create_user(username=request.POST.get('username'),
                                 email=request.POST.get('email'),
                                 password=request.POST.get('password'))
        return redirect('login')
    return render(request, 'trackingPlatform/register_user.html')


def new_lot(request):
    if request.method == 'POST':
        lot = Lot()
        lot.product_name = request.POST.get('product_name')
        lot.created_by = request.user
        lot.description = request.POST.get('description')
        lot.track_code = request.POST.get('track_code')
        txId = lot.writeOnChain()
        lot.txId = txId
        lot.save()
        return redirect('home')

    return render(request, 'trackingPlatform/new_lot.html', {})


def lot_details(request, pk):
    lot = get_object_or_404(Lot, pk=pk)
    return render(request, 'trackingPlatform/lot_details.html', {'lot': lot})
