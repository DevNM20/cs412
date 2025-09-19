# File: views.py
# Author: Nathan Moges (bmoges18@bu.edu) 9/19/2025
# Description: This file views.py has four function show_main, 
#submit_order, confirmation, and calculate_time which displays 
#the indivudal main and order pages. 

from django.shortcuts import render
from django.http import HttpResponse
import random
import time 


def show_main(request):
    '''Directs the application to display the main.html.'''

    template_name = "restaurant/main.html"
    return render(request, template_name)

def submit_order(request):
    """Displays the order page"""
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
    """The helper function calculate_time calculates the readytime by 
    randomizing a number from 30-60 minutes and adding it to the current time"""

    current_time = time.time()
    random_time_in_sec = random.randint(30, 60) * 60
    readytime_in_sec = current_time + random_time_in_sec
    readytime = time.strftime("%H:%M:%S %p", time.localtime(readytime_in_sec))
    return readytime    



def confirmation(request) :
    """Confirmation function takes in the info of the customer and reposts it on the confirmation.html page
    It does this by splitting the name from the input attribute in the html file which holds the name and price of every item in the menu
    Then I convert that value into a float and add it into a an empty variable called total. With the name 
    variable I added it into an empty list and both selected_items and
    total gets returned."""
    if request.POST:
        total = 0
        selected_items = []
        combo_items = request.POST.getlist("combo")

        for items in combo_items:
            name, price = items.split(',')
            total += float(price)
            selected_items.append(name) 

        template_name = "restaurant/confirmation.html"

        name = request.POST['name'] #customer info
        phone_number = request.POST['phone_number']
        email = request.POST['email']

        pancakes = request.POST.get('pancakes') #items on the menu
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





