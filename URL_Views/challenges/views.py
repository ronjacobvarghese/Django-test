from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
monthly_challenges = {
    "january": "This month is january",
    "febuary": "This month is febuary",
    "march": "This month is march",
    "july": "This month is july",
    "june": " This month is june",
    "august": "This month is august",
    "april": "This month is april",
    "may": "This month is may",
    "september": "This month is september",
    "october": "This month is october",
    "november": "This month is november",
    "december": None,
}


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid Month!!")

    redirect_month = months[month-1]
    redirect_path = reverse("monthly-challenge", args=[redirect_month])

    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]

        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "header": month,
        })

    except:
        raise Http404()