import streamlit as st
import pandas as pd
import base64

st.set_page_config(layout="wide", page_title="Food Packaging Safety Assistant", initial_sidebar_state="expanded")

st.title("Food Packaging Safety Assistant")

# Initial Contextual Information
with st.expander("Contexte de l'Emballage", expanded=True):
    st.write("Veuillez fournir des informations supplémentaires pour une analyse plus précise.")
    purpose = st.text_input("Objectif de l'emballage (ex: conservation, protection, transport, etc.)")
    client_needs = st.text_area("Besoins spécifiques du client (ex: type d'aliment, conditions de stockage, etc.)")
    additional_info = st.text_area("Informations complémentaires (ex: présence de nanoparticules, etc.)")

# Side Bar Menu
st.sidebar.title("Navigation")
choice = st.sidebar.radio("Choisir un logigramme:", ("Réglementation et Spécificités", "Tests et Exigences"))

# --- Logigramme 1: Réglementation et Spécificités ---
def logigramme_1():
    st.header("Logigramme 1: Réglementation et Spécificités selon le matériau")

    # Define packaging materials
    materials = ["Polystyrène", "Polypropylène", "Polyéthylène", "Polyéthylène Téréphtalate (PET)", "Aluminium", 
                 "Papier/Carton", "Bois", "Métal", "Verre", "Céramique", "Pellicule de cellulose régénérée", "Autres"]
    material = st.selectbox("Sélectionner le matériau d'emballage:", materials)

    st.subheader("Règlements applicables:")

    # EU Regulations
    st.write("**Règlement (CE) No 1935/2004:** Règles générales pour les matériaux au contact des aliments.")
    if material in ["Polystyrène", "Polypropylène", "Polyéthylène", "PET"]:
        st.write("**Règlement (EU) No 10/2011:**  Mesures spécifiques pour les plastiques.")
    if material == "Aluminium":
        st.write("**Arrêté du 27 août 1987:** Règles spécifiques pour l'aluminium.")
    if material == "Papier/Carton":
        st.write("**Arrêté du 28 juin 1912:** Règles spécifiques pour le papier/carton.")
    if material == "Métal":
        st.write("**Décret No. 76-492:** Règles spécifiques pour les objets en étain.")
    if material == "Verre":
        st.write("**Arrêté du 15 novembre 1945:** Règles spécifiques pour le verre.")
    if material == "Bois":
        st.write("**Arrêté du 15 novembre 1945:** Règles spécifiques pour le bois.")
    if material == "Céramique":
        st.write("**Directive 2005/31/CE:** Règles spécifiques pour les céramiques.")
        st.write("**Directive 84/500/CEE:** Règles spécifiques pour les céramiques (ancienne directive).")
    if material == "Pellicule de cellulose régénérée":
        st.write("**Directive 2007/42/CE:** Règles spécifiques pour la pellicule de cellulose régénérée.")

    # French Regulations 
    st.write("**Décret No. 2007-766:** Application du code de la consommation.")
    st.write("**Décret No. 2008-1469:**  Modifie le Décret 2007-766.")

    st.subheader("Spécifications spécifiques:")

    # Example - adapt based on the ACTIA guide
    if material == "Polystyrène":
        st.write("- Limite de migration globale: 10 mg/dm²")
        st.write("- Limites de migration spécifique pour certains additifs (voir liste EU).")
    elif material == "Aluminium":
        st.write("- Teneur en aluminium > 99%")
        st.write("- Teneur en impuretés < 1%")
    elif material == "Papier/Carton":
        st.write("- Vérifier l'origine des fibres recyclées.")
        st.write("- Vérifier le respect des critères de pureté chimique du matériau recommandés par la DGCCRF.")
    elif material == "Métal":
        st.write("- Vérifier la conformité aux restrictions d'emploi pour les métaux (ex: cuivre, zinc galvanisé).")
    elif material == "Verre":
        st.write("- Teneur en oxyde de plomb < 24%.")
    elif material == "Bois":
        st.write("- Vérifier la conformité aux essences de bois autorisées.")
    elif material == "Céramique":
        st.write("- Limites de migration spécifique pour le plomb et le cadmium.")
    elif material == "Pellicule de cellulose régénérée":
        st.write("- Limites de migration spécifique pour les monomères et les additifs.")

    st.subheader("Résumé:")
    st.write("L'emballage en {} est soumis aux règlements suivants:".format(material))
    st.write("EU: [Liste des règlements EU]")
    st.write("France: [Liste des règlements français]")
    st.write("Spécifications: [Liste des spécifications]")

    # Export Results
    st.download_button(
        label="Télécharger les résultats",
        data=st.session_state.get("results_reglementation", "Aucun résultat à exporter"),
        file_name="results_reglementation.txt",
        mime="text/plain"
    )

