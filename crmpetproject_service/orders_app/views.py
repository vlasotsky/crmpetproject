from django.shortcuts import render
from orders_app.models import CoffeeMakerInUse
from orders_app.forms import SearchForm

# Create your views here.


def mainpage(request):
    data = {
        "title": "Welcome to CRM PET PROJECT!",
        "data": [
            {
                "button_link": "admin",
                "name": "Orders",
                "overview": "Look at the list of up-to-date orders.",
            },
            {
                "button_link": "coffeemakers",
                "name": "Coffeemakers",
                "overview": "Products currently in use",
            },
            {
                "button_link": "devpage",
                "name": "For purchase",
                "overview": "Products currently available for purchase",
            },
        ],
    }

    return render(request, "orders_app/mainpage.html", data)


def get_coffeemakers(request):

    coffeemakers = CoffeeMakerInUse.objects.all()

    if request.method == "POST":
        form = SearchForm(request.POST)

        if form.is_valid():
            search_res = []
            data_for_search = form.data["data_for_search"]

            if data_for_search.isDigit():
                search_res = list(
                    CoffeeMakerInUse.objects.filter(coffeemaker_id=int(data_for_search))
                )

            search_res = set(list(CoffeeMakerInUse.objects.filter(customer__name__contains=data_for_search)) + \
                             list(CoffeeMakerInUse.objects.filter(coffeemaker__manufacturer__contains=data_for_search)) + \
                             list(CoffeeMakerInUse.objects.filter(coffeemaker__model__contains=data_for_search)) + \
                             list(CoffeeMakerInUse.objects.filter(status__contains=data_for_search)) + search_res)
            
            return render(request, "orders_app/table.html", {"coffeemakers": coffeemakers, "form": form})
        
    return render(request, "orders_app/table.html", {"coffeemakers": coffeemakers})


def devpage(request):

    return render(request, "orders_app/devpage.html", {"title": "Sorry!"})
