# Partie 1 : Application pratique

# Liste des ventes quotidiennes
ventes = [
    {"produit": "ordinateur", "quantité": 2, "prix_unitaire": 700},
    {"produit": "smartphone", "quantité": 5, "prix_unitaire": 300},
    {"produit": "tablette", "quantité": 4, "prix_unitaire": 250}
]

# 1. Calculer le total des ventes pour chaque produit
for vente in ventes:
    vente["total"] = vente["quantité"] * vente["prix_unitaire"]  # Ajout d'une clé "total" pour chaque produit
    print(f"Produit: {vente['produit']}, Total des ventes: {vente['total']} euros")

# 2. Afficher le chiffre d'affaires total du magasin pour la journée
chiffre_affaires = sum(vente["total"] for vente in ventes)  # Somme des totaux
print(f"Chiffre d'affaires total du magasin: {chiffre_affaires} euros")

# 3. Ajouter une nouvelle vente au tableau
nouvelle_vente = {"produit": "imprimante", "quantité": 3, "prix_unitaire": 150}
nouvelle_vente["total"] = nouvelle_vente["quantité"] * nouvelle_vente["prix_unitaire"]
ventes.append(nouvelle_vente)  # Ajouter la nouvelle vente
print("Nouvelle vente ajoutée:", nouvelle_vente)

# 4. Afficher les produits dont les ventes totales dépassent 1000 euros
print("Produits avec des ventes totales > 1000 euros:")
for vente in ventes:
    if vente["total"] > 1000:
        print(f"- {vente['produit']} avec un total de {vente['total']} euros")

# Partie 2 : Analyse des données

# Liste des températures de la semaine
# Exemple : Températures en degrés Celsius pour 7 jours consécutifs
temperatures = [18, 22, 19, 25, 17, 20, 24]

# 1. Calculer la température moyenne de la semaine
temperature_moyenne = sum(temperatures) / len(temperatures)
print(f"Température moyenne de la semaine: {temperature_moyenne:.2f} °C")

# 2. Identifier les jours où la température est inférieure à 20°C
jours_froid = [i + 1 for i, temp in enumerate(temperatures) if temp < 20]  # Les jours sont indexés à partir de 1
print("Jours avec températures inférieures à 20°C:", jours_froid)

# 3. Trouver le jour avec la température la plus élevée
jour_max_temp = temperatures.index(max(temperatures)) + 1
print(f"Le jour avec la température la plus élevée est le jour {jour_max_temp} avec {max(temperatures)} °C.")
