from django.shortcuts import render, get_object_or_404, redirect
from .models import Car, CarImage, Profile, Message, Order
from .forms import UserRegistrationForm, MessageForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login
from django.db.models import Q

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            Profile.objects.create(
                user=user, 
                role=form.cleaned_data['role']
            )
            login(request, user)
            return redirect('cars:car_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def car_list(request):
    cars = Car.objects.filter(is_validated=True)
    
    brand = request.GET.get('brand')
    fuel_type = request.GET.get('fuel_type')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    min_year = request.GET.get('min_year')

    if brand:
        cars = cars.filter(brand__icontains=brand)
    if fuel_type:
        cars = cars.filter(fuel_type=fuel_type)
    if min_price:
        cars = cars.filter(price__gte=min_price)
    if max_price:
        cars = cars.filter(price__lte=max_price)
    if min_year:
        cars = cars.filter(year__gte=min_year)

    return render(request, 'cars/car_list.html', {'cars': cars})

def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'cars/car_detail.html', {'car': car})

@login_required
def car_create(request):
    if request.method == "POST":
        car = Car.objects.create(
            seller=request.user,
            brand=request.POST.get('brand'),
            model=request.POST.get('model'),
            year=request.POST.get('year'),
            price=request.POST.get('price'),
            mileage=request.POST.get('mileage'),
            fuel_type=request.POST.get('fuel_type'),
            description=request.POST.get('description')
        )
        for img in request.FILES.getlist('images'):
            CarImage.objects.create(car=car, image=img)
        return redirect('cars:seller_dashboard')
    return render(request, 'cars/car_form.html')

@login_required
def inbox(request):
    messages = Message.objects.filter(Q(receiver=request.user) | Q(sender=request.user)).order_by('-timestamp')
    return render(request, 'cars/inbox.html', {'messages': messages})

@login_required
def send_message(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.receiver = car.seller
            message.car = car
            message.save()
            return redirect('cars:inbox')
    else:
        form = MessageForm()
    return render(request, 'cars/send_message.html', {'form': form, 'car': car})

@login_required
def place_order(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if car.seller != request.user:
        Order.objects.get_or_create(buyer=request.user, car=car, status='pending')
    return redirect('cars:my_orders')

@login_required
def my_orders(request):
    orders = Order.objects.filter(buyer=request.user).order_by('-created_at')
    return render(request, 'cars/my_orders.html', {'orders': orders})

@login_required
def seller_dashboard(request):
    my_cars = Car.objects.filter(seller=request.user)
    received_orders = Order.objects.filter(car__seller=request.user).order_by('-created_at')
    return render(request, 'cars/seller_dashboard.html', {
        'my_cars': my_cars,
        'received_orders': received_orders
    })

@user_passes_test(lambda u: u.is_staff)
def admin_dashboard(request):
    pending_cars = Car.objects.filter(is_validated=False)
    return render(request, 'cars/admin_dashboard.html', {'pending_cars': pending_cars})

@user_passes_test(lambda u: u.is_staff)
def validate_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    car.is_validated = True
    car.save()
    return redirect('cars:admin_dashboard')
