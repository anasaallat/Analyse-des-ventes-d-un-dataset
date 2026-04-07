import pandas as pd

# Charger les données
df = pd.read_csv("sales.csv")

# Voir les premières lignes
print(df.head())

# Calcul du chiffre d'affaires total
revenue = df["Sales"].sum()
print("Chiffre d'affaires :", revenue)

# Top 5 produits
top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(5)

print("Top produits :")
print(top_products)

# Panier moyen
average_order = df["Sales"].mean()

print("Panier moyen :", average_order)

import matplotlib.pyplot as plt

df.groupby("Category")["Sales"].sum().plot(kind="bar")
plt.show()