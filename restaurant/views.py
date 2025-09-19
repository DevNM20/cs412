from django.shortcuts import render
from django.http import HttpResponse
import random
import time 
# Create your views here.
def show_main(request):
    '''Directs the application to display the main.html.'''

    template_name = "restaurant/main.html"
    return render(request, template_name)

def submit_order(request):

    template_name = "restaurant/order.html"
    specials = [
        {"name": "Meatball Pasta", "price": 12.99},
        {"name": "Rice and Beans", "price": 8.99},
        {"name": "Salad", "price": 4.99},
        {"name": "Fries", "price": 3.99},
    ]

    daily_special = random.choice(specials)


    context = {
        "daily_special" : daily_special
    }
    return render(request, template_name, context)

def calculate_time():
    current_time = time.time()
    random_time_in_sec = random.randint(30, 60) * 60
    readytime_in_sec = current_time + random_time_in_sec
    readytime = time.strftime("%H:%M:%S %p", time.localtime(readytime_in_sec))
    return readytime    


#Fix confirmation function
def confirmation(request) :
    if request.POST:
        total = 0
        selected_items = []
        combo_items = request.POST.getlist("combo")

        for items in combo_items:
            name, price = items.split(',')
            total += float(price)
            selected_items.append(name) 

        template_name = "restaurant/confirmation.html"

        name = request.POST['name']
        phone_number = request.POST['phone_number']
        email = request.POST['email']

        pancakes = request.POST.get('pancakes')
        frenchtoast = request.POST.get('frenchtoast')
        cereal = request.POST.get('cereal')
        eggs = request.POST.get('eggs')

        special_item = request.POST.get("special")
        if special_item:
            special_name, special_price = special_item.split(",")
            total += float(special_price)
            selected_items.append(special_name)

        context = {
            'name' : name,
            'phone_number' : phone_number,
            'email' : email,
            'pancake_price' : pancakes,
            'frenchtoast_price' : frenchtoast,
            'cereal_price' : cereal,
            'eggs_price' : eggs,
            'readytime' : calculate_time(),
            'total' : total,
            'selected_items' : selected_items,
            
        }
        return render(request, template_name, context)