# --- Logigramme 2: Tests et Exigences ---
def logigramme_2():
    st.header("Logigramme 2: Tests et Exigences selon le matériau et l'aliment")

    # Define packaging materials
    materials = ["Polystyrène", "Polypropylène", "Polyéthylène", "Polyéthylène Téréphtalate (PET)", "Aluminium", 
                 "Papier/Carton", "Bois", "Métal", "Verre", "Céramique", "Pellicule de cellulose régénérée", "Autres"]
    material = st.selectbox("Sélectionner le matériau d'emballage:", materials)

    # Define the food types
    food_types = ["Aqueux pH > 4.5", "Acide", "Gras", "Sec", "Autres"]
    food_type = st.selectbox("Sélectionner le type d'aliment:", food_types)

    st.subheader("Questions pour identifier les tests et exigences:")

    # Define questions based on material and food type
    questions = []
    if material in ["Polystyrène", "Polypropylène", "Polyéthylène", "PET", "Aluminium", "Métal"]:
        questions = [
            "Le matériau est-il en contact direct avec l'aliment ?",
            "Y a-t-il une barrière fonctionnelle ?",
            "Le matériau est-il composé de plusieurs couches ?",
            "Le matériau est-il recyclé ?",
            "Le matériau est-il actif ou intelligent ?",
            "Le matériau est-il soumis à un traitement thermique ?",
            "Quelle est la température maximale du traitement thermique ?",
            "Quelle est la durée maximale du traitement thermique ?",
            "Quelle est la durée de conservation du produit (DLC ou DLUO) ?"
        ]
    # ... (Add logic for other materials as needed)

    # Create a list of answers
    answers = []
    for question in questions:
        answer = st.radio(question, ("Oui", "Non"))
        answers.append(answer)

    st.subheader("Tests et Exigences:")
    tests = []
    requirements = []

    # Logigramme 2 (Décret 2008-1469) - Example logic - Adapt based on the ACTIA guide
    if material in ["Polystyrène", "Polypropylène", "Polyéthylène", "PET", "Aluminium", "Métal"]:
        if answers[0] == "Oui":  # Contact Direct
            if answers[5] == "Oui":  # Thermal Treatment
                tests.append("Migration globale")
                tests.append("Migration spécifique")
                requirements.append("Limite de migration globale (10 mg/dm²)")
                requirements.append("Limite de migration spécifique pour les substances concernées")
        else:
            tests.append("Migration spécifique pour les substances concernées")
        if answers[8] == "Oui": # DLC/DLUO
            tests.append("Tests organoleptiques")
        if answers[6] == "Oui": # Thermal Treatment Max Temp
            if int(st.text_input("Température maximale du traitement thermique (en °C)")) > 100:
                tests.append("Migration spécifique pour les substances sensibles à la chaleur")

    # Logigramme 3 (Mesures spécifiques) - Replace with ACTIA Guide logic
    if material in ["Polystyrène", "Polypropylène", "Polyéthylène", "PET"]:
        if answers[1] == "Oui": # Barrier Function
            requirements.append("Vérifier la performance de la barrière fonctionnelle.")
        if answers[2] == "Oui": # MultiLayer
            tests.append("Migration spécifique pour chaque couche")
        if answers[3] == "Oui": # Recycled
            requirements.append("Vérifier la conformité du processus de recyclage.")
        if answers[4] == "Oui": # Active
            requirements.append("Vérifier la conformité du matériau actif/intelligent aux règlements spécifiques.")
    # ... (Add logic for other materials as needed)

    # Logigramme 4 (Mesures spécifiques françaises) - Replace with ACTIA Guide logic
    if material == "Aluminium":
        if answers[0] == "Oui": # Contact Direct
            if int(st.text_input("Teneur en aluminium (%)")) < 99:
                requirements.append("Vérifier la conformité de la teneur en aluminium.")
            if int(st.text_input("Teneur en impuretés (%)")) > 1:
                requirements.append("Vérifier la conformité de la teneur en impuretés.")
    if material == "Métal":
        if answers[1] == "Oui":  # Treated
            if st.text_input("Type de traitement du métal") in ["Étamé", "Galvanisé"]:
                requirements.append("Vérifier la conformité aux restrictions d'emploi pour les métaux traités (ex: cuivre, zinc galvanisé).")
        if answers[2] == "Oui": # Thermal Treatment
            if int(st.text_input("Température maximale du traitement thermique (en °C)")) > 100:
                tests.append("Migration spécifique pour les substances sensibles à la chaleur")
    # ... (Add logic for other materials as needed)

    # Logigramme 5 (Recommandations françaises) - Replace with ACTIA Guide logic
    if material == "Papier/Carton":
        if answers[0] == "Oui": # Contact Direct
            requirements.append("Vérifier l'origine des fibres recyclées.")
        if answers[2] == "Oui": # Printed
            requirements.append("Vérifier la conformité des encres d'impression.")
        if answers[3] == "Oui": # HumidOrFattyFood
            requirements.append("Vérifier la résistance du matériau aux aliments humides ou gras.")
    # ... (Add logic for other materials as needed)

    # Display Results
    st.write(f"**Tests recommandés:** {', '.join(tests)}")
    st.write(f"**Exigences spécifiques:** {', '.join(requirements)}")

    # Export Results
    st.download_button(
        label="Télécharger les résultats",
        data=st.session_state.get("results_tests", "Aucun résultat à exporter"),
        file_name="results_tests.txt",
        mime="text/plain"
    )

