import spacy
from pydantic import BaseModel

# Charger les modèles SpaCy pour le français et l'anglais
nlp_fr = spacy.load("fr_core_news_sm")
nlp_en = spacy.load("en_core_web_sm")


# Modèle de la réponse
class AnalyzeResponse(BaseModel):
    category: str
    subcategory: str


# Liste des mots-clés par catégorie et sous-catégorie en français et en anglais
CATEGORIES = {
    "Finance / Business": {
        "Gestion de budget": {
            "fr": [
                "finance",
                "budget",
                "argent",
                "économie",
                "capital",
                "investir",
                "épargner",
                "business",
                "entreprise",
                "revenu",
            ],
            "en": [
                "finance",
                "budget",
                "money",
                "economy",
                "capital",
                "invest",
                "save",
                "business",
                "company",
                "income",
            ],
        },
        "Création d'entreprise": {
            "fr": [
                "entreprise",
                "business",
                "startup",
                "capital",
                "fonds",
                "investissement",
                "développer",
                "affaire",
                "gagner",
            ],
            "en": [
                "startup",
                "company",
                "business",
                "funding",
                "capital",
                "investment",
                "develop",
                "gain",
                "revenue",
            ],
        },
        "Investissement": {
            "fr": [
                "investir",
                "action",
                "boursier",
                "placement",
                "immobilier",
                "cryptomonnaie",
                "crypto",
                "actif",
                "retour",
                "dividende",
            ],
            "en": [
                "invest",
                "stock",
                "share",
                "market",
                "real estate",
                "cryptocurrency",
                "crypto",
                "asset",
                "return",
                "dividend",
            ],
        },
    },
    "Santé / Bien-être": {
        "Perte de poids": {
            "fr": [
                "perdre",
                "poids",
                "minceur",
                "régime",
                "calories",
                "kilos",
                "alimentation",
            ],
            "en": [
                "lose",
                "weight",
                "diet",
                "calories",
                "nutrition",
                "kilos",
                "exercise",
            ],
        },
        "Condition physique": {
            "fr": [
                "forme",
                "exercice",
                "sport",
                "fitness",
                "entraînement",
                "gym",
                "musculation",
            ],
            "en": [
                "fitness",
                "exercise",
                "sport",
                "workout",
                "gym",
                "muscle",
                "training",
            ],
        },
        "Bien-être mental": {
            "fr": [
                "stress",
                "bien-être",
                "relaxation",
                "méditation",
                "santé mentale",
                "calme",
            ],
            "en": [
                "stress",
                "well-being",
                "relaxation",
                "meditation",
                "mental health",
                "calm",
            ],
        },
    },
    "Education / Apprentissage": {
        "Apprentissage linguistique": {
            "fr": [
                "apprendre",
                "langue",
                "parler",
                "bilingue",
                "cours de langue",
                "linguistique",
            ],
            "en": [
                "learn",
                "language",
                "speak",
                "bilingual",
                "language course",
                "linguistics",
            ],
        },
        "Acquisition de compétences": {
            "fr": ["compétences", "apprentissage", "savoir", "formation", "étudier"],
            "en": ["skills", "learning", "knowledge", "training", "study"],
        },
    },
    "Productivité / Gestion de projet": {
        "Gestion de projet": {
            "fr": ["projet", "gestion", "planification", "objectifs", "organisation"],
            "en": ["project", "management", "planning", "goals", "organization"],
        },
        "Amélioration de la productivité": {
            "fr": [
                "productivité",
                "efficacité",
                "focus",
                "gestion du temps",
                "planification",
            ],
            "en": [
                "productivity",
                "efficiency",
                "focus",
                "time management",
                "planning",
            ],
        },
    },
    "Développement personnel": {
        "Amélioration de soi": {
            "fr": [
                "développement",
                "personnel",
                "compétences sociales",
                "confiance",
                "motivation",
            ],
            "en": [
                "self",
                "development",
                "personal",
                "social skills",
                "confidence",
                "motivation",
            ],
        },
        "Gestion du stress": {
            "fr": [
                "stress",
                "anxiété",
                "calme",
                "détente",
                "relaxation",
                "respiration",
            ],
            "en": ["stress", "anxiety", "calm", "relaxation", "breathing"],
        },
    },
    "Technologie / Programmation": {
        "Programmation": {
            "fr": [
                "programmation",
                "code",
                "développement",
                "technologie",
                "informatique",
                "python",
                "javascript",
            ],
            "en": [
                "programming",
                "code",
                "development",
                "technology",
                "computer",
                "python",
                "javascript",
            ],
        },
        "Développement d'applications": {
            "fr": [
                "application",
                "mobile",
                "développement",
                "logiciel",
                "interface",
                "plateforme",
            ],
            "en": [
                "application",
                "mobile",
                "development",
                "software",
                "interface",
                "platform",
            ],
        },
    },
}


# Fonction pour détecter la langue
def detect_language(doc):
    # Simple détection de langue basée sur la proportion de mots-clés anglais vs français
    french_keywords = sum(
        1 for token in doc if token.lemma_ in ["le", "la", "et", "de", "un", "une"]
    )  # Ajuste ces mots-clés de langue française
    english_keywords = sum(
        1 for token in doc if token.lemma_ in ["the", "and", "to", "of", "a"]
    )  # Ajuste ces mots-clés en anglais
    return "fr" if french_keywords > english_keywords else "en"


# Fonction pour analyser l'input utilisateur et retourner une catégorie
def categorize_input(user_input: str) -> AnalyzeResponse:
    # Traiter l'input utilisateur en détectant la langue
    nlp = nlp_fr if detect_language(nlp_fr(user_input)) == "fr" else nlp_en
    doc = nlp(user_input.lower())  # Analyse avec spaCy

    # Détecter les entités nommées (NER)
    entities = {ent.label_: ent.text for ent in doc.ents}
    print(f"Entités détectées: {entities}")

    # Utilisation de NER pour catégoriser
    if "MONEY" in entities:
        return AnalyzeResponse(
            category="Finance / Business", subcategory="Gestion de budget"
        )
    if "LANGUAGE" in entities or any(
        token.lemma_ in ["python", "javascript", "code"] for token in doc
    ):
        return AnalyzeResponse(category="Technologie", subcategory="Programmation")
    if "ORG" in entities:
        return AnalyzeResponse(
            category="Finance / Business", subcategory="Création d'entreprise"
        )
    if any(
        token.lemma_ in ["apprendre", "étudier", "étude", "cours", "formation"]
        for token in doc
    ):
        if any(
            token.lemma_ in ["python", "programmation", "code", "technologie"]
            for token in doc
        ):
            return AnalyzeResponse(category="Technologie", subcategory="Programmation")
        else:
            return AnalyzeResponse(category="Education", subcategory="Apprentissage")
    if any(
        token.lemma_ in ["perdre", "poids", "condition", "santé", "forme"]
        for token in doc
    ):
        return AnalyzeResponse(
            category="Santé / Bien-être", subcategory="Condition physique"
        )
    if any(token.lemma_ in ["projet", "gestion", "productivité"] for token in doc):
        return AnalyzeResponse(
            category="Productivité / Gestion de projet", subcategory="Gestion de projet"
        )
    if any(
        token.lemma_ in ["développement", "personnel", "confiance", "compétences"]
        for token in doc
    ):
        return AnalyzeResponse(
            category="Développement personnel", subcategory="Amélioration de soi"
        )

    return AnalyzeResponse(category="Inconnu", subcategory="Non catégorisé")
