from django import forms
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import LigneFactureForm
from .models import Facture, LigneFacture, Produit
from django.shortcuts import get_object_or_404

class ProduitListView(ListView):
    model = Produit
    template_name = 'produit_liste.html'
    context_object_name = 'produits'

class ProduitCreateView(CreateView):
    model = Produit
    fields = ['nom', 'prix', 'date_peremption']
    template_name = 'produit_form.html'
    success_url = reverse_lazy('produit_liste')

class ProduitUpdateView(UpdateView):
    model = Produit
    fields = ['nom', 'prix', 'date_peremption']
    template_name = 'produit_form.html'
    success_url = reverse_lazy('produit_liste')

class ProduitDeleteView(DeleteView):
    model = Produit
    template_name = 'produit_confirm_delete.html'
    success_url = reverse_lazy('produit_liste')

def creer_facture(request):
    LigneFormSet = forms.formset_factory(LigneFactureForm, extra=3)  # 3 lignes par défaut

    if request.method == 'POST':
        formset = LigneFormSet(request.POST)
        if formset.is_valid():
            facture = Facture.objects.create()  # Crée une nouvelle facture
            for form in formset:
                produit = form.cleaned_data.get('produit')
                quantite = form.cleaned_data.get('quantite')
                if produit and quantite:
                    LigneFacture.objects.create(
                        facture=facture,
                        produit=produit,
                        quantite=quantite
                    )
            return redirect('facture_detail', pk=facture.pk)
    else:
        formset = LigneFormSet()

    return render(request, 'creer_facture.html', {'formset': formset})


def facture_detail(request, pk):
    facture = get_object_or_404(Facture, pk=pk)
    lignes = facture.lignes.all()
    return render(request, 'facture_detail.html', {
        'facture': facture,
        'lignes': lignes
    })

