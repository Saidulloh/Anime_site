from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.paginator import Paginator
import datetime
from .forms import *
from .models import *
from .service import send

# Create your views here.

def homepage(request):
    product_slider = Product.objects.all()[:3]
    genres = Genre.objects.all()
    latest_products = Product.objects.all()
    all_products = Product.objects.all()
    
    return render(request, 'index.html', locals())


def product_detail(request, id): 
    # Поиск по сайту  
    if 'search_button' in request.GET:
        word = request.GET.get('search_word')
        search_products = Product.objects.filter(Q(title__icontains = word) | Q(description__icontains = word))
        # для выведения общего отзыва
        d = {}
        rrr = [1, 2, 3, 4, 5]
        for i in search_products:
            comments_one_anime = Comment.objects.filter(product = i)
            f = 0
            lenght = len(comments_one_anime)
            for comments in comments_one_anime:
                f += comments.star
            if lenght != 0:
                d[i.id] = round(f / lenght)
            else:
                d[i.id] = 'Нет отзывов'

        return render(request, 'detail_pages/search_page.html', locals())

    else:
        video = Video.objects.filter(product_id = id)
        images = Image.objects.filter(product_id = id)
        genres = Genre.objects.all()
        category_all = Category.objects.all()
        comments = Comment.objects.filter(product_id = id)
        product = Product.objects.get(id = id)

        # для выведения общего отзыва
        d = {}
        comments_one_anime = Comment.objects.filter(product = product)
        f = 0
        lenght = len(comments_one_anime)
        for comment_all in comments_one_anime:
            f += comment_all.star
        if lenght != 0:
            d[product.id] = round(f / lenght)
        else:
            d[product.id] = 'Нет отзывов'

        # Пагинация
        contact_list = Comment.objects.filter(product_id = id)
        paginator = Paginator(contact_list, 3)
        page_num = request.GET.get('page')
        page_obj = paginator.get_page(page_num)

    # Комментарий
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False) 
            form.product = product
            form.owner = request.user # что бы сохранить пользователя который оставил комм
            form.save()
            return redirect('detailanime', id)
    else:
        form = CommentForm()

    rrr = [1, 2, 3, 4, 5]

    return render(request, 'detail_pages/single_anime.html', locals())


def category_page(request, id):
    category = Category.objects.get(id = id)
    product_all = Product.objects.filter(category = category)

    # для выведения общего отзыва
    d = {}
    for i in product_all:
        comments_one_anime = Comment.objects.filter(product = i)
        f = 0
        lenght = len(comments_one_anime)
        for comments in comments_one_anime:
            f += comments.star
        if lenght != 0:
            d[i.id] = round(f / lenght)
        else:
            d[i.id] = 'Нет отзывов'

    rrr = [1, 2, 3, 4, 5]

    return render(request, 'detail_pages/category_page.html', locals())


def genre_page(request, id):
    genre = Genre.objects.get(id = id)
    product_all = Product.objects.filter(genre = genre)

    # для выведения общего отзыва
    d = {}
    for i in product_all:
        comments_one_anime = Comment.objects.filter(product = i)
        f = 0
        lenght = len(comments_one_anime)
        for comments in comments_one_anime:
            f += comments.star
        if lenght != 0:
            d[i.id] = round(f / lenght)
        else:
            d[i.id] = 'Нет отзывов'

    rrr = [1, 2, 3, 4, 5]
    return render(request, 'detail_pages/genre_page.html', locals())


def what_is_on_this_week(request):
    # Поиск по сайту 
    if 'search_button' in request.GET:
        word = request.GET.get('search_word')
        search_products = Product.objects.filter(Q(title__icontains = word) | Q(description__icontains = word))
        # для выведения общего отзыва
        d = {}
        rrr = [1, 2, 3, 4, 5]
        for i in search_products:
            comments_one_anime = Comment.objects.filter(product = i)
            f = 0
            lenght = len(comments_one_anime)
            for comments in comments_one_anime:
                f += comments.star
            if lenght != 0:
                d[i.id] = round(f / lenght)
            else:
                d[i.id] = 'Нет отзывов'
        return render(request, 'detail_pages/search_page.html', locals())
    else:
        time_now = datetime.datetime.now()
        day_of_the_week = datetime.datetime.ctime(time_now)
        day = day_of_the_week.split(' ')[0]

        return render(request, 'detail_pages/what_is_on.html', locals())


def contacts(request):
    if request.method == 'GET':
        form = ContactForm(request.GET)
        print('форма')
        if form.is_valid():
            print('валидна')
            send(
                form.cleaned_data['subject'],
                form.cleaned_data['message'],
                request.user.email,
            )
    form = ContactForm()
    return render(request, 'detail_pages/contacts.html', locals())
