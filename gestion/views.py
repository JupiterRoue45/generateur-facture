from django import forms
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import LigneFactureForm
from .models import Facture, LigneFacture, Produit
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

# class pour affichage des listes

class ProduitListView(ListView):
    model = Produit
    template_name = 'produit_liste.html'
    paginate_by = 5  

# class pour création et l'ajout d'un produit

class ProduitCreateView(CreateView):
    model = Produit
    fields = ['nom', 'prix', 'date_peremption']
    template_name = 'produit_form.html'
    success_url = reverse_lazy('produit_liste')

# class pour la modification d'un produit

class ProduitUpdateView(UpdateView):
    model = Produit
    fields = ['nom', 'prix', 'date_peremption']
    template_name = 'produit_form.html'
    success_url = reverse_lazy('produit_liste')

# class pour la suppression d'un produit

class ProduitDeleteView(DeleteView):
    model = Produit
    template_name = 'produit_confirm_delete.html'
    success_url = reverse_lazy('produit_liste')

# Méthode pour créer une facture

def creer_facture(request):
    LigneFormSet = forms.formset_factory(LigneFactureForm, extra=1)  # 1 lignes par défaut

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

# Méthode pour afficher la liste des factures

def facture_liste(request):
    factures = Facture.objects.order_by('-date_creation')
    paginator = Paginator(factures, 5)  # 5 factures par page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'facture_liste.html', {
        'page_obj': page_obj
    })

# Méthode pour afficher les détails d'une facture

def facture_detail(request, pk):
    facture = get_object_or_404(Facture, pk=pk)
    lignes = facture.lignes.all()

    for ligne in lignes:
        ligne.sous_total = ligne.produit.prix * ligne.quantite

    return render(request, 'facture_detail.html', {
        'facture': facture,
        'lignes': lignes
    })
