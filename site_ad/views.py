from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import Ad,  Category
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm,AuthenticationForm
from .forms import SearchForm, AdPlacementForm, RegistrationForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
def ad_detail(request, ad_id):
    ad = Ad.objects.get(id=ad_id)
    return render(request, 'ad_detail.html', {'ad': ad})

def ad_list(request):
    ads = Ad.objects.all().order_by('-added_date')
    paginator = Paginator(ads, 10)  # 10 ads per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'ad_list.html', {'page_obj': page_obj})
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Неправильное имя пользователя или пароль')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
def logout_view(request):
    logout(request)
    return render(request,'logout.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = form.cleaned_data['first_name']
            user.save()
            return redirect('registration_end')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def registration_end_view(request):
    return render(request, 'registration_end.html')

def search_view(request):
    query = request.GET.get('query', '')
    ads = Ad.objects.filter(Q(name__icontains=query))
    paginator = Paginator(ads, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'ad_list.html', {'page_obj': page_obj, 'query': query})
@login_required(login_url='/login/')
def create_ad(request):
    if request.method == 'POST':
        form = AdPlacementForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.seller = request.user
            ad.save()
            return redirect('ad_detail', ad_id=ad.id)
    else:
        form = AdPlacementForm()
    return render(request, 'create_ad.html', {'form': form})
def edit_ad(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)

    if request.user != ad.seller:
        # Redirect or show an error message indicating that the user doesn't have permission to edit this ad
        return redirect('ad_detail', ad_id=ad_id)

    if request.method == 'POST':
        form = AdPlacementForm(request.POST, request.FILES, instance=ad)
        if form.is_valid():
            form.save()
            # Redirect to the ad detail page after saving the changes
            return redirect('ad_detail', ad_id=ad_id)
    else:
        form = AdPlacementForm(instance=ad)  # Pass the ad instance to the form for pre-filling the fields

    return render(request, 'edit_ad.html', {'form': form})
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound

def delete_ad(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)

    if request.user == ad.seller:
        ad.delete()
        return HttpResponse(status=204)
    else:
        return HttpResponseBadRequest("You don't have permission to delete this ad.")
def categories(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})
def category_ads(request, category):
    if category == 'all':
        ads = Ad.objects.all().order_by('-added_date')
    else:
        ads = Ad.objects.filter(category__alias=category).order_by('-added_date')
    paginator = Paginator(ads, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'ad_list.html', {'page_obj': page_obj})