# --- Logigramme 3: Mesures spécifiques (EU) ---
def logigramme_3(material):
    st.subheader("Logigramme 3: Mesures spécifiques (EU)")

    # Replace with detailed information from ACTIA Guide
    if material == "Polystyrène":
        st.write("Liste positive: [Liste des substances autorisées pour le Polystyrène]")
        st.write("Limite de migration globale: 10 mg/dm²")
        st.write("Limite de migration spécifique: [Liste des substances avec LMS]")
        st.write("Restrictions d'emploi: [Conditions spécifiques d'utilisation]")
    elif material == "Polypropylène":
        st.write("Liste positive: [Liste des substances autorisées pour le Polypropylène]")
        st.write("Limite de migration globale: 10 mg/dm²")
        st.write("Limite de migration spécifique: [Liste des substances avec LMS]")
        st.write("Restrictions d'emploi: [Conditions spécifiques d'utilisation]")
    elif material == "Polyéthylène":
        st.write("Liste positive: [Liste des substances autorisées pour le Polyéthylène]")
        st.write("Limite de migration globale: 10 mg/dm²")
        st.write("Limite de migration spécifique: [Liste des substances avec LMS]")
        st.write("Restrictions d'emploi: [Conditions spécifiques d'utilisation]")
    elif material == "Polyéthylène Téréphtalate (PET)":
        st.write("Liste positive: [Liste des substances autorisées pour le PET]")
        st.write("Limite de migration globale: 10 mg/dm²")
        st.write("Limite de migration spécifique: [Liste des substances avec LMS]")
        st.write("Restrictions d'emploi: [Conditions spécifiques d'utilisation]")
    # Add logic for other materials as needed
    else:
        st.write("Veuillez consulter le guide ACTIA for more details.")

# --- Logigramme 4: Mesures spécifiques françaises ---
def logigramme_4(material):
    st.subheader("Logigramme 4: Mesures spécifiques françaises")

    # Replace with detailed information from ACTIA Guide
    if material == "Aluminium":
        st.write("Teneur en aluminium ≥ 99%")
        st.write("Teneurs limites pour les impuretés: [Liste des impuretés et teneurs]")
    elif material == "Acier inoxydable":
        st.write("Teneur en chrome ≥ 13%")
        st.write("Teneurs limites pour d'autres éléments: [Liste des éléments et teneurs]")
    elif material == "Bois":
        st.write("Essences de bois autorisées: [Liste des essences]")
        st.write("Teneur en pentachlorophénol: [Limite de teneur]")
    # Add logic for other materials as needed
    else:
        st.write("Veuillez consulter le guide ACTIA for more details.")

