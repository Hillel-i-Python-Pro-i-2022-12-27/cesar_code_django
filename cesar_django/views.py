
import string

from django.urls import reverse_lazy
from django.views.generic import CreateView

from cesar_django.models import TextForCryptoModel


class CryptoTextCreate(CreateView):
    model = TextForCryptoModel
    fields = (
        'text',
        'crypted_text',
    )
    success_url = reverse_lazy('cesar_django:get-crypto')
