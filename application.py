import joblib
import pandas as pd
import numpy as np
import os


model = joblib.load('model_billet.pkl')
features = joblib.load('features.pkl')

def safe_float_input(prompt):
    value = input(prompt)
    
    if value.strip() == "":
        print(f"⚠️ {prompt} manquant")
        return np.nan
    
    else :
        return float(value)

def predict_single_value(model) :

    values = {}
    values['diagonal'] = safe_float_input('diagonal (diagonale) (en mm) :')
    values['height_left'] = safe_float_input('height left (hauteur du billet (mesuré sur le côté gauche) (en mm) :')
    values['height_right'] = safe_float_input('height right (hauteur du billet (mesuré sur le coté droit) (en mm) :')
    values['margin_low'] = safe_float_input("margin low (marge entre le bord inférieur et l'image) (en mm) :")
    values['margin_up'] = safe_float_input("margin up (marge entre le bord supérieur et l'image) (en mm) :")
    values['length'] = safe_float_input("length (longueur) (en mm) :")
                     
    
    # 1. transformer en format sklearn
    X = pd.DataFrame([values], columns=features)
    
    # 2. prédiction
    pred = model.predict(X)[0]

    # 3. Interprétation
    if pred == 1:
        return 'billet authentique'
    else :
        return 'faux billet'

    
def predict_billet_csv():

    # 1. chemin fichier
    DATA_PATH = input("Entrez le chemin du fichier CSV : ")

    # 2. vérification existence
    if not os.path.exists(DATA_PATH):
        print(f"❌ Attention : le fichier '{DATA_PATH}' n'existe pas.")
        return

    # 3. chargement
    try:
        df = pd.read_csv(DATA_PATH, sep=None, engine='python')
        print("✅ Données chargées :", df.shape)

    except Exception as e:
        print("❌ Erreur lors du chargement :", e)
        return

   
    # 4. vérification colonnes
    missing_cols = [f for f in features if f not in df.columns]

    if missing_cols:
        print(f"❌ Colonnes manquantes : {missing_cols}")
        return

    # 5. garder uniquement les bonnes colonnes
    X = df[features]

    # 5 bis. Détection des valeurs manquantes
    missing = X.isna().sum()
    missing = missing[missing > 0]

    if not missing.empty:
        print("\n⚠️ Attention : valeurs manquantes détectées")

        for col, count in missing.items():
            print(f"- {col} : {count} valeur(s) remplacée(s) par la moyenne")

        print("\nLes valeurs non renseignées seront imputées automatiquement avant la prédiction.\n"
        "Les variables 'length (longueur)' et 'margin_low (marge entre le bord inférieur et l'image)'\n"
        "sont particulièrement importantes pour la fiabilité du résultat.")

    # 6. prédiction
    preds = model.predict(X)

    # 7. Ajout des prédictions
    df['prediction'] = preds.astype(int)

    # 7. interprétation
    df["prediction_label"] = df["prediction"].map({
        1: "Billet authentique",
        0: "Faux billet"
    })

    return df[['id', 'prediction_label']]


def main():
    print("=== Détecteur de faux billets ===")
    print("1 - Manuel")
    print("2 - Import CSV")

    choice = input("Choix : ")

    if choice == "1":
        print("⚠️ Mode manuel :")
        print("- Les valeurs non renseignées seront automatiquement remplacées")
        print("- Les variables 'length (longueur)' et 'margin_low (marge entre le bord inférieur et l'image)' " \
        "sont particulièrement importantes pour la fiabilité du résultat.\n")
        print(predict_single_value(model))

    elif choice == "2":
        df = predict_billet_csv()
        print(df)

    else:
        print("Choix invalide")


if __name__ == "__main__":
    main()

