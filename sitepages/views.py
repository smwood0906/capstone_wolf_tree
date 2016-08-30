from django.shortcuts import render, redirect
from .forms import ContactForm
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context

# Create your views here.
def home(request):
    return render(request, "home.html")

def beers(request):
    return render(request, "beers.html")

def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
                , '')
            contact_email = request.POST.get(
                'contact_email'
                , '')
            contact_zip = request.POST.get(
                'contact_zip'
                , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
        context = Context({
            'contact_name': contact_name,
            'contact_email': contact_email,
            'form_content': form_content,
            'contact_zip': contact_zip,
        })
        content = template.render(context)

        email = EmailMessage(
            "New contact form submission",
            content,
            "smwood@sarahmwood.com",
            ['smwood@sarahmwood.com'],
            headers={'Reply-To': contact_email}
        )
        email.send()
        return redirect('contact')

    return render(request, 'contact.html', {
        'form': form_class,
    })

def tumor(request):
    return render(request, "tumornator.html")

def about(request):
    return render(request, "about.html")





