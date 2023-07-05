from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

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

def monthly_challenge_by_number(request, month):
    months_list = list(monthly_challenges_text.keys())
    print(months_list)#['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    if month > len(months_list):
        return HttpResponseNotFound("Invalid month number")
    
    redirect_month = months_list[month - 1]
    return HttpResponseRedirect("/challenges/" + redirect_month)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges_text[month]
    except:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challenge_text)







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