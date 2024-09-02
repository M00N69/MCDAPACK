import streamlit as st

# Configuration de la page
st.set_page_config(layout="wide", page_title="Assistant Sécurité Emballages Alimentaires", initial_sidebar_state="expanded")

# CSS personnalisé pour la mise en forme
st.markdown(
    """
    <style>
    /* Couleur de fond de la barre latérale */
    [data-testid="stSidebar"] {
        background-color: #2398B2;
    }

    /* Couleur du texte du titre de la barre latérale */
    [data-testid="stSidebar"] h1 {
        color: black;
    }

    /* Couleur du texte des widgets de la barre latérale */
    [data-testid="stSidebar"] .css-17eq0hr {
        color: black;
    }

    /* Style de la bannière */
    .banner {
        background-image: url('https://github.com/M00N69/BUSCAR/blob/main/logo%2002%20copie.jpg?raw=true');
        background-size: cover;
        padding: 75px;
        text-align: center;
    }

    /* Style des tableaux */
    .dataframe td {
        white-space: normal !important;
        word-wrap: break-word !important;
    }

    /* Style du logo dans la barre latérale */
    .sidebar-logo-container {
        text-align: center;
        margin-top: 50px;
    }
    .sidebar-logo {
        width: 150px;
        height: auto;
    }
    </style>
    <div class="banner"></div>
    """,
    unsafe_allow_html=True
)

