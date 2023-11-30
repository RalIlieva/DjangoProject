from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact information saved successfully.')
            return render(request, 'contact.html', {'form': ContactForm()})
        else:
            print(form.errors)
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def contact_submit(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact form submitted successfully!')
            return render(request, 'contact.html', {'form': ContactForm()})
        else:
            messages.error(request, 'There was an error in the form submission.')
    else:
        pass

    return render(request, 'contact.html', {'form': ContactForm()})


def snake_game_view(request):
    return render(request, 'snake.html')


def article_detail(request, article_id):
    pass


def product_category(request, category):
    # Add your logic here, for example, you can render a template
    if category == 'option1':
        template_name = 'option1_template.html'
    elif category == 'option2':
        template_name = 'option2_template.html'
    else:
        # Handle other categories or provide a default template
        template_name = 'products.html'

    return render(request, template_name, {'category': category})


def products(request):
    return render(request, 'products.html')
