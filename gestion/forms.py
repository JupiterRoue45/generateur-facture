from django import forms
from .models import Produit

class LigneFactureForm(forms.Form):
    produit = forms.ModelChoiceField(queryset=Produit.objects.all(), label="Produit")
    quantite = forms.IntegerField(min_value=1, label="Quantité")
