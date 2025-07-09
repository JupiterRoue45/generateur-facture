from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Produit

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
