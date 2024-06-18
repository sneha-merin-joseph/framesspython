from django.shortcuts import get_object_or_404, render, redirect
# Create your views here.   
from django.core.paginator import Paginator
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *



def ProductCategoryList(request, id,):
    category = Category.objects.get(id=id)
    movie =    Movie.objects.filter(category=category)
    paginated = Paginator(movie, 8)
    page_number = request.GET.get('page') #Get the requested page number from the URL
    
    product = paginated.get_page(page_number)
    context ={
        'category': category,
        'product': product
            }
    print(category)
    return render(request, 'User-Page/LandingPage/category.html', context)


def Product_List(request):
    products = Movie.objects.all().order_by('-id')
    paginated = Paginator(products, 8)
    page_number = request.GET.get('page') #Get the requested page number from the URL
    product = paginated.get_page(page_number)
    context ={
        'product':product,
    }
    return render(request,'User-Page/Movies/product-list.html',context)

@login_required(login_url='login')
def Product_detail(request,id):
    query = request.GET.get('q')
    category = Category.objects.all()
    movie = Movie.objects.get(pk=id)
    movies = Movie.objects.filter(category=movie.category)
    # images = Images.objects.filter(movie_id=id)
    reviews = Reviews.objects.filter(movie=movie,status ='New')
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.user = request.user  # Set the user
            review.save()
            return redirect('movie:product_detail', id=movie.id)
    else:
        form = ReviewForm()
    context = {
                'movie': movie,
                'movies':movies,
                'reviews': reviews,
                'form': form
               }
               
    return render(request,'User-Page/Movies/Movie_detail.html',context)


@login_required(login_url='login')
def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # Include request.FILES to handle file uploads
        if form.is_valid():
            new_movie = form.save()
            return redirect('movie:product_detail', id=new_movie.id)
        else:
            print(form.errors)  # Print form errors to the console for debugging
    else:
        form = ProductForm()
    return render(request, 'User-Page/Movies/movie_add.html', {'form': form})

@login_required(login_url='login')
def product_update(request, pk):
    movie = get_object_or_404(Movie, id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=movie)  # Include request.FILES
        if form.is_valid():
            form.save()
            return redirect('movie:product_detail', id=movie.id)
        else:
            print(form.errors)  # Print form errors to the console for debugging
    else:
        form = ProductForm(instance=movie)
    return render(request, 'User-Page/Movies/movie_update.html', {'form': form})


@login_required(login_url='login')
def product_delete(request, pk):
    movie = get_object_or_404(Movie, id=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movie:product_list')  # Redirect to a list or another appropriate view
    return render(request, 'User-Page/Movies/movie_confirm_delete.html', {'movie': movie})