# --- Logigramme 5: Recommandations françaises ---
def logigramme_5(material):
    st.subheader("Logigramme 5: Recommandations françaises")

    # Replace with detailed information from ACTIA Guide
    if material == "Papier/Carton":
        st.write("Matières cellulosiques recommandées: [Liste des matières]")
        st.write("Substances autorisées ou évaluées: [Liste des substances]")
    elif material == "Bois":
        st.write("Essences de bois supplémentaires: [Liste des essences]")
        st.write("Substances évaluées pour les vernis: [Liste des substances]")
    elif material == "Verre":
        st.write("Teneur en plomb, cadmium, arsenic: [Limites de teneur]")
    elif material == "Métal":
        st.write("Teneurs limites pour le plomb, cadmium, arsenic: [Limites de teneur]")
    elif material == "Acier inoxydable":
        st.write("Teneur en chrome ≥ 13%")
        st.write("Teneurs limites pour d'autres éléments: [Liste des éléments et teneurs]")
    elif material == "Aluminiums":
        st.write("Teneur en plomb, cadmium, arsenic: [Limites de teneur]")
    elif material == "Étain":
        st.write("Teneur en étain ≥ 97%")
        st.write("Teneur en antimoine et cuivre: [Limites de teneur]")
    elif material == "Zinc":
        st.write("Teneur en zinc ≥ 99.85%")
        st.write("Teneur en plomb, cadmium, arsenic: [Limites de teneur]")
    elif material == "Fonts":
        st.write("Teneur en plomb, cadmium, arsenic: [Limites de teneur]")
        st.write("Teneurs limites pour d'autres éléments: [Liste des éléments et teneurs]")
    elif material == "Métaux blanchis":
        st.write("Teneur en plomb, cadmium, arsenic: [Limites de teneur]")
        st.write("Teneurs limites pour d'autres éléments: [Liste des éléments et teneurs]")
    elif material == "Revêtements organiques ou métalliques":
        st.write("Substances évaluées pour les vernis: [Liste des substances]")
        st.write("Substances autorisées ou évaluées pour les revêtements de type 'plastique': [Liste des substances]")
    elif material == "Encres":
        st.write("Critères de composition des encres: [Liste des critères]")
    elif material == "Vernis de revêtement":
        st.write("Limites de migration globale: [Valeurs]")
        st.write("Limites de migration spécifique: [Valeurs]")
    # Add logic for other materials as needed
    else:
        st.write("Veuillez consulter le guide ACTIA for more details.")

# --- Main Execution ---
if choice == "Réglementation et Spécificités":
    logigramme_1()
elif choice == "Tests et Exigences":
    logigramme_2()
    if material in ["Polystyrène", "Polypropylène", "Polyéthylène", "PET"]:
        logigramme_3(material)
    if material in ["Aluminium", "Acier inoxydable", "Bois"]:
        logigramme_4(material)
    if material in ["Papier/Carton", "Bois", "Verre", "Métal", "Acier inoxydable", "Aluminiums", "Étain", "Zinc", "Fonts", "Métaux blanchis", "Revêtements organiques ou métalliques", "Encres", "Vernis de revêtement"]:
        logigramme_5(material)

# Final Conclusion
st.header("Conclusion")

st.write("Basé sur les informations fournies et l'analyse des logigrammes, la conclusion est:")

# Example conclusion - adapt based on the information provided
if choice == "Réglementation et Spécificités":
    st.write(f"L'emballage en {material} semble conforme aux exigences réglementaires générales et spécifiques. Cependant, il est important de vérifier la conformité en détail en consultant les textes légaux et les spécifications pour le matériau choisi.")

if choice == "Tests et Exigences":
    if tests and requirements:
        st.write(f"L'emballage en {material} pour {food_type} semble conforme aux exigences réglementaires et les tests nécessaires pourraient être: {', '.join(tests)}. Les exigences spécifiques sont: {', '.join(requirements)}.")
    elif tests:
        st.write(f"L'emballage en {material} pour {food_type} semble conforme aux exigences réglementaires et les tests nécessaires pourraient être: {', '.join(tests)}.")
    else:
        st.write(f"L'emballage en {material} pour {food_type} semble conforme aux exigences réglementaires.")

st.write(f"N'oubliez pas de prendre en compte le contexte de l'emballage: {purpose}, {client_needs}, {additional_info}.")
st.write("Cette conclusion est basée sur l'analyse des données disponibles. Il est crucial de mener des tests et d'obtenir une validation officielle pour garantir la sécurité de l'emballage.")
