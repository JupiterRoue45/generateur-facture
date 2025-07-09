from django import forms
from .models import Produit

# class pour ajouter une ligne de facture (un produit avec sa quantité) lors de la génération d'une facture

class LigneFactureForm(forms.Form):
    produit = forms.ModelChoiceField(queryset=Produit.objects.all(), label="Produit")
    quantite = forms.IntegerField(min_value=1, label="Quantité")
