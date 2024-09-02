import streamlit as st

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
if choice == "Réglementation et Spécificités":
    st.header("Logigramme 1: Réglementation et Spécificités selon le matériau")

    # Material Selection
    materials = [
        "Aciers", "Aciers inoxydables", "Aluminium", "Alliages d'aluminium", 
        "Bois", "Caoutchoucs", "Céramiques", "Étain", "Fontes", "Grès - Porcelaine",
        "Matières plastiques", "Métaux blanchis", "Métaux et alliages de métaux", 
        "Objets en étain", "Papiers", "Pellicules de cellulose régénérée",
        "Produits de nettoyage des MCDA", "Silicones", "Verre", "Zinc", "Autres"
    ]
    material = st.selectbox("Sélectionner le matériau d'emballage:", materials)

    # Display Regulations and Specifications
    st.subheader("Réglementations et Spécifications:")
    # --- Detailed Regulations and Specifications for each Material ---
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
    # ... (continuer avec les autres matériaux selon le même schéma)
    
    # Export Results
    st.download_button(
        label="Télécharger les résultats",
        data=st.session_state.get("results_reglementation", "Aucun résultat à exporter"),
        file_name="results_reglementation.txt",
        mime="text/plain"
    )
# --- Logigramme 2: Tests et Exigences ---
elif choice == "Tests et Exigences":
    st.header("Logigramme 2: Tests et Exigences selon le matériau et l'aliment")

    # Material Selection
    materials = [
        "Aciers", "Aciers inoxydables", "Aluminium", "Alliages d'aluminium", 
        "Bois", "Caoutchoucs", "Céramiques", "Étain", "Fontes", "Grès - Porcelaine",
        "Matières plastiques", "Métaux blanchis", "Métaux et alliages de métaux", 
        "Objets en étain", "Papiers ET CARTONS", "Pellicules de cellulose régénérée",
        "Produits de nettoyage des MCDA", "Silicones", "Verre, cristal, vitrocéramique", 
        "Objets émaillés et décorés", "Zinc", "Autres"
    ]
    material = st.selectbox("Sélectionner le matériau d'emballage:", materials)

    # Food Type Selection
    food_types = ["Aqueux pH > 4.5", "Acide", "Gras", "Sec", "Autres"]
    food_type = st.selectbox("Sélectionner le type d'aliment:", food_types)

    # Questions
    st.subheader("Questions pour identifier les tests et exigences:")

    # Questions based on material and food type
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
        if material in ["Métaux et alliages de métaux", "Objets en étain", "Aciers étamés - aciers galvanisés cuivre - zinc - plomb - arsenic"]:
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

    # Answers
    answers = []
    for question in questions:
        if question.startswith("Quelle est"):
            answer = st.text_input(question)
        else:
            answer = st.radio(question, ("Oui", "Non"))
        answers.append(answer)

    # Tests and Requirements
    st.subheader("Tests et Exigences:")
    tests = []
    requirements = []

    # --- Logigramme 2: Tests et Exigences ---
