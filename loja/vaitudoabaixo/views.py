from django.shortcuts import render, redirect
from .models import Articles, myUser, MyUserManager
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

@login_required(login_url='user_login')
def index(request):
	return render(request,'index.html')

@login_required(login_url='user_login')
def list_articles(request):
    articles = Articles.objects.all()
    return render(request, 'crud_items/list_articles.html', {'articles': articles})

@login_required(login_url='user_login')
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

@login_required(login_url='user_login')
def search_article(request):
    if request.method == 'POST':
        name = request.POST.get('search_name')  # Obtém o nome para pesquisar
        articles = Articles.objects.filter(name__icontains=name)  # Realiza a busca por nome (ignorando case-sensitive)

        return render(request, 'crud_items/search_results.html', {'articles': articles, 'search_name': name})

    return render(request, 'crud_items/search_article.html')

@login_required(login_url='user_login')
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

@login_required(login_url='user_login')    
def delete_article(request):
    if request.method == 'POST':
        article_id = request.POST.get('id')

        try:
            article = Articles.objects.get(id=article_id)
            article_name = article.name
            article.delete()
            return render(request, 'crud_items/delete_article.html', {'article_name': article_name})
        except Articles.DoesNotExist:
            return render(request, 'crud_items/delete_article.html', {'not_found': True, 'article_name': article_name})
    
    return render(request, 'crud_items/delete_article.html')

@login_required(login_url='user_login')
def list_users(request):
    users = myUser.objects.all()
    return render(request, 'crud_users/list_users.html', {'users': users})

def regist_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if myUser.objects.filter(email=email).exists():
            return render(request, 'crud_users/regist_user.html', {'error_message': 'User with this email already exists'})

        # Use o método create_user fornecido pelo seu MyUserManager
        user = myUser.objects.create_user(email=email, password=password, name=name, lastname=lastname)

        return redirect('user_login')
    else:
        return render(request, 'crud_users/regist_user.html')

@login_required(login_url='user_login')
def update_user(request):
    if request.method == 'POST':
        new_name = request.POST.get('new_name')
        new_lastname = request.POST.get('new_lastname')
        new_email = request.POST.get('new_email')
        new_password = request.POST.get('new_password')  # Corrigido o nome do campo

        # Obtém o usuário usando o modelo myUser
        user = myUser.objects.get(email=new_email)

        user.name = new_name
        user.lastname = new_lastname
        user.email = new_email
        user.set_password(new_password)  # Use set_password para criptografar a senha corretamente

        user.save()

        return render(request, 'crud_users/update_user.html', {
            'new_name': new_name,
            'new_lastname': new_lastname,
            'new_email': new_email,
        })

    return render(request, 'crud_users/update_user.html')

@login_required(login_url='user_login')
def delete_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Alterado para 'email'

        try:
            # Obtém o usuário usando o modelo myUser
            user = myUser.objects.get(email=email)
            user_name = user.name
            user.delete()
            return render(request, 'crud_users/delete_user.html', {'user_name': user_name})
        except myUser.DoesNotExist:  # Alterado para 'myUser'
            return render(request, 'crud_users/delete_user.html', {'not_found': True})

    return render(request, 'crud_users/delete_user.html')

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        logger.debug(f'Attempting login with email: {email} and password: {password}')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            logger.info(f'Successful login for user: {user.email}')
            login(request, user)
            return redirect('index')  # Redireciona para a URL nomeada 'index'
        else:
            logger.warning(f'Failed login attempt for email: {email}, password: {password}')
            return render(request, 'login.html', {'error_message': 'Invalid credentials. Try again.'})
    else:
        return render(request, 'login.html')

def export_users(request):
    # Para usuários do seu modelo myUser
    custom_users = myUser.objects.all()
    custom_users_data = [f"Email: {user.email}, Password: {user.password}" for user in custom_users]

    return HttpResponse("\n".join(custom_users_data), content_type="text/plain")

""" def login_view(request):
    if request.method == 'POST':
        # Lógica de autenticação aqui
        name = request.POST.get('name')
        password = request.POST.get('password')
        logger.debug(f'Attempting login for name: {name}')
        
        user = authenticate(request, name=name, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Login successful.')
            logger.info('Login successful')
            return redirect('index')
        else:
            messages.error(request, 'Invalid credentials. Try again.')
            logger.error('Invalid credentials')

    return redirect('index') """
