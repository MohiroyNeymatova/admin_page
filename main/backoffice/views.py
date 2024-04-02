from django.shortcuts import render, redirect
from main.models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            usr = authenticate(username=username, password=password)
            if usr is not None:
                login(request, usr)
                return redirect('index')
            else:
                messages.warning(request, 'Username or password is wrong')
        else:
            print('ssssssssssss')
            messages.warning(request, 'No user found')
            return redirect('login')
    return render(request, 'backoffice/sign-in.html')


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def index(request):
    user = request.user
    context = {
        'infos': Info.objects.all().count(),
        'banners': MainBanner.objects.all().count(),
        'portfolio': Portfolio.objects.all().count(),
        'reviews': Testimonial.objects.all().count(),
        'services': Service.objects.all().count(),
        'messages': Message.objects.all().count(),
        'abouts': About.objects.all().count(),
        'clients': Client.objects.all().count()

    }
    return render(request, 'backoffice/index.html', context)


@login_required(login_url='login')
def settings(request):
    if request.method == "POST":
        user = request.user
        username = request.POST.get("username")
        password = request.POST.get("password")
        if User.objects.exclude(id=user.id).filter(username=username).exists():
            messages.warning(request, 'This username is busy!')
            return redirect('settings')
        user.username = username
        if password != "":
            user.set_password(password)
        user.save()
        login(request, user)
        return redirect('settings')
    return render(request, 'backoffice/settings.html')


@login_required(login_url='login')
def info_view(request):
    context = {
        "infos": Info.objects.all().order_by('-id')
    }
    return render(request, 'backoffice/info.html', context)


@login_required(login_url='login')
def create_info(request):
    if request.method == 'POST':
        Info.objects.create(
            logo=request.FILES.get('logo'),
            address=request.POST.get('address'),
            tw=request.POST.get('tw'),
            insta=request.POST.get('insta'),
            fb=request.POST.get('fb'),
            ln=request.POST.get('ln')
        )
        return redirect('info')
    return render(request, 'backoffice/create_info.html')


@login_required(login_url='login')
def update_info(request, pk):
    info = Info.objects.get(id=pk)
    if request.method == 'POST':
        if request.FILES.get('logo'):
            info.logo = request.FILES.get('logo')
        info.address = request.POST.get('address')
        info.tw = request.POST.get('tw')
        info.fb = request.POST.get('fb')
        info.insta = request.POST.get('insta')
        info.ln = request.POST.get('ln')
        info.save()
        return redirect('info')
    context = {
        'info': info
    }
    return render(request, 'backoffice/update_info.html', context)


@login_required(login_url='login')
def delete_info(request, pk):
    Info.objects.get(id=pk).delete()
    return redirect('info')


@login_required(login_url='login')
def main_banner_view(request):
    context = {
        "main_banners": MainBanner.objects.all().order_by('-id')
    }
    return render(request, 'backoffice/main_banner.html', context)


@login_required(login_url='login')
def create_main_banner(request):
    if request.method == 'POST':
        MainBanner.objects.create(
            image=request.FILES.get('image'),
            title=request.POST.get('title'),
            text=request.POST.get('text')
        )
        return redirect('main_banner')
    return render(request, 'backoffice/create_main_banner.html')


@login_required(login_url='login')
def update_main_banner(request, pk):
    banner = MainBanner.objects.get(id=pk)
    if request.method == 'POST':
        if request.FILES.get('image'):
            banner.image = request.FILES.get('image')
        banner.title = request.POST.get('title')
        banner.text = request.POST.get('text')
        banner.save()
        return redirect('main_banner')
    context = {
        "main_banner": banner
    }
    return render(request, 'backoffice/update_main_banner.html', context)


@login_required(login_url='login')
def delete_main_banner(request, pk):
    MainBanner.objects.get(id=pk).delete()
    return redirect('main_banner')


@login_required(login_url='login')
def services_view(request):
    context = {
        "services": Service.objects.all().order_by('-id')
    }
    return render(request, 'backoffice/services.html', context)


@login_required(login_url='login')
def create_service(request):
    if request.method == 'POST':
        Service.objects.create(
            icon=request.FILES.get('icon'),
            title=request.POST.get('title'),
            text=request.POST.get('text')
        )
        return redirect('services')
    return render(request, 'backoffice/create_service.html')


@login_required(login_url='login')
def update_service(request, pk):
    service = Service.objects.get(id=pk)
    if request.method == 'POST':
        if request.FILES.get('icon'):
            service.icon = request.FILES.get('icon')
        service.title = request.POST.get('title')
        service.text = request.POST.get('text')
        service.save()
        return redirect('services')
    context = {
        "service": service
    }
    return render(request, 'backoffice/update_service.html', context)


