import streamlit as st

# Configuration de la page
st.set_page_config(
    layout="wide",
    page_title="Assistant Sécurité Emballages Alimentaires",
    initial_sidebar_state="expanded"
)

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
            <img src="https://raw.githubusercontent.com/M00N69/RAPPELCONSO/main/logo%2004%20copie.jpg" alt="Visipilot Logo" class="sidebar-logo">
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
# Titre principal de l'application
st.title("Assistant Sécurité Emballages Alimentaires")

# Expander pour expliquer le fonctionnement de l'application
with st.expander("📄 Comment utiliser cette application", expanded=False):
    st.write("""
    **Bienvenue sur l'Assistant Sécurité Emballages Alimentaires !**

    Cette application vous aide à déterminer les réglementations, spécifications, tests et exigences pertinents pour différents matériaux d'emballage alimentaire en fonction de l'aliment concerné et des conditions d'utilisation.

    **Étapes pour utiliser l'application :**
    1. **Contexte de l'Emballage :** Fournissez des informations contextuelles sur l'emballage et les besoins spécifiques.
    2. **Navigation :** Utilisez la barre latérale pour sélectionner entre les logigrammes disponibles :
        - *Réglementation et Spécificités* : Obtenez des informations détaillées sur les réglementations et spécifications applicables selon le matériau choisi.
        - *Tests et Exigences* : Identifiez les tests et exigences nécessaires en fonction du matériau et du type d'aliment.
    3. **Sélection et Réponses :** Sélectionnez le matériau et répondez aux questions posées pour affiner les résultats.
    4. **Résultats et Conclusion :** Consultez les informations générées et téléchargez les résultats si nécessaire.

    **Note :** Assurez-vous de fournir des informations précises pour obtenir des résultats fiables. En cas de doute, consultez les textes réglementaires officiels ou contactez un expert en sécurité alimentaire.
    """)
# Informations contextuelles initiales
with st.expander("🏷️ Contexte de l'Emballage", expanded=True):
    st.write("Veuillez fournir des informations supplémentaires pour une analyse plus précise.")
    purpose = st.text_input("Objectif de l'emballage (ex: conservation, protection, transport, etc.)")
    client_needs = st.text_area("Besoins spécifiques du client (ex: type d'aliment, conditions de stockage, etc.)")
    additional_info = st.text_area("Informations complémentaires (ex: présence de nanoparticules, etc.)")

# Menu de navigation dans la barre latérale
st.sidebar.title("📚 Navigation")
choice = st.sidebar.radio(
    "Choisir un logigramme :",
    ("Réglementation et Spécificités", "Tests et Exigences")
)
# --- Logigramme 1: Réglementation et Spécificités ---
if choice == "Réglementation et Spécificités":
    st.header("📝 Logigramme 1: Réglementation et Spécificités selon le matériau")

    # Sélection du matériau
    materials = [
        "Aciers", "Aciers inoxydables", "Aluminium", "Alliages d'aluminium", 
        "Bois", "Caoutchoucs", "Céramiques", "Étain", "Fontes", "Grès - Porcelaine",
        "Matières plastiques", "Métaux blanchis", "Métaux et alliages de métaux", 
        "Objets en étain", "Papiers", "Pellicules de cellulose régénérée",
        "Produits de nettoyage des MCDA", "Silicones", "Verre", "Zinc", "Autres"
    ]
    material = st.selectbox("Sélectionner le matériau d'emballage :", materials)

    # Affichage des réglementations et spécifications en fonction du matériau sélectionné
    st.subheader("📚 Réglementations et Spécificités :")
    
    if material == "Aciers":
        st.write("### Aciers")
        st.write("**Réglementations :**")
        st.write("- Arrêté du 15 novembre 1945 : MÉTAUX ET ALLIAGES")
        st.write("**Spécifications :**")
        st.write("- Teneur en plomb, cadmium, arsenic, cobalt")
        st.write("- Limites des éléments ajoutés")
    # Ajoutez ici les autres conditions pour chaque matériau comme dans votre code initial

    # Bouton pour télécharger les résultats
    st.download_button(
        label="💾 Télécharger les résultats",
        data="Résultats de la réglementation et spécificités pour le matériau sélectionné.",
        file_name=f"resultats_{material.lower()}.txt",
        mime="text/plain"
    )

# --- Logigramme 2: Tests et Exigences ---
elif choice == "Tests et Exigences":
    st.header("🔬 Logigramme 2: Tests et Exigences selon le matériau et l'aliment")

    # Sélection du matériau
    materials = [
        "Aciers", "Aciers inoxydables", "Aluminium", "Alliages d'aluminium", 
        "Bois", "Caoutchoucs", "Céramiques", "Étain", "Fontes", "Grès - Porcelaine",
        "Matières plastiques", "Métaux blanchis", "Métaux et alliages de métaux", 
        "Objets en étain", "Papiers et Cartons", "Pellicules de cellulose régénérée",
        "Produits de nettoyage des MCDA", "Silicones", "Verre, cristal, vitrocéramique", 
        "Objets émaillés et décorés", "Zinc", "Autres"
    ]
    material = st.selectbox("Sélectionner le matériau d'emballage :", materials)

    # Sélection du type d'aliment
    food_types = ["Aqueux pH > 4.5", "Acide", "Gras", "Sec", "Autres"]
    food_type = st.selectbox("Sélectionner le type d'aliment :", food_types)

    # Questions pour identifier les tests et exigences
    st.subheader("❓ Questions pour identifier les tests et exigences :")
    is_direct_contact = st.radio("Le matériau est-il en contact direct avec l'aliment ?", ("Oui", "Non"))
    is_thermal_treatment = st.radio("Le matériau est-il soumis à un traitement thermique ?", ("Oui", "Non"))
    max_temperature = st.number_input("Quelle est la température maximale du traitement thermique (en °C) ?", min_value=0)
    storage_duration = st.number_input("Quelle est la durée de conservation du produit (en jours) ?", min_value=0)

    # Affichage des tests et exigences en fonction des réponses
    st.subheader("✅ Tests et Exigences recommandés :")
    if is_direct_contact == "Oui":
        st.write("- Test de migration globale")
        st.write("- Test de migration spécifique")
    if is_thermal_treatment == "Oui" and max_temperature > 100:
        st.write("- Test de résistance thermique")

    # Bouton pour télécharger les résultats
    st.download_button(
        label="💾 Télécharger les résultats",
        data="Résultats des tests et exigences pour le matériau et l'aliment sélectionnés.",
        file_name=f"tests_exigences_{material.lower()}_{food_type.lower()}.txt",
        mime="text/plain"
    )

# --- Conclusion générale ---
st.header("🏁 Conclusion")

st.write("En se basant sur les informations fournies et l'analyse réalisée, les recommandations appropriées ont été générées. Veuillez vous assurer de respecter toutes les réglementations applicables et de procéder aux tests nécessaires pour garantir la sécurité et la conformité de vos emballages alimentaires.")

st.write(f"**Contexte de l'emballage fourni :**")
st.write(f"- **Objectif :** {purpose if purpose else 'Non spécifié'}")
st.write(f"- **Besoins spécifiques du client :** {client_needs if client_needs else 'Non spécifié'}")
st.write(f"- **Informations complémentaires :** {additional_info if additional_info else 'Non spécifié'}")

st.write("Pour des analyses plus approfondies ou des conseils supplémentaires, veuillez consulter les autorités compétentes ou des experts en sécurité alimentaire.")
