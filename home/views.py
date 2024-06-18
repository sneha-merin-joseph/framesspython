from django.http import HttpResponseRedirect
from django.shortcuts import render
# Create your views here.
from django.core.paginator import Paginator
from .models import *
from movies.models import *
from django.db.models import Q


# Create your views here.
def homepage(request):
    products = Movie.objects.all().order_by('-id')
    paginated = Paginator(products, 8)
    page_number = request.GET.get('page') #Get the requested page number from the URL
    product = paginated.get_page(page_number)
    context ={
        'product':product,
    }
    return render(request, 'User-Page/LandingPage/home.html',context)

def search(request):  # new
    if 'query' in request.GET:
        query = request.GET.get('query')
        if query:
            category = Category.objects.all()
            movie = Movie.objects.filter(product__title__icontains=query)
            movies = Movie.objects.filter(category=movie.category)
            # images = Images.objects.filter(movie_id=id)
            review = Review.objects.filter(movie=movie,status='True')
            context={
                'movie':movie,
                'movies':movies,
                'review': review,
            }
        
            return render(request, 'User-Page/Movies/product-list.html', context)
        return HttpResponseRedirect('/')