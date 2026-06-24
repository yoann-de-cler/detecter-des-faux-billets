# 🤖 Détection de faux billets – Machine Learning

## 🎯 Objectif
Construire un modèle de machine learning capable de détecter automatiquement les faux billets à partir de leurs caractéristiques physiques.

---

## 📊 Données
Les données contiennent des mesures physiques de billets :
- dimensions (longueur, hauteur, diagonale)
- marges (haut, bas, gauche, droite)
- variable cible : billet authentique ou faux

---

## 🧹 Préparation des données
- Analyse exploratoire (distributions, corrélations)
![Boxplot de la distribution des variables explicatives sur la varibale cible](boxplot_variables_explicatives_par_classe.png)
- Traitement des valeurs manquantes (imputation via régression)
- Détection des outliers
- Standardisation des variables
- Séparation train / test

---

## 🤖 Modélisation
Plusieurs algorithmes ont été testés et comparés :
- Régression logistique
![Regression logistique](evaluation_modele_regression_logistique.png)
- K-Nearest Neighbors
- Random Forest
- K-means (analyse exploratoire non supervisée)

---

## 📈 Évaluation
Les modèles ont été évalués via :
- Accuracy
- Precision / Recall / F1-score
- ROC AUC
- Matrices de confusion
- Validation croisée
![Validation des modèles](validation_modeles.png)

---

## 🏆 Résultat
- Les classes sont fortement séparables dans l’espace des variables
- Les modèles supervisés obtiennent de très bonnes performances
- La régression logistique est retenue pour sa simplicité et son interprétabilité
- Un pipeline complet permet de reproduire les prédictions en production

---

## 🚀 Industrialisation
Le modèle final est encapsulé dans un pipeline :
- imputation des valeurs manquantes
- standardisation
- modèle de classification

Le pipeline est sauvegardé et réutilisable via `joblib`.

---

## 🛠️ Stack technique
- Python
- Pandas / NumPy
- Scikit-learn
- Statsmodels
- Matplotlib / Seaborn
- Joblib

---

## 👤 Auteur
Yoann De Cler
