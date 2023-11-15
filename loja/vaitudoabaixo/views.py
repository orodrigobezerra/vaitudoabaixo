from django.shortcuts import render, redirect
from .models import Articles, User
from django.contrib.auth import authenticate, login as auth_login, get_user_model
from django.contrib.auth.decorators import login_required
from django.http import StreamingHttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import get_user_model

import logging, csv

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
    # Filtrar usuários excluindo superusuários
    users = get_user_model().objects.filter(is_superuser=False)

    return render(request, 'crud_users/list_users.html', {'users': users})


def regist_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            # Autenticar o usuário antes de fazer login
            authenticated_user = authenticate(request, username=user.username, password=form.cleaned_data['password1'])
            if authenticated_user:
                auth_login(request, authenticated_user)

                messages.success(request, 'User registered successfully. You are now logged in.')
                return redirect('index')  # Redireciona para a página inicial após o registro
            else:
                messages.error(request, 'Error authenticating user. Please try logging in.')

        else:
            messages.error(request, 'Error registering user. Correct the errors.')

    else:
        form = UserCreationForm()

    return render(request, 'crud_users/regist_user.html', {'form': form})

@login_required(login_url='user_login')
def update_user(request):
    user = request.user

    if request.method == 'POST':
        # Obtém os novos dados do formulário
        new_username = request.POST['new_username']
        new_password = request.POST['new_password']

        # Atualiza os campos desejados do usuário
        user.username = new_username
        user.set_password(new_password)
        user.save()

        messages.success(request, 'Success, your user was updated!')
        return redirect('update_user')  # Altere para o nome de URL apropriado
    else:
        return render(request, 'crud_users/update_user.html')

@login_required(login_url='user_login')
def delete_user(request):
    if request.method == 'POST':
        username_to_delete = request.POST.get('username')

        try:
            user_to_delete = User.objects.get(username=username_to_delete)
            user_to_delete.delete()
            messages.success(request, f'The user {username_to_delete} has been deleted successfully.')
            return redirect('user_login')  # Altere para o nome da URL da sua página inicial
        except User.DoesNotExist:
            messages.error(request, f'The user {username_to_delete} does not exist.')
    
    return render(request, 'crud_users/delete_user.html')

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        logger.debug(f'Attempting login with email: {email} and password: {password}')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            logger.info(f'Successful login for user: {user.email}')
            auth_login(request, user)  # Use auth_login em vez de login
            return redirect('index')  # Redireciona para a URL nomeada 'index'
        else:
            logger.warning(f'Failed login attempt for email: {email}, password: {password}')
            return render(request, 'login.html', {'error_message': 'Invalid credentials. Try again.'})
    else:
        return render(request, 'login.html')


@login_required(login_url='user_login')
def export_users(request):
    users = User.objects.all()

    def generate_csv():
        yield "Email,Password\n"
        for user in users:
            yield f"{user.email},{user.password}\n"

    response = StreamingHttpResponse(generate_csv(), content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename="users.csv"'
    return response

@login_required(login_url='user_login')
def export_articles(request):
    articles = Articles.objects.all()

    def generate_csv():
        yield "Name,Color,Instrument,Qty_Stock,Price,Image\n"
        for article in articles:
            yield f"{article.name},{article.color},{article.instrument},{article.qty_stock},{article.price},{article.image}\n"

    response = StreamingHttpResponse(generate_csv(), content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename="articles.csv"'
    return response
