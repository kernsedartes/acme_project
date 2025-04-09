# Create your views here.
from django.views.generic import CreateView
from django.urls import reverse_lazy
from users.forms import CustomUserCreationForm

class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('pages:homepage')
    template_name = 'registration/registration_form.html'