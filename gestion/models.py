from django.db import models

"Classe Produit pour représenter un produit dans la BD"
class Produit(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_peremption = models.DateField()

    def __str__(self):
        return f"{self.nom} - {self.prix}€"

"Classe Facture pour représenter une facture dans la BD"
class Facture(models.Model):
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Facture #{self.id} – {self.date_creation.strftime('%Y-%m-%d %H:%M')}"

    def total(self):
        return sum(ligne.produit.prix * ligne.quantite for ligne in self.lignes.all())

    def nombre_produits(self):
        return sum(ligne.quantite for ligne in self.lignes.all())

"Classe intermédiaire LigneFacture pour pouvoir représenter plusieurs quantité du même produit dans la même facture"
class LigneFacture(models.Model):
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE, related_name='lignes')
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantite} x {self.produit.nom}"
