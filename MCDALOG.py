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

if choice == "Réglementation et Spécificités":
    st.header("Logigramme 1: Réglementation et Spécificités selon le matériau")

    # Define packaging materials
    materials = ["Polystyrène", "Polypropylène", "Polyéthylène", "Polyéthylène Téréphtalate (PET)", "Aluminium", 
                 "Papier/Carton", "Bois", "Métal", "Verre", "Céramique", "Pellicule de cellulose régénérée", "Autres"]
    material = st.selectbox("Sélectionner le matériau d'emballage:", materials)

    # Display applicable regulations
    st.subheader("Règlements applicables:")

    # EU Regulations
    st.write("**Règlement (CE) No 1935/2004:** Règles générales pour les matériaux au contact des aliments.")
    if material == "Polystyrène" or material == "Polypropylène" or material == "Polyéthylène" or material == "PET":
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
    if material == "Pellicule de cellulose régénérée":
        st.write("**Directive 2007/42/CE:** Règles spécifiques pour la pellicule de cellulose régénérée.")

    # French Regulations
    st.write("**Décret No. 2007-766:** Application du code de la consommation.")
    st.write("**Décret No. 2008-1469:**  Modifie le Décret 2007-766.")

    # Display specific specifications
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


elif choice == "Tests et Exigences":
    st.header("Logigramme 2: Tests et Exigences selon le matériau et l'aliment")

    # Define packaging materials
    materials = ["Polystyrène", "Polypropylène", "Polyéthylène", "Polyéthylène Téréphtalate (PET)", "Aluminium", 
                 "Papier/Carton", "Bois", "Métal", "Verre", "Céramique", "Pellicule de cellulose régénérée", "Autres"]
    material = st.selectbox("Sélectionner le matériau d'emballage:", materials)

    # Define the food types
    food_types = ["Aqueux pH > 4.5", "Acide", "Gras", "Sec", "Autres"]
    food_type = st.selectbox("Sélectionner le type d'aliment:", food_types)

    # Questions
    st.subheader("Questions pour identifier les tests et exigences:")

    # Logigramme 2 (Décret 2008-1469)
    questions_logigramme2 = [
        "Le matériau est-il en contact direct avec l'aliment ?",
        "Le matériau est-il soumis à un traitement thermique ?",
        "Quelle est la température maximale du traitement thermique ?",  # Ask only if thermal treatment is yes
        "Quelle est la durée maximale du traitement thermique ?", # Ask only if thermal treatment is yes
        "Quelle est la durée de conservation du produit (DLC ou DLUO) ?" 
    ]
    answers_logigramme2 = []
    for question in questions_logigramme2:
        answer = st.radio(question, ("Oui", "Non"))
        answers_logigramme2.append(answer)

    # Logigramme 3 (Mesures spécifiques)
    questions_logigramme3 = [
        "Y a-t-il une barrière fonctionnelle ?",
        "Le matériau est-il composé de plusieurs couches ?",
        "Le matériau est-il recyclé ?",
        "Le matériau est-il actif ou intelligent ?"
    ]
    answers_logigramme3 = []
    for question in questions_logigramme3:
        answer = st.radio(question, ("Oui", "Non"))
        answers_logigramme3.append(answer)

    # Logigramme 4 (Mesures spécifiques françaises)
    questions_logigramme4 = []
    answers_logigramme4 = []
    if material == "Aluminium":
        questions_logigramme4 = [
            "La teneur en aluminium est-elle supérieure à 99% ?",
            "La teneur en impuretés est-elle inférieure à 1% ?"
        ]
        for question in questions_logigramme4:
            answer = st.radio(question, ("Oui", "Non"))
            answers_logigramme4.append(answer)
    elif material == "Acier":
        questions_logigramme4 = [
            "La teneur en chrome est-elle supérieure à 13% ?"
        ]
        for question in questions_logigramme4:
            answer = st.radio(question, ("Oui", "Non"))
            answers_logigramme4.append(answer)
    elif material == "Bois":
        questions_logigramme4 = [
            "Le bois appartient-il à la liste des essences autorisées ?",
            "Le bois est-il traité (ex: par pentachlorophénol) ?"
        ]
        for question in questions_logigramme4:
            answer = st.radio(question, ("Oui", "Non"))
            answers_logigramme4.append(answer)
    elif material == "Papier/Carton":
        questions_logigramme4 = [
            "Le matériau est-il composé de fibres recyclées ?"
        ]
        for question in questions_logigramme4:
            answer = st.radio(question, ("Oui", "Non"))
            answers_logigramme4.append(answer)

    # Logigramme 5 (Recommandations françaises)
    questions_logigramme5 = []
    answers_logigramme5 = []
    if material == "Aluminium":
        questions_logigramme5 = [
            "Le matériau est-il laqué ?"
        ]
        for question in questions_logigramme5:
            answer = st.radio(question, ("Oui", "Non"))
            answers_logigramme5.append(answer)
    elif material == "Acier":
        questions_logigramme5 = [
            "Le matériau est-il laqué ?"
        ]
        for question in questions_logigramme5:
            answer = st.radio(question, ("Oui", "Non"))
            answers_logigramme5.append(answer)
    elif material == "Verre":
        questions_logigramme5 = [
            "Le matériau est-il en contact avec des aliments acides ?",
            "Le matériau est-il décoré ou imprimé ?"
        ]
        for question in questions_logigramme5:
            answer = st.radio(question, ("Oui", "Non"))
            answers_logigramme5.append(answer)
    elif material == "Céramique":
        questions_logigramme5 = [
            "Le matériau est-il en contact avec des aliments acides ?"
        ]
        for question in questions_logigramme5:
            answer = st.radio(question, ("Oui", "Non"))
            answers_logigramme5.append(answer)
    elif material == "Papier/Carton":
        questions_logigramme5 = [
            "Le matériau est-il imprimé ?",
            "Le matériau est-il en contact avec des aliments humides ou gras ?"
        ]
        for question in questions_logigramme5:
            answer = st.radio(question, ("Oui", "Non"))
            answers_logigramme5.append(answer)
    elif material == "Bois":
        questions_logigramme5 = [
            "Le matériau est-il en contact avec des aliments humides ou gras ?"
        ]
        for question in questions_logigramme5:
            answer = st.radio(question, ("Oui", "Non"))
            answers_logigramme5.append(answer)

    # Process answers to determine tests and requirements
    st.subheader("Tests et Exigences:")
    tests = []
    requirements = []

    # Logigramme 2 (Décret 2008-1469)
    if answers_logigramme2[0] == "Oui":  # Contact Direct
        if answers_logigramme2[1] == "Oui":  # Thermal Treatment
            tests.append("Migration globale")
            tests.append("Migration spécifique")
            requirements.append("Limite de migration globale (10 mg/dm²)")
            requirements.append("Limite de migration spécifique pour les substances concernées")
        else:
            tests.append("Migration spécifique pour les substances concernées")
        if answers_logigramme2[4] == "Oui": # DLC/DLUO
            tests.append("Tests organoleptiques")
        if answers_logigramme2[1] == "Oui": # Thermal Treatment
            if answers_logigramme2[2] == "Oui":  # Thermal Treatment Max Temp
                temp_input = st.text_input("Température maximale du traitement thermique (en °C)")
                if temp_input:  # Check if the input is not empty
                    max_temp = int(temp_input)
                    if max_temp > 100:
                        tests.append("Migration spécifique pour les substances sensibles à la chaleur")
                else:
                    st.write("Veuillez entrer la température maximale du traitement thermique.")

    # Logigramme 3 (Mesures spécifiques)
    if material in ["Polystyrène", "Polypropylène", "Polyéthylène", "PET"]:
        if answers_logigramme3[0] == "Oui": # Barrier Function
            requirements.append("Vérifier la performance de la barrière fonctionnelle.")
        if answers_logigramme3[1] == "Oui": # MultiLayer
            tests.append("Migration spécifique pour chaque couche")
        if answers_logigramme3[2] == "Oui": # Recycled
            requirements.append("Vérifier la conformité du processus de recyclage.")
        if answers_logigramme3[3] == "Oui": # Active
            requirements.append("Vérifier la conformité du matériau actif/intelligent aux règlements spécifiques.")
    if material == "Céramique":
        if answers_logigramme5[0] == "Oui":  # Contact Direct
            requirements.append("Vérifier la conformité aux limites de migration spécifique pour le plomb et le cadmium (Directive 2005/31/CE).")
    if material == "Pellicule de cellulose régénérée":
        if answers_logigramme5[0] == "Oui":  # Contact Direct
            requirements.append("Vérifier la conformité aux limites de migration spécifique pour les monomères et les additifs (Directive 2007/42/CE).")
    if material == "Papier/Carton":
        if answers_logigramme4[0] == "Oui": # Recycled Fibers
            requirements.append("Vérifier l'origine des fibres recyclées.")

    # Logigramme 4 (Mesures spécifiques françaises)
    if material == "Aluminium":
        if answers_logigramme4[0] == "Oui": # Aluminium Content
            requirements.append("Vérifier la conformité de la teneur en aluminium (Arrêté du 27 août 1987).")
        if answers_logigramme4[1] == "Oui": # Impurities Content
            requirements.append("Vérifier la conformité de la teneur en impuretés (Arrêté du 27 août 1987).")
        if answers_logigramme5[0] == "Oui": # Lacquered
            requirements.append("Vérifier la conformité aux recommandations françaises pour les revêtements organiques ou métalliques (Arrêté du 27 août 1987).")
    if material == "Acier":
        if answers_logigramme4[0] == "Oui": # Chrome Content
            requirements.append("Vérifier la conformité de la teneur en chrome (Arrêté du 13 janvier 1976).")
        if answers_logigramme5[0] == "Oui": # Lacquered
            requirements.append("Vérifier la conformité aux recommandations françaises pour les revêtements organiques ou métalliques (Arrêté du 13 janvier 1976).")
    if material == "Bois":
        if answers_logigramme4[0] == "Oui": # Wood Type
            requirements.append("Vérifier la conformité du type de bois (Arrêté du 15 novembre 1945).")
        if answers_logigramme4[1] == "Oui": # Wood Treatment
            requirements.append("Vérifier la conformité du traitement du bois (Arrêté du 15 novembre 1945).")
        if answers_logigramme5[2] == "Oui": # HumidOrFattyFood
            requirements.append("Vérifier la résistance du matériau aux aliments humides ou gras.")
    if material == "Métal":
        if answers_logigramme2[0] == "Oui":  # Contact Direct
            requirements.append("Vérifier la conformité aux restrictions d'emploi pour les métaux (ex: cuivre, zinc galvanisé) (Arrêté du 28 juin 1912).")
            requirements.append("Vérifier la conformité aux limites de migration spécifique (mg/kg d'aliment) pour les éléments ajoutés (Arrêté du 28 juin 1912).")
        if answers_logigramme2[1] == "Oui":  # Thermal Treatment
            if answers_logigramme2[2] == "Oui":  # Thermal Treatment Max Temp
                temp_input = st.text_input("Température maximale du traitement thermique (en °C)")
                if temp_input:  # Check if the input is not empty
                    max_temp = int(temp_input)
                    if max_temp > 100:
                        tests.append("Migration spécifique pour les substances sensibles à la chaleur")
                else:
                    st.write("Veuillez entrer la température maximale du traitement thermique.")
    if material == "Verre":
        if answers_logigramme5[0] == "Oui": # Acidic Food
            requirements.append("Vérifier la conformité aux limites de migration spécifique pour le plomb (Arrêté du 15 novembre 1945).")
        if answers_logigramme5[1] == "Oui": # Decorated
            requirements.append("Vérifier la conformité des pigments et des encres utilisés (Arrêté du 15 novembre 1945).")

    # Logigramme 5 (Recommandations françaises)
    if material == "Papier/Carton":
        if answers_logigramme5[0] == "Oui": # Printed
            requirements.append("Vérifier la conformité des encres d'impression.")
        if answers_logigramme5[1] == "Oui": # HumidOrFattyFood
            requirements.append("Vérifier la résistance du matériau aux aliments humides ou gras.")
    
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
