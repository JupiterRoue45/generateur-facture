from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProduitListView.as_view(), name='produit_liste'),
    path('produit/ajouter/', views.ProduitCreateView.as_view(), name='produit_ajouter'),
    path('produit/<int:pk>/modifier/', views.ProduitUpdateView.as_view(), name='produit_modifier'),
    path('produit/<int:pk>/supprimer/', views.ProduitDeleteView.as_view(), name='produit_supprimer'),

]