# Ajout du logo et du lien dans la barre latérale
st.sidebar.markdown(
    """
    <div class="sidebar-logo-container">
        <a href="https://www.visipilot.com" target="_blank">
            <img src="https://raw.githubusercontent.com/M00N69/RAPPELCONSO/main/logo%2004%20copie.jpg" alt="Visipilot Logo" class="sidebar-logo" style="width: 250px; height: auto;">
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
st.title("Assistant Sécurité Emballages Alimentaires")

# Informations contextuelles initiales
with st.expander("Contexte de l'Emballage", expanded=True):
    st.write("Veuillez fournir des informations supplémentaires pour une analyse plus précise.")
    purpose = st.text_input("Objectif de l'emballage (ex: conservation, protection, transport, etc.)")
    client_needs = st.text_area("Besoins spécifiques du client (ex: type d'aliment, conditions de stockage, etc.)")
    additional_info = st.text_area("Informations complémentaires (ex: présence de nanoparticules, etc.)")
# Menu latéral
st.sidebar.title("Navigation")
choice = st.sidebar.radio("Choisir un logigramme:", ("Réglementation et Spécificités", "Tests et Exigences"))
# --- Logigramme 1: Réglementation et Spécificités ---
if choice == "Réglementation et Spécificités":
    st.header("Logigramme 1: Réglementation et Spécificités selon le matériau")

    # Sélection du matériau
    materials = [
        "Aciers", "Aciers inoxydables", "Aluminium", "Alliages d'aluminium", 
        "Bois", "Caoutchoucs", "Céramiques", "Étain", "Fontes", "Grès - Porcelaine",
        "Matières plastiques", "Métaux blanchis", "Métaux et alliages de métaux", 
        "Objets en étain", "Papiers", "Pellicules de cellulose régénérée",
        "Produits de nettoyage des MCDA", "Silicones", "Verre", "Zinc", "Autres"
    ]
    material = st.selectbox("Sélectionner le matériau d'emballage:", materials)

    # Affichage des Réglementations et Spécifications
    st.subheader("Réglementations et Spécifications:")

    # Réglementations et spécifications détaillées pour chaque matériau
    if material == "Aciers":
        st.write("## Aciers")
        st.write("### Réglementations:")
        st.write("- Arrêté du 15 novembre 1945: MÉTAUX ET ALLIAGES")
        st.write("### Spécifications:")
        st.write("- Teneur en plomb, cadmium, arsenic, cobalt")
        st.write("- LLS des éléments ajoutés")
    elif material == "Aciers inoxydables":
        st.write("## Aciers inoxydables")
        st.write("### Réglementations:")
        st.write("- Arrêté du 15 novembre 1945: MÉTAUX ET ALLIAGES")
        st.write("- Arrêté du 13 janvier 1976: Aciers inoxydables")
        st.write("### Spécifications:")
        st.write("- Teneur en chrome ≥ 13%")
        st.write("- Teneurs limites en éléments ajoutés")
    elif material == "Aluminium":
        st.write("## Aluminium")
        st.write("### Réglementations:")
        st.write("- Arrêté du 15 novembre 1945: MÉTAUX ET ALLIAGES")
        st.write("- Arrêté du 27 août 1987: Aluminium et alliages d'aluminium")
        st.write("### Spécifications:")
        st.write("- Teneur en aluminium (>99%)")
        st.write("- Teneur en impuretés (≤ 1 %)")
    elif material == "Bois":
        st.write("## Bois")
        st.write("### Réglementations:")
        st.write("- Arrêté du 15 novembre 1945: Bois")
        st.write("### Spécifications:")
        st.write("- Liste des essences de bois autorisées au contact des aliments")
        st.write("- Teneur en pentachlorophénol")
    elif material == "Caoutchoucs":
        st.write("## Caoutchoucs")
        st.write("### Réglementations:")
        st.write("- Directive n° 93/11/CE: Caoutchoucs (tétines et sucettes)")
        st.write("- Arrêté du 9 novembre 1994: Caoutchoucs")
        st.write("- Arrêté du 9 août 2005: Caoutchoucs")
        st.write("- Arrêté du 19 décembre 2006: Caoutchoucs")
        st.write("### Spécifications:")
        st.write("- Listes positives (monomères et additifs)")
        st.write("- Matières organiques volatiles libres (≤ 0,5 %)")
        st.write("- Migration globale (LMG = 10 mg/dm² ou 60 mg/kg d'aliment)")
        st.write("- Formaldehyde (LMS = 3 mg/kg)")
        st.write("- Amines aromatiques primaires et secondaires (LMS = 1 mg/kg)")
        st.write("- N-nitrosamines (LMS = 1 µg/dm³)")
        st.write("- Substances N-nitrosables (LMS = 10 µg/dm³)")
        st.write("- Monomères avec LMS")
        st.write("- Additifs avec LMS")
        st.write("- Peroxydes")
    elif material == "Céramiques":
        st.write("## Céramiques")
        st.write("### Réglementations:")
        st.write("- Directive n° 84/500/CEE: Céramiques")
        st.write("- Directive n° 2005/31/CE: Céramiques")
        st.write("- Arrêté du 7 novembre 1985: Céramiques")
        st.write("- Arrêté du 23 mai 2006: Céramiques")
        st.write("### Spécifications:")
        st.write("- Limite de migration spécifique du plomb")
        st.write("- Limite de migration spécifique du cadmium")
        st.write("- Déclaration écrite de conformité")
    elif material == "Étain":
        st.write("## Étain")
        st.write("### Réglementations:")
        st.write("- Arrêté du 15 novembre 1945: MÉTAUX ET ALLIAGES")
        st.write("### Spécifications:")
        st.write("- Teneur en étain ≥ 97 %")
        st.write("- Teneur en antimoine et cuivre")
        st.write("- Teneur en plomb, cadmium, arsenic")
        st.write("- LLS des éléments ajoutés, en particulier : étain, plomb, cadmium, arsenic, antimoine, cuivre")
    elif material == "Fontes":
        st.write("## Fontes")
        st.write("### Réglementations:")
        st.write("- Arrêté du 15 novembre 1945: MÉTAUX ET ALLIAGES")
        st.write("### Spécifications:")
        st.write("- Teneur en plomb, cadmium, arsenic")
        st.write("- LLS des éléments ajoutés")
    elif material == "Grès - Porcelaine":
        st.write("## Grès - Porcelaine")
        st.write("### Réglementations:")
        st.write("- Directive n° 84/500/CEE: Céramiques")
        st.write("- Directive n° 2005/31/CE: Céramiques")
        st.write("### Spécifications:")
        st.write("- Limite de migration spécifique du plomb et du cadmium")
        st.write("- Déclaration écrite de conformité")
    elif material == "Matières plastiques":
        st.write("## Matières plastiques")
        st.write("### Réglementations:")
        st.write("- Règlement (UE) n° 10/2011: Plastiques")
        st.write("- Directive 2002/72/CE: Plastiques")
        st.write("### Spécifications:")
        st.write("- Migration globale (LMG = 10 mg/dm² ou 60 mg/kg d'aliment)")
        st.write("- Migration spécifique (en mg/kg d'aliment)")
        st.write("- Listes positives (monomères et additifs)")
    elif material == "Métaux blanchis":
        st.write("## Métaux blanchis")
        st.write("### Réglementations:")
        st.write("- Arrêté du 15 novembre 1945: MÉTAUX ET ALLIAGES")
        st.write("### Spécifications:")
        st.write("- Teneur en plomb, cadmium, arsenic")
        st.write("- LLS des éléments ajoutés, en particulier : plomb, cadmium")
    elif material == "Métaux et alliages de métaux":
        st.write("## Métaux et alliages de métaux")
        st.write("### Réglementations:")
        st.write("- Arrêté du 15 novembre 1945: MÉTAUX ET ALLIAGES")
        st.write("### Spécifications:")
        st.write("- LLS des éléments ajoutés")
    elif material == "Objets en étain":
        st.write("## Objets en étain")
        st.write("### Réglementations:")
        st.write("- Arrêté du 15 novembre 1945: MÉTAUX ET ALLIAGES")
        st.write("### Spécifications:")
        st.write("- Teneur en étain ≥ 97 %")
        st.write("- Teneur en antimoine et cuivre")
        st.write("- Teneur en plomb, cadmium, arsenic")
        st.write("- LLS des éléments ajoutés, en particulier : étain, plomb, cadmium, arsenic, antimoine, cuivre")
    elif material == "Papiers":
        st.write("## Papiers")
        st.write("### Réglementations:")
        st.write("- Arrêté du 15 novembre 1945: Papiers")
        st.write("### Spécifications:")
        st.write("- Teneur en pentachlorophénol")
        st.write("- Teneur en polychlorobiphényles")
        st.write("- Migration du formol, glyoxal, fluor")
    elif material == "Pellicules de cellulose régénérée":
        st.write("## Pellicules de cellulose régénérée")
        st.write("### Réglementations:")
        st.write("- Directive 2007/42/CE: Pellicules de cellulose régénérée")
        st.write("### Spécifications:")
        st.write("- Matières organiques volatiles libres (≤ 0,5 %)")
        st.write("- Migration globale (LMG = 10 mg/dm² ou 60 mg/kg d'aliment)")
        st.write("- Formaldehyde (LMS = 3 mg/kg)")
        st.write("- Amines aromatiques primaires et secondaires (LMS = 1 mg/kg)")
        st.write("- N-nitrosamines (LMS = 1 µg/dm³)")
        st.write("- Substances N-nitrosables (LMS = 10 µg/dm³)")
        st.write("- Listes positives (monomères et additifs)")
    elif material == "Produits de nettoyage des MCDA":
        st.write("## Produits de nettoyage des MCDA")
        st.write("### Réglementations:")
        st.write("- Arrêté du 19 décembre 2013: Produits de nettoyage des matériaux en contact avec les denrées alimentaires")
        st.write("### Spécifications:")
        st.write("- Dossier de demande d'autorisation de substance")
        st.write("- Restriction d'emploi concernant les produits de rinçage")
        st.write("- Liste positive")
    elif material == "Silicones":
        st.write("## Silicones")
        st.write("### Réglementations:")
        st.write("- Directive 2002/72/CE: Silicones")
        st.write("### Spécifications:")
        st.write("- Matières organiques volatiles libres (≤ 0,5%)")
        st.write("- Migration globale (LMG= 10 mg/dm³ ou 60 mg/kg d'aliment)")
        st.write("- Organo-étains (LMS = 0,1 mg/kg)")
        st.write("- Peroxydes")
    elif material == "Verre":
        st.write("## Verre")
        st.write("### Réglementations:")
        st.write("- Directive 84/500/CEE: Verre")
        st.write("### Spécifications:")
        st.write("- LMS pour le plomb et cadmium")
    elif material == "Zinc":
        st.write("## Zinc")
        st.write("### Réglementations:")
        st.write("- Arrêté du 15 novembre 1945: MÉTAUX ET ALLIAGES")
        st.write("### Spécifications:")
        st.write("- Teneur en zinc ≥ 99 %")
        st.write("- Teneur en plomb, cadmium, arsenic")
        st.write("- LLS des éléments ajoutés")
    elif material == "Autres":
        st.write("## Autres Matériaux")
        st.write("### Réglementations:")
        st.write("Les réglementations spécifiques seront appliquées en fonction du type de matériau non répertorié.")
        st.write("### Spécifications:")
        st.write("Les spécifications seront définies en fonction du matériau sélectionné.")


    # Exportation des résultats
    st.download_button(
        label="Télécharger les résultats",
        data=st.session_state.get("results_reglementation", "Aucun résultat à exporter"),
        file_name="results_reglementation.txt",
        mime="text/plain"
    )
# Logigramme 2: Tests et Exigences
elif choice == "Tests et Exigences":
    st.header("Logigramme 2: Tests et Exigences selon le matériau et l'aliment")

    # Sélection du matériau
    materials = [
        "Aciers", "Aciers inoxydables", "Aluminium", "Alliages d'aluminium", 
        "Bois", "Caoutchoucs", "Céramiques", "Étain", "Fontes", "Grès - Porcelaine",
        "Matières plastiques", "Métaux blanchis", "Métaux et alliages de métaux", 
        "Objets en étain", "Papiers ET CARTONS", "Pellicules de cellulose régénérée",
        "Produits de nettoyage des MCDA", "Silicones", "Verre, cristal, vitrocéramique", 
        "Objets émaillés et décorés", "Zinc", "Autres"
    ]
    material = st.selectbox("Sélectionner le matériau d'emballage:", materials)

    # Sélection du type d'aliment
    food_types = ["Aqueux pH > 4.5", "Acide", "Gras", "Sec", "Autres"]
    food_type = st.selectbox("Sélectionner le type d'aliment:", food_types)

    # Questions pour identifier les tests et exigences
    st.subheader("Questions pour identifier les tests et exigences:")
    questions = []
    
    if material in [
        "Aciers", "Aciers inoxydables", "Aluminium", "Alliages d'aluminium", 
        "Bois", "Caoutchoucs", "Céramiques", "Étain", "Fontes", 
        "Grès - Porcelaine", "Métaux blanchis", "Métaux et alliages de métaux", 
        "Objets en étain", "Pellicules de cellulose régénérée", "Silicones", 
        "Verre, cristal, vitrocéramique", "Objets émaillés et décorés", "Zinc"
    ]:
        questions.extend([
            "Le matériau est-il en contact direct avec l'aliment ?",
            "Le matériau est-il soumis à un traitement thermique ?",
            "Quelle est la température maximale du traitement thermique (en °C) ?",
            "Quelle est la durée maximale du traitement thermique (en minutes) ?",
            "Quelle est la durée de conservation du produit (DLC ou DLUO) (en jours) ?"
        ])
        if material in ["Matières plastiques", "Pellicules de cellulose régénérée"]:
            questions.extend([
                "Y a-t-il une barrière fonctionnelle ?",
                "Le matériau est-il composé de plusieurs couches ?",
                "Le matériau est-il recyclé ?",
                "Le matériau est-il actif ou intelligent ?"
            ])
        if material == "Bois":
            questions.append("Le matériau est-il traité ?")
        if material in ["Métaux et alliages de métaux", "Objets en étain"]:
            questions.append("Le matériau est-il traité (ex: étamé, galvanisé, etc.) ?")
        if material == "Verre, cristal, vitrocéramique":
            questions.append("Le matériau est-il décoré ou imprimé ?")
        if material in ["Céramiques", "Verre, cristal, vitrocéramique"]:
            questions.append("Le matériau est-il en contact avec des aliments acides ?")
    elif material == "Papiers ET CARTONS":
        questions.extend([
            "Le matériau est-il en contact direct avec l'aliment ?",
            "Le matériau est-il composé de fibres recyclées ?",
            "Le matériau est-il imprimé ?",
            "Le matériau est-il en contact avec des aliments humides ou gras ?"
        ])
    else:
        questions.extend([
            "Le matériau est-il en contact direct avec l'aliment ?",
            "Le matériau est-il composé de plusieurs couches ?"
        ])

    answers = []
    for question in questions:
        if question.startswith("Quelle est"):
            answer = st.text_input(question)
        else:
            answer = st.radio(question, ("Oui", "Non"))
        answers.append(answer)

    # Tests et Exigences
    st.subheader("Tests et Exigences:")
    tests = []
    requirements = []

    # Logique pour déterminer les tests et exigences
    if material in [
        "Aciers", "Aciers inoxydables", "Aluminium", "Alliages d'aluminium", 
        "Bois", "Caoutchoucs", "Céramiques", "Étain", "Fontes", 
        "Grès - Porcelaine", "Métaux blanchis", "Métaux et alliages de métaux", 
        "Objets en étain", "Pellicules de cellulose régénérée", "Silicones", 
        "Verre, cristal, vitrocéramique", "Objets émaillés et décorés", "Zinc"
    ]:
        if len(answers) > 0 and answers[0] == "Oui":  # Contact direct
            if len(answers) > 1 and answers[1] == "Oui":  # Traitement thermique
                tests.extend(["Migration globale", "Migration spécifique"])
                requirements.extend(["Limite de migration globale (10 mg/dm²)", "Limite de migration spécifique pour les substances concernées"])

                if len(answers) > 2 and answers[2]:
                    try:
                        temperature_max = float(answers[2])
                        if temperature_max > 100:
                            tests.append("Migration spécifique pour les substances sensibles à la chaleur")
                    except ValueError:
                        st.warning("Veuillez entrer une valeur numérique valide pour la température maximale du traitement thermique.")
            else:
                tests.append("Migration spécifique pour les substances concernées")

            if len(answers) > 4 and answers[4]:
                try:
                    conservation_duree = int(answers[4])
                    if conservation_duree > 0:
                        tests.append("Tests organoleptiques")
                except ValueError:
                    st.warning("Veuillez entrer une valeur numérique valide pour la durée de conservation.")

        if material == "Bois" and len(answers) > 5 and answers[5] == "Oui":  # Traitement du bois
            requirements.append("Vérifier la conformité du traitement du bois (ex: pentachlorophénol).")
        
        if material in ["Métaux et alliages de métaux", "Objets en étain"] and len(answers) > 5 and answers[5] == "Oui":  # Traitement du métal
            requirements.append("Vérifier la conformité du traitement du métal (ex: étamé, galvanisé).")
        
        if material == "Verre, cristal, vitrocéramique" and len(answers) > 5 and answers[5] == "Oui":  # Décoré ou imprimé
            requirements.append("Vérifier la conformité des décors et des encres.")
        
        if material in ["Céramiques", "Verre, cristal, vitrocéramique"] and len(answers) > 6 and answers[6] == "Oui":  # Contact avec des aliments acides
            requirements.append("Vérifier la conformité aux limites de migration spécifique pour le plomb et le cadmium (céramiques) ou le plomb (verre).")
    
    elif material == "Papiers ET CARTONS":
        if len(answers) > 0 and answers[0] == "Oui":  # Contact direct
            requirements.append("Vérifier la teneur en pentachlorophénol.")
            requirements.append("Vérifier la teneur en polychlorobiphenyls.")
            requirements.append("Vérifier la migration du formol, glyoxal, fluor.")
            if len(answers) > 3 and answers[3] == "Oui":  # Contact avec des aliments humides ou gras
                requirements.append("Vérifier la migration des azurants optiques.")
                requirements.append("Vérifier la migration des colorants.")
        if len(answers) > 1 and answers[1] == "Oui":  # Composé de fibres recyclées
            requirements.append("Vérifier l'origine des fibres recyclées.")
        if len(answers) > 2 and answers[2] == "Oui":  # Imprimé
            requirements.append("Vérifier la conformité des encres d'impression.")

    elif material == "Matières plastiques":
        if len(answers) > 5 and answers[5] == "Oui":  # Barrière fonctionnelle
            requirements.append("Vérifier la performance de la barrière fonctionnelle.")
        if len(answers) > 6 and answers[6] == "Oui":  # Plusieurs couches
            tests.append("Migration spécifique pour chaque couche.")
        if len(answers) > 7 and answers[7] == "Oui":  # Recyclé
            requirements.append("Vérifier la conformité du processus de recyclage (Règlement (CE) n° 282/2008).")
        if len(answers) > 8 and answers[8] == "Oui":  # Actif ou intelligent
            requirements.append("Vérifier la conformité du matériau actif/intelligent aux règlements spécifiques (Règlement (CE) n° 450/2009).")

    elif material == "Pellicules de cellulose régénérée":
        if len(answers) > 5 and answers[5] == "Oui":  # Barrière fonctionnelle
            requirements.append("Vérifier la performance de la barrière fonctionnelle.")
        if len(answers) > 6 and answers[6] == "Oui":  # Plusieurs couches
            tests.append("Migration spécifique pour chaque couche.")
        if len(answers) > 7 and answers[7] == "Oui":  # Recyclé
            requirements.append("Vérifier la conformité du processus de recyclage.")
        if len(answers) > 8 and answers[8] == "Oui":  # Actif ou intelligent
            requirements.append("Vérifier la conformité du matériau actif/intelligent aux règlements spécifiques.")

    elif material == "Aluminium":
        if len(answers) > 0 and answers[0] == "Oui":  # Contact direct
            if len(answers) > 2 and answers[2]:
                try:
                    teneur_aluminium = float(answers[2])
                    if teneur_aluminium < 99:  # Teneur en aluminium
                        requirements.append("Vérifier la conformité de la teneur en aluminium (>99%).")
                except ValueError:
                    st.warning("Veuillez entrer une valeur numérique valide pour la teneur en aluminium.")
            if len(answers) > 3 and answers[3]:
                try:
                    teneur_impuretes = float(answers[3])
                    if teneur_impuretes > 1:  # Teneur en impuretés
                        requirements.append("Vérifier la conformité de la teneur en impuretés (≤1%).")
                except ValueError:
                    st.warning("Veuillez entrer une valeur numérique valide pour la teneur en impuretés.")
    
    elif material == "Caoutchoucs":
        if len(answers) > 0 and answers[0] == "Oui":  # Contact direct
            requirements.append("Limite de migration des nitrosamines dans la salive = 0,01 mg/kg de matériau")
            requirements.append("Limite de migration des substances N-nitrosables dans la salive = 0,1 mg/kg de matériau")
    
    elif material == "Silicones":
        if len(answers) > 0 and answers[0] == "Oui":  # Contact direct
            requirements.append("Matières organiques volatiles libres (≤ 0,5%)")
            requirements.append("Migration globale (LMG= 10 mg/dm³ ou 60 mg/kg d'aliment)")
            requirements.append("Organo-étains (LMS = 0,1 mg/kg)")
            requirements.append("Peroxydes")
    
    elif material == "DÉRIVÉS ÉPOXYDIQUES DES VERNIS":
        requirements.append("BFDGE et NOGE non autorisés")
        requirements.append("LMS des dérivés H₂O du Badge = 9 mg/kg")
        requirements.append("LMS des dérivés du HCI du Badge = 1 mg/kg")
    
    elif material == "Céramiques":
        requirements.append("Limite de migration spécifique du plomb")
        requirements.append("Limite de migration spécifique du cadmium")
        requirements.append("Déclaration écrite de conformité")
    
    elif material == "MCDA TRAITÉS PAR RAYONNEMENTS IONISANTS":
        if len(answers) > 2 and answers[2]:
            try:
                dose_traitement = float(answers[2])
                if dose_traitement < 10:  # Dose de traitement
                    requirements.append("Dossier de demande d'autorisation de traitement pour doses inférieures à 10 kGy.")
                else:
                    requirements.append("Dossier de demande d'autorisation de traitement pour doses supérieures à 10 kGy.")
            except ValueError:
                st.warning("Veuillez entrer une valeur numérique valide pour la dose de traitement.")
    
    elif material == "Produits de nettoyage des MCDA":
        requirements.append("Dossier de demande d'autorisation de substance.")
        requirements.append("Restriction d'emploi concernant les produits de rinçage.")
        requirements.append("Liste positive.")

    # Affichage des résultats
    st.write(f"**Tests recommandés:** {', '.join(tests)}")
    st.write(f"**Exigences spécifiques:** {', '.join(requirements)}")

    # Exportation des résultats
    st.download_button(
        label="Télécharger les résultats",
        data=st.session_state.get("results_tests", "Aucun résultat à exporter"),
        file_name="results_tests.txt",
        mime="text/plain"
    )


