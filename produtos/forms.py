from django import forms
from django.forms import inlineformset_factory
from produtos.models import Imagens
from produtos.models import Produtos

class ImagensForm(forms.ModelForm):
    class Meta:
        model = Imagens
        fields = ('imagem',)

ImagensFormSet = inlineformset_factory(Produtos, Imagens, form=ImagensForm, extra=1)
