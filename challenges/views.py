from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges_text = {
    "january": "Read one book every day!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Meet some friends at the weekend!",
    "may": "Make a barbecue!",
    "june": "Walk with a dog 1 hour!",
    "july": "Go on a holiday!",
    "august": "Swim in lake!",
    "september": "Watch a Django Movie!",
    "october": "Make a pumpkin decoration!",
    "november": "Run 10km!",
    "december": "Buy presents!"
}


# Create your views here.

def index(request):
    list_items = ""
    months_list = list(monthly_challenges_text.keys())
    for month in months_list:
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\"> {month.capitalize()}</a></li>"
        #we get <li>...</li><li>...</li>
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)




def monthly_challenge_by_number(request, month):
    months_list = list(monthly_challenges_text.keys())
    print(months_list)#['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    if month > len(months_list):
        return HttpResponseNotFound("<h1>Invalid month number</h1>")
    
    redirect_month = months_list[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])# /challenge/january
    return HttpResponseRedirect(redirect_path)
    # return HttpResponseRedirect("/challenges/" + redirect_month)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges_text[month]
        response_data = f"<h1>{challenge_text}</h1>"
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
    return HttpResponse(response_data)







    # challenge_text = None
    # if month == "january":
    #     challenge_text = "Read one book every day!"
    # elif month == "february":
    #     challenge_text = "Walk for at least 20 minutes every day!"
    # elif month == "march":
    #     challenge_text = "Learn Django for at least 20 minutes every day!"
    # else:
    #     return HttpResponseNotFound("This month is not supported!")

# def january(request):
#     return HttpResponse("Eat no meat for the entire month!")

# def february(request):
#     return HttpResponse("Walk for at least 20 minutes every day!")

# def march(request):
#     return HttpResponse("Learn Django for at least 20 minutes every day!")