from .models import *

def all_things(request):
    product_all_of_monday = Product.objects.filter(day_of_create = 'Monday', visable = True)
    product_all_of_tuesday = Product.objects.filter(day_of_create = 'Tuesday', visable = True)
    product_all_of_wednesday = Product.objects.filter(day_of_create = 'Wednesday', visable = True)
    product_all_of_thursday = Product.objects.filter(day_of_create = 'Thursday', visable = True)
    product_all_of_friday = Product.objects.filter(day_of_create = 'Friday', visable = True)
    product_all_of_saturday = Product.objects.filter(day_of_create = 'Saturday', visable = True)
    product_all_of_sunday = Product.objects.filter(day_of_create = 'Sunday', visable = True)
    context = {
        'product_all_of_monday':product_all_of_monday,
        'product_all_of_tuesday':product_all_of_tuesday,
        'product_all_of_wednesday':product_all_of_wednesday,
        'product_all_of_thursday':product_all_of_thursday,
        'product_all_of_friday':product_all_of_friday,
        'product_all_of_saturday':product_all_of_saturday,
        'product_all_of_sunday':product_all_of_sunday,
    }
    return context