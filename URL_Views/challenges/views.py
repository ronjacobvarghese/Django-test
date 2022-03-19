from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
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
  "september":"This month is september",
  "october":"This month is october",
  "november": "This month is november",
  "december": "This month is december",
}

def index(request):
  list_items = ""
  months = list(monthly_challenges.keys())
  
  for month in months:
    capitalize_month = month.capitalize()
    month_path  = reverse("monthly-challenge", args = [month])
    list_items += f"<li><a href = \"{month_path}\">{capitalize_month}</a></li>"

  response_data= f"<ul>{list_items}</ul>"
  return HttpResponse(response_data)

def monthly_number(request,month):
  months = list(monthly_challenges.keys())
  
  if month > len(months):
    return HttpResponseNotFound("Invalid Month!!")
  redirect_month = months[month-1]
  redirect_path = reverse("monthly-challenge",args = [ redirect_month ])
  return  HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
  try:
    challenge_text = monthly_challenges[month]
    response_data = f"<h1>{challenge_text}</h1>"
    return HttpResponse(response_data)
  except:
    return HttpResponseNotFound("<h1> This month is not supported</h1>")
   
  