elif choice == "Tests et Exigences":
    st.header("Logigramme 2: Tests et Exigences selon le matériau et l'aliment")

    # Material Selection
    materials = [
        "Aciers", "Aciers inoxydables", "Aluminium", "Alliages d'aluminium", 
        "Bois", "Caoutchoucs", "Céramiques", "Étain", "Fontes", "Grès - Porcelaine",
        "Matières plastiques", "Métaux blanchis", "Métaux et alliages de métaux", 
        "Objets en étain", "Papiers ET CARTONS", "Pellicules de cellulose régénérée",
        "Produits de nettoyage des MCDA", "Silicones", "Verre, cristal, vitrocéramique", 
        "Objets émaillés et décorés", "Zinc", "Autres"
    ]
    material = st.selectbox("Sélectionner le matériau d'emballage:", materials)

    # Food Type Selection
    food_types = ["Aqueux pH > 4.5", "Acide", "Gras", "Sec", "Autres"]
    food_type = st.selectbox("Sélectionner le type d'aliment:", food_types)

    # Questions
    st.subheader("Questions pour identifier les tests et exigences:")

    # Questions based on material and food type
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
        if material in ["Métaux et alliages de métaux", "Objets en étain", "Aciers étamés - aciers galvanisés cuivre - zinc - plomb - arsenic"]:
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

    # Answers
    answers = []
    for question in questions:
        if question.startswith("Quelle est"):
            answer = st.text_input(question)
        else:
            answer = st.radio(question, ("Oui", "Non"))
        answers.append(answer)

    # Tests and Requirements
    st.subheader("Tests et Exigences:")
    tests = []
    requirements = []

    # --- Logigramme 2 Logic ---
    if material in [
        "Aciers", "Aciers inoxydables", "Aluminium", "Alliages d'aluminium", 
        "Bois", "Caoutchoucs", "Céramiques", "Étain", "Fontes", 
        "Grès - Porcelaine", "Métaux blanchis", "Métaux et alliages de métaux", 
        "Objets en étain", "Pellicules de cellulose régénérée", "Silicones", 
        "Verre, cristal, vitrocéramique", "Objets émaillés et décorés", "Zinc"
    ]:
        if answers[0] == "Oui":  # Contact direct
            if answers[1] == "Oui":  # Traitement thermique
                tests.extend(["Migration globale", "Migration spécifique"])
                requirements.extend(["Limite de migration globale (10 mg/dm²)", "Limite de migration spécifique pour les substances concernées"])
                # --- Error Handling for Temperature Input ---
                if answers[2] and answers[2].isdigit():  # Check if input is not empty and is a number
                    if int(answers[2]) > 100:  # Température maximale du traitement thermique
                        tests.append("Migration spécifique pour les substances sensibles à la chaleur")
                else:
                    st.warning("Veuillez entrer une valeur numérique pour la température maximale du traitement thermique.")
            else:
                tests.append("Migration spécifique pour les substances concernées")
            if answers[4] and answers[4].isdigit():
                if int(answers[4]) > 0:  # Durée de conservation (DLC ou DLUO)
                    tests.append("Tests organoleptiques")
        if material == "Bois":
            if len(answers) > 5 and answers[5] == "Oui":  # Traitement du bois
                requirements.append("Vérifier la conformité du traitement du bois (ex: pentachlorophénol).")
        if material in ["Métaux et alliages de métaux", "Objets en étain"]:
            if len(answers) > 5 and answers[5] == "Oui":  # Traitement du métal
                requirements.append("Vérifier la conformité du traitement du métal (ex: étamé, galvanisé).")
        if material == "Verre, cristal, vitrocéramique":
            if len(answers) > 5 and answers[5] == "Oui":  # Décoré ou imprimé
                requirements.append("Vérifier la conformité des décors et des encres.")
        if material in ["Céramiques", "Verre, cristal, vitrocéramique"]:
            if len(answers) > 6 and answers[6] == "Oui":  # Contact avec des aliments acides
                requirements.append("Vérifier la conformité aux limites de migration spécifique pour le plomb et le cadmium (céramiques) ou le plomb (verre).")
    elif material == "Papiers ET CARTONS":
        if answers[0] == "Oui":  # Contact direct
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

    # --- Logigramme 3 Logic ---
    if material == "Matières plastiques":
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

    # --- Logigramme 4 Logic ---
    if material == "Aluminium":
        if answers[0] == "Oui":  # Contact direct
            if answers[2] and answers[2].isdigit():
                if float(answers[2]) < 99:  # Teneur en aluminium
                    requirements.append("Vérifier la conformité de la teneur en aluminium (>99%).")
            else:
                st.warning("Veuillez entrer une valeur numérique pour la teneur en aluminium.")
            if answers[3] and answers[3].isdigit():
                if float(answers[3]) > 1:  # Teneur en impuretés
                    requirements.append("Vérifier la conformité de la teneur en impuretés (≤1%).")
            else:
                st.warning("Veuillez entrer une valeur numérique pour la teneur en impuretés.")
    elif material == "Caoutchoucs":
        if answers[0] == "Oui":  # Contact direct
            requirements.append("Limite de migration des nitrosamines dans la salive = 0,01 mg/kg de matériau")
            requirements.append("Limite de migration des substances N-nitrosables dans la salive = 0,1 mg/kg de matériau")
    elif material == "Silicones":
        if answers[0] == "Oui":  # Contact direct
            requirements.append("Matières organiques volatiles libres (≤ 0,5%)")
            requirements.append("Migration globale (LMG= 10 mg/dm³ ou 60 mg/kg d'aliment)")
            requirements.append("Organo-étains (LMS = 0,1 mg/kg)")
            requirements.append("Peroxydes")
    elif material == "DÉRIVÉS ÉPOXYDIQUES DES VERNIS":
        requirements.append("BFDGE et NOGE non autorisés")
        requirements.append("LMS des dérivés H₂O du Badge = 9 mg/kg")
        requirements.append("LMS des dérivés du HCI du Badge = 1 mg/kg")
    elif material == "Pellicules de cellulose régénérée":
        requirements.append("Listes positives (monomères et additifs)")
        requirements.append("Matières organiques volatiles libres (≤ 0,5 %)")
        requirements.append("Migration globale (LMG = 10 mg/dm² ou 60 mg/kg d'aliment)")
        requirements.append("Formaldehyde (LMS = 3 mg/kg)")
        requirements.append("Amines aromatiques primaires et secondaires (LMS = 1 mg/kg)")
        requirements.append("N-nitrosamines (LMS = 1 µg/dm³)")
        requirements.append("Substances N-nitrosables (LMS = 10 µg/dm³)")
        requirements.append("Monomères avec LMS")
        requirements.append("Additifs avec LMS")
        requirements.append("Peroxydes")
    elif material == "Céramiques":
        requirements.append("Limite de migration spécifique du plomb")
        requirements.append("Limite de migration spécifique du cadmium")
        requirements.append("Déclaration écrite de conformité")
    elif material == "MCDA TRAITÉS PAR RAYONNEMENTS IONISANTS":
        if answers[2] and answers[2].isdigit():
            if float(answers[2]) < 10:  # Dose de traitement
                requirements.append("Dossier de demande d'autorisation de traitement pour doses inférieures à 10 kGy.")
            else:
                requirements.append("Dossier de demande d'autorisation de traitement pour doses supérieures à 10 kGy.")
        else:
            st.warning("Veuillez entrer une valeur numérique pour la dose de traitement.")
    elif material == "Produits de nettoyage des MCDA":
        requirements.append("Dossier de demande d'autorisation de substance.")
        requirements.append("Restriction d'emploi concernant les produits de rinçage.")
        requirements.append("Liste positive.")

    # --- Logigramme 5 Logic ---
    if material == "Aciers":
        requirements.append("Vérifier la teneur en plomb, cadmium, arsenic, cobalt.")
        requirements.append("Vérifier la LLS des éléments ajoutés.")
    elif material == "Aciers inoxydables":
        requirements.append("Vérifier les exigences françaises pour les aciers inoxydables (Arrêté du 13 janvier 1976).")
    elif material == "Aluminium":
        requirements.append("Vérifier les exigences françaises pour les aluminiums et alliages (Arrêté du 27 août 1987).")
    elif material == "Bois":
        requirements.append("Vérifier la liste des essences de bois autorisées au contact des aliments (Arrêté du 15 novembre 1945).")
        requirements.append("Vérifier la teneur en pentachlorophénol.")
    elif material == "Caoutchoucs":
        requirements.append("Vérifier les exigences françaises pour les caoutchoucs (Arrêté du 9 novembre 1994).")
        requirements.append("Vérifier les modalités de contrôle des matières organiques volatiles libres.")
    elif material == "Étain":
        requirements.append("Vérifier la teneur en étain ≥ 97 %.")
        requirements.append("Vérifier la teneur en antimoine et cuivre.")
        requirements.append("Vérifier la teneur en plomb, cadmium, arsenic.")
        requirements.append("Vérifier la LLS des éléments ajoutés, en particulier : étain, plomb, cadmium, arsenic, antimoine, cuivre.")
    elif material == "Fontes":
        requirements.append("Vérifier la teneur en plomb, cadmium, arsenic.")
        requirements.append("Vérifier la LLS des éléments ajoutés.")
    elif material == "Métaux blanchis":
        requirements.append("Vérifier la teneur en plomb, cadmium, arsenic.")
        requirements.append("Vérifier la LLS des éléments ajoutés, en particulier : plomb, cadmium.")
    elif material == "Verre, cristal, vitrocéramique":
        requirements.append("Vérifier la LMS pour le plomb et cadmium.")
    elif material == "Objets émaillés et décorés":
        requirements.append("Vérifier la LMS pour le plomb, cadmium et chrome VI.")
    elif material == "Revêtements organiques de supports métalliques":
        requirements.append("Vérifier la liste des substances évaluées dans la résolution-cadre ResAp (2004) 15.")
        requirements.append("Vérifier la limite de migration globale (10 mg/dm³ ou 60 mg/kg d'aliment).")
    elif material == "Revêtements métalliques de supports métalliques":
        requirements.append("Vérifier la LLS des éléments ajoutés, en particulier : nickel, chrome, zinc, cuivre.")
    elif material == "Support bois":
        requirements.append("Vérifier la liste des essences de bois autorisées au contact des aliments (Arrêté du 15 novembre 1945).")
        requirements.append("Vérifier la teneur en pentachlorophénol.")
    elif material == "Vernis de revêtement":
        requirements.append("Vérifier la liste des substances évaluées dans la résolution cadre ResAp (2004) 15.")
    elif material == "Matière plastique de revêtement":
        requirements.append("Vérifier la liste de l'UE du règlement (UE) n° 10/2011.")
    elif material == "Support papiers et cartons":
        requirements.append("Vérifier les listes des matières cellulosiques recommandées par la profession.")
        requirements.append("Vérifier les listes des additifs autorisés en France, dans l'UE, aux USA et en Allemagne.")
        requirements.append("Vérifier le transfert des constituants antimicrobiens.")
        requirements.append("Vérifier l'inertie organoleptique.")
    elif material == "Papiers ET CARTONS":
        requirements.append("Vérifier la teneur en pentachlorophénol.")
        requirements.append("Vérifier la teneur en polychlorobiphenyls.")
        requirements.append("Vérifier la migration du formol, glyoxal, fluor.")
        if len(answers) > 3 and answers[3] == "Oui":  # Contact avec des aliments humides ou gras
            requirements.append("Vérifier la migration des azurants optiques.")
            requirements.append("Vérifier la migration des colorants.")
    elif material == "ENCRES":
        requirements.append("Vérifier les critères de composition.")
        requirements.append("Vérifier les critères d'exclusion.")
        requirements.append("Vérifier la LMS des substances autorisées ou évaluées par l'UE, USA, BFR, Conseil de l'Europe.")
        requirements.append("Vérifier la LMS = 0,01 mg/kg d'aliment pour les substances non évaluées.")
        requirements.append("Vérifier la LMS = 0,05 mg/kg d'aliment pour les substances évaluées par 3 tests de mutagenèse.")
        requirements.append("Vérifier la LMS > 0,05 mg/kg d'aliment pour les substances évaluées selon les règles de l'Efsa.")
    elif material == "COMPLEXES":
        requirements.append("Vérifier la limite de migration globale (10 mg/dm³ ou 60 mg/kg d'aliment).")
        requirements.append("Vérifier la limite de migration spécifique (en mg/kg d'aliment).")

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

