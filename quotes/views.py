from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

import time
import random

IMAGES = [
    "https://i.pinimg.com/736x/3b/9d/50/3b9d50a32ed833d9cdc73978e98c8fc2.jpg",
    "https://images4.alphacoders.com/135/1352902.jpeg",
    "https://media.tenor.com/qg8lImmxa_sAAAAe/one-piece-monkey-d-luffy.png",
    "https://miro.medium.com/v2/resize:fit:1400/format:webp/1*YqfVlyCe06DfcPsR3kpYrw.jpeg",

    

]

QUOTES = [
    "Without You, I Won’t… I Can’t Become The Pirate King!!!",
    "Are We Friends? Or Are We Foes? That’s The Kind Of Thing You Decide For Yourselves!",
    "If You Hurt Somebody… Or If Somebody Hurts You, The Blood That Flows Is Still Red.",
    "If You Don’t Take Risks, You Can’t Create A Future",
    "You Want To Keep Everyone From Dying? That’s Naive. It’s War. People Die.",
]
# Create your views here.

def home(request):
    return HttpResponse("412 project")

def home_page(request):
        '''Respond to the URL '', delegate work to a template.'''

        template_name = 'quotes/home.html'
        context = {
             "time": time.ctime(),
            "randomquote": random.choice(QUOTES),
            "randomimage": random.choice(IMAGES),
        }
        return render(request, template_name, context)
def show_all(request):
    '''Respond to the URL 'show_all', delegate work to a template.'''
    ""

    template_name = "quotes/show_all.html"
    context = {
         "time": time.ctime(),
        "totalquotes" : QUOTES,
        "totalimages" : IMAGES,
    }
    return render(request, template_name, context)

def about(request):
        '''Respond to the URL 'about', delegate work to a template.'''

        template_name = 'quotes/about.html'
        context = {
             "time": time.ctime(),
        }
        return render(request, template_name, context)