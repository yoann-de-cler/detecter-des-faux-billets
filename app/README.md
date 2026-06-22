# 🖥️ Application - Détection de faux billets

## 🎯 Objectif
Cette application permet de prédire si un billet est authentique ou faux à l’aide d’un modèle de machine learning.

---

## 🧠 Modèle utilisé
- Régression logistique
- Préprocessing sauvegardé via pickle (model + features)

---

## 🧭 Fonctionnalités
- Saisie manuelle des caractéristiques d’un billet
- Import d’un fichier CSV
- Prédictions automatiques

---

## 📊 Résultat
L’application retourne :
- ID du billet (si CSV)
- Prédiction : authentique / faux billet

---

## ▶️ Lancement de l’application

1. Ouvrir un terminal (Anaconda Prompt ou autre)

2. Se placer dans le dossier de l’application :

```
cd chemin/vers/le/projet/app
```

3. Lancer l'application :

```
python application.py
```

---

## 🧭 Utilisation de l’application

Une fois l’application lancée :

- Choisir `1` → Mode manuel  
  → saisir les caractéristiques d’un billet une par une

- Choisir `2` → Import CSV  
  → entrer le chemin du fichier CSV à analyser

---

## 📊 Résultat

L’application affiche :
- l’identifiant du billet (si CSV)
- la prédiction : **authentique** ou **faux billet**

---


