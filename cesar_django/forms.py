from django.urls import reverse_lazy
from django.views.generic import FormView

class GetCryptoTextForm(FormView):
    template_name = "cesar_django/textforcryptomodel_form.html"
    success_url = reverse_lazy('cesar_django:get-crypto')
