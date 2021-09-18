from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

challenges = {
    "january": "Ron is an idiot in january",
    "february": "Ron is an idiot in february",
    "march": "Ron is an idiot in march",
    "april": "Ron is an idiot in april",
    "may": "Ron is an idiot in may",
    "june": "Ron is an idiot in june",
    "july": "Ron is an idiot in july",
    "august": "Ron is an idiot in august",
    "september": "Ron is an idiot in september",
    "october": "Ron is an idiot in october",
    "november": "Ron is an idiot in november",
    "december": "Ron is an idiot in december",

}

def index(request):
    list_items = ""
    months =list(challenges.keys())
    
    for month in months:
        month_path = reverse ("month-challenge" , args = [month])
        list_items += f"<li><a href =\'{month_path}\'>{month.capitalize()}</a></li> "
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month entry")
    forward_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[forward_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenges(request, month):
    try:
        challenge_text = challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)

    except:
        return HttpResponseNotFound("This month is not supported")
