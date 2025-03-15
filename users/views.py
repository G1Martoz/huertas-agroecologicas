from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.contrib.auth.tokens import default_token_generator
from .forms import UserRegistrationForm
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ValidationError

@require_http_methods(['GET', 'POST'])
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            current_site = get_current_site(request)
            mail_subject = 'Activa tu cuenta'
            message = render_to_string('users/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            try:
                email = EmailMessage(mail_subject, message, to=[user.email])
                email.send()
                messages.success(request, 'Por favor confirma tu email para completar el registro.')
                return redirect('login')
            except Exception as e:
                user.delete()  # Delete the user if email sending fails
                messages.error(request, 'Lo sentimos, hubo un problema al enviar el email de confirmación. Por favor, inténtalo de nuevo más tarde.')
                return redirect('register')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        messages.success(request, '¡Gracias por confirmar tu email! Ahora puedes iniciar sesión.')
        return redirect('login')
    else:
        messages.error(request, 'El enlace de activación es inválido.')
        return redirect('register')