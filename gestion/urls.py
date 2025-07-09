from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProduitListView.as_view(), name='produit_liste'),
    path('produit/ajouter/', views.ProduitCreateView.as_view(), name='produit_ajouter'),
    path('produit/<int:pk>/modifier/', views.ProduitUpdateView.as_view(), name='produit_modifier'),
    path('produit/<int:pk>/supprimer/', views.ProduitDeleteView.as_view(), name='produit_supprimer'),
    path('facture/creer/', views.creer_facture, name='facture_creer'),
    path('facture/<int:pk>/', views.facture_detail, name='facture_detail'),
    path('factures/', views.facture_liste, name='facture_liste'),

]
