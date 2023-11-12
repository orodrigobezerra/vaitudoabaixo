from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Articles, Users
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.hashers import make_password
import logging

logger = logging.getLogger(__name__)


def index(request):
	return render(request,'index.html')

def user_login(request):
	return render(request,'login.html')

def list_articles(request):
    articles = Articles.objects.all()
    return render(request, 'crud_items/list_articles.html', {'articles': articles})

def add_article(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        color = request.POST.get('color')
        instrument = request.POST.get('instrument')
        qty_stock = request.POST.get('qtystock')
        price = request.POST.get('price')
        image = request.POST.get('image')

        article = Articles(
            name=name,
            color=color,
            instrument=instrument,
            qty_stock=qty_stock,
            price=price,
            image=image
        )
        article.save()

        return render(request, 'crud_items/add_article.html', {
            'name': name,
            'color': color,
            'instrument': instrument,
            'qty_stock': qty_stock,
            'price': price,
            'image': image
        })

    return render(request, 'crud_items/add_article.html')

def search_article(request):
    if request.method == 'POST':
        name = request.POST.get('search_name')  # Obtém o nome para pesquisar
        articles = Articles.objects.filter(name__icontains=name)  # Realiza a busca por nome (ignorando case-sensitive)

        return render(request, 'crud_items/search_results.html', {'articles': articles, 'search_name': name})

    return render(request, 'crud_items/search_article.html')


def update_article(request):
    if request.method == 'POST':
        article_id = request.POST.get('id')
        new_name = request.POST.get('new_name')
        new_color = request.POST.get('new_color')
        new_instrument = request.POST.get('new_instrument')
        new_qty_stock = request.POST.get('new_qtystock')
        new_price = request.POST.get('new_price')
        new_image = request.POST.get('new_image')

        article = Articles.objects.get(id=article_id)
        article.name = new_name
        article.color = new_color
        article.instrument = new_instrument
        article.qty_stock = new_qty_stock
        article.price = new_price
        article.image = new_image

        article.save()

        return render(request, 'crud_items/update_article.html', {
            'article_id': article_id,
            'new_name': new_name,
            'new_color': new_color,
            'new_instrument': new_instrument,
            'new_qty_stock': new_qty_stock,
            'new_price': new_price,
            'new_image': new_image
        })

    return render(request, 'crud_items/update_article.html')
    
def delete_article(request):
    if request.method == 'POST':
        article_id = request.POST.get('id')

        # Verifica se o artigo existe
        try:
            article = Articles.objects.get(id=article_id)
            article_name = article.name
            article.delete()
            return render(request, 'crud_items/delete_article.html', {'article_name': article_name})
        except Articles.DoesNotExist:
            return render(request, 'crud_items/delete_article.html', {'not_found': True})

    return render(request, 'crud_items/delete_article.html')

def list_users(request):
    users = Users.objects.all()
    return render(request, 'crud_users/list_users.html', {'users': users})

def regist_user(request):
     if request.method == 'POST':
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Create a new User instance
        user = Users(name=name, lastname=lastname, email=email)
        
        # Set the password using set_password method
        user.password = make_password(password)
        
        # Save the user to the database
        user.save()

        return redirect('login_view')
     else:
         return render(request, 'crud_users/regist_user.html')  # Replace 'login' with the actual name or URL of your login page

def update_user(request):
    if request.method == 'POST':
        user_id = request.POST.get('id')
        new_name = request.POST.get('new_name')
        new_lastname = request.POST.get('new_lastname')
        new_email = request.POST.get('new_email')

        user = Users.objects.get(id=user_id)
        user.name = new_name
        user.lastname = new_lastname
        user.email = new_email


        user.save()

        return render(request, 'crud_users/update_user.html', {
            'user_id': user_id,
            'new_name': new_name,
            'new_lastname': new_lastname,
            'new_email': new_email,
        })

    return render(request, 'crud_users/update_user.html')

def delete_user(request):
    if request.method == 'POST':
        user_id = request.POST.get('id')

        # Verifica se o artigo existe
        try:
            user = Users.objects.get(id=user_id)
            user_name = user.name
            user.delete()
            return render(request, 'crud_users/delete_user.html', {'user_name': user_name})
        except Users.DoesNotExist:
            return render(request, 'crud_users/delete_user.html', {'not_found': True})

    return render(request, 'crud_users/delete_user.html')

def login_view(request):
    if request.method == 'POST':
        # Lógica de autenticação aqui
        name = request.POST.get('name')
        password = request.POST.get('password')
        logger.debug(f'Attempting login for email: {name}')
        
        user = authenticate(request, name=name, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Login successful.')
            logger.info('Login successful')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials. Try again.')
            logger.error('Invalid credentials')

    return render(request, 'login.html')