@login_required(login_url='login')
def delete_service(request, pk):
    Service.objects.get(id=pk).delete()
    return redirect('services')


@login_required(login_url='login')
def about_view(request):
    context = {
        "abouts": About.objects.all().order_by('-id')
    }
    return render(request, 'backoffice/about.html', context)


@login_required(login_url='login')
def create_about(request):
    if request.method == 'POST':
        About.objects.create(
            photo=request.FILES.get('photo'),
            text1=request.POST.get('text1'),
            text2=request.POST.get('text2')
        )
        return redirect('about')
    return render(request, 'backoffice/create_about.html')


@login_required(login_url='login')
def update_about(request, pk):
    about = About.objects.get(id=pk)
    if request.method == 'POST':
        if request.FILES.get('photo'):
            about.photo = request.FILES.get('photo')
        about.text1 = request.POST.get('text1')
        about.text2 = request.POST.get('text2')
        about.save()
        return redirect('about')
    context = {
        "about": about
    }
    return render(request, 'backoffice/update_about.html', context)


@login_required(login_url='login')
def delete_about(request, pk):
    About.objects.get(id=pk).delete()
    return redirect('about')


@login_required(login_url='login')
def portfolio_view(request):
    context = {
        "portfolio": Portfolio.objects.all().order_by('-id')
    }
    return render(request, 'backoffice/portfolio.html', context)


@login_required(login_url='login')
def create_portfolio(request):
    if request.method == 'POST':
        Portfolio.objects.create(
            image=request.FILES.get('image')
        )
        return redirect('portfolio')
    return render(request, 'backoffice/create_portfolio.html')


@login_required(login_url='login')
def update_portfolio(request, pk):
    portfolio = Portfolio.objects.get(id=pk)
    if request.method == 'POST':
        portfolio.image = request.FILES.get('image')
        portfolio.save()
        return redirect('portfolio')
    context = {
        "portfolio": portfolio
    }
    return render(request, 'backoffice/update_portfolio.html', context)


@login_required(login_url='login')
def delete_portfolio(request, pk):
    Portfolio.objects.get(id=pk).delete()
    return redirect('portfolio')


@login_required(login_url='login')
def testimonials_view(request):
    context = {
        "testimonials": Testimonial.objects.all().order_by('-id')
    }
    return render(request, 'backoffice/testimonials.html', context)


@login_required(login_url='login')
def create_testimonial(request):
    if request.method == 'POST':
        Testimonial.objects.create(
            review=request.POST.get('review'),
            name=request.POST.get('name')
        )
        return redirect('testimonials')
    return render(request, 'backoffice/create_testimonial.html')


@login_required(login_url='login')
def update_testimonial(request, pk):
    testimonial = Testimonial.objects.get(id=pk)
    if request.method == 'POST':
        testimonial.review = request.POST.get('review')
        testimonial.name = request.POST.get('name')
        testimonial.save()
        return redirect('testimonials')
    context = {
        "testimonial": testimonial
    }
    return render(request, 'backoffice/update_testimonial.html', context)


@login_required(login_url='login')
def delete_testimonial(request, pk):
    Testimonial.objects.get(id=pk).delete()
    return redirect('testimonials')


@login_required(login_url='login')
def clients_view(request):
    context = {
        "clients": Client.objects.all().order_by('-id')
    }
    return render(request, 'backoffice/clients.html', context)


@login_required(login_url='login')
def create_client(request):
    if request.method == 'POST':
        Client.objects.create(
            logo=request.FILES.get('logo')
        )
        return redirect('clients')
    return render(request, 'backoffice/create_client.html')


@login_required(login_url='login')
def update_client(request, pk):
    client = Client.objects.get(id=pk)
    if request.method == 'POST':
        client.logo = request.FILES.get('logo')
        client.save()
        return redirect('clients')
    context = {
        "client": client
    }
    return render(request, 'backoffice/update_client.html', context)


@login_required(login_url='login')
def delete_client(request, pk):
    Client.objects.get(id=pk).delete()
    return redirect('clients')


@login_required(login_url='login')
def messages_view(request):
    context = {
        "messages": Message.objects.all().order_by('-id')
    }
    return render(request, 'backoffice/messages.html', context)


@login_required(login_url='login')
def delete_message(request, pk):
    Message.objects.get(id=pk).delete()
    return redirect('messages')


@login_required(login_url='login')
def message_details(request, pk):
    context = {
        'message': Message.objects.get(id=pk)
    }
    return render(request, 'backoffice/message_details.html', context)


def page_not_found_view(request, exception):
    return render(request, 'backoffice/error.html')
