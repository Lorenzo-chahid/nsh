# app/data/ukrainian_course_data.py


project_name = "Learn Ukrainian"
project_description = "Un projet pour aider les utilisateurs à apprendre l'ukrainien."

courses_data = [
    {
        "title": "Alphabet et Prononciation Ukrainiens",
        "description": "Apprenez l'alphabet ukrainien et la prononciation de base.",
        "order": 1,
        "sections": [
            {
                "title": "Introduction à l'Alphabet Ukrainien",
                "content": """
L'alphabet ukrainien utilise l'alphabet cyrillique et comporte 33 lettres. Il est essentiel de maîtriser chaque lettre pour bien prononcer et écrire en ukrainien.

Voici les lettres de l'alphabet ukrainien :

А, Б, В, Г, Ґ, Д, Е, Є, Ж, З, И, І, Ї, Й, К, Л, М, Н, О, П, Р, С, Т, У, Ф, Х, Ц, Ч, Ш, Щ, Ь, Ю, Я
""",
                "order": 1,
                "exercises": [
                    {
                        "question": "Combien de lettres comporte l'alphabet ukrainien ?",
                        "answer": "33",
                        "order": 1,
                    },
                    {
                        "question": "L'ukrainien utilise l'alphabet latin. Vrai ou Faux ?",
                        "answer": "Faux",
                        "order": 2,
                    },
                ],
            },
            {
                "title": "Les Voyelles Ukrainiennes",
                "content": """
Les voyelles ukrainiennes sont :

- А (a)
- Е (é)
- Є (yié)
- И (i)
- І (i)
- Ї (yi)
- О (o)
- У (ou)
- Ю (you)
- Я (ya)

Chaque voyelle a une prononciation spécifique qui est importante pour la compréhension orale.
""",
                "order": 2,
                "exercises": [
                    {
                        "question": "Comment prononce-t-on la voyelle 'І' en ukrainien ?",
                        "answer": "Comme le 'i' dans 'machine'.",
                        "order": 1,
                    },
                    {
                        "question": "Quelle voyelle se prononce comme 'ou' en français ?",
                        "answer": "У",
                        "order": 2,
                    },
                ],
            },
            {
                "title": "Les Consonnes Ukrainiennes",
                "content": """
Les consonnes ukrainiennes comprennent des sons similaires au français et des sons spécifiques :

- Б (b)
- В (v)
- Г (h)
- Ґ (g)
- Д (d)
- Ж (j)
- З (z)
- Й (y)
- К (k)
- Л (l)
- М (m)
- Н (n)
- П (p)
- Р (r roulé)
- С (s)
- Т (t)
- Ф (f)
- Х (kh)
- Ц (ts)
- Ч (tch)
- Ш (ch)
- Щ (chtch)
- Ь (signe mou)

La lettre 'Х' se prononce comme le 'j' espagnol dans 'José'.
""",
                "order": 3,
                "exercises": [
                    {
                        "question": "Quelle consonne ukrainienne se prononce comme le 'kh' espagnol ?",
                        "answer": "Х",
                        "order": 1,
                    },
                    {
                        "question": "La consonne 'Р' en ukrainien est-elle roulée ?",
                        "answer": "Oui",
                        "order": 2,
                    },
                ],
            },
            {
                "title": "Règles de Prononciation",
                "content": """
En ukrainien :

- L'accent tonique peut tomber sur n'importe quelle syllabe.
- Les lettres 'Г' et 'Ґ' ont des prononciations différentes.
- Le signe mou 'Ь' adoucit la consonne précédente.
""",
                "order": 4,
                "exercises": [
                    {
                        "question": "L'accent tonique en ukrainien est-il toujours sur la première syllabe ?",
                        "answer": "Non",
                        "order": 1,
                    },
                    {
                        "question": "Quelle est la fonction du signe mou 'Ь' ?",
                        "answer": "Il adoucit la consonne précédente.",
                        "order": 2,
                    },
                ],
            },
        ],
    },
    {
        "title": "Salutations et Présentations",
        "description": "Apprenez à saluer et vous présenter en ukrainien.",
        "order": 2,
        "sections": [
            {
                "title": "Salutations de Base",
                "content": """
Pour saluer :

- 'Привіт' signifie 'Salut'.
- 'Добрий день' signifie 'Bonjour'.
- 'Добрий ранок' signifie 'Bon matin'.
- 'Добрий вечір' signifie 'Bonsoir'.
""",
                "order": 1,
                "exercises": [
                    {
                        "question": "Comment dit-on 'Bonjour' en ukrainien ?",
                        "answer": "Добрий день",
                        "order": 1,
                    },
                    {
                        "question": "Quelle est la traduction de 'Добрий вечір' ?",
                        "answer": "Bonsoir",
                        "order": 2,
                    },
                ],
            },
            {
                "title": "Se Présenter",
                "content": """
Pour vous présenter :

- 'Мене звати...' signifie 'Je m'appelle...'.
- 'Я з Франції' signifie 'Je viens de France'.
- 'Радий знайомству' (masculin) ou 'Рада знайомству' (féminin) signifie 'Enchanté(e)'.
""",
                "order": 2,
                "exercises": [
                    {
                        "question": "Comment dire 'Je m'appelle Anna' en ukrainien ?",
                        "answer": "Мене звати Анна",
                        "order": 1,
                    },
                    {
                        "question": "Quelle phrase utiliser pour demander 'Comment vous appelez-vous ?' ?",
                        "answer": "Як вас звати?",
                        "order": 2,
                    },
                ],
            },
            {
                "title": "Expressions de Politesse",
                "content": """
Expressions utiles :

- 'Будь ласка' signifie 'S'il vous plaît' ou 'De rien'.
- 'Дякую' signifie 'Merci'.
- 'Вибачте' signifie 'Excusez-moi' ou 'Pardon'.
""",
                "order": 3,
                "exercises": [
                    {
                        "question": "Comment dit-on 'Merci' en ukrainien ?",
                        "answer": "Дякую",
                        "order": 1,
                    },
                    {
                        "question": "Quelle est la réponse appropriée à 'Дякую' ?",
                        "answer": "Будь ласка",
                        "order": 2,
                    },
                ],
            },
        ],
    },
    {
        "title": "Les Nombres et le Temps",
        "description": "Apprenez les nombres et comment exprimer le temps en ukrainien.",
        "order": 3,
        "sections": [
            {
                "title": "Les Nombres de 1 à 20",
                "content": """
Les nombres de 1 à 10 :

1 - один  
2 - два  
3 - три  
4 - чотири  
5 - п'ять  
6 - шість  
7 - сім  
8 - вісім  
9 - дев'ять  
10 - десять  

Les nombres de 11 à 20 suivent un schéma régulier :

11 - одинадцять  
12 - дванадцять  
13 - тринадцять  
...  
20 - двадцять
""",
                "order": 1,
                "exercises": [
                    {
                        "question": "Comment dit-on '7' en ukrainien ?",
                        "answer": "сім",
                        "order": 1,
                    },
                    {
                        "question": "Quel est le nombre 'дванацять' en chiffres ?",
                        "answer": "12",
                        "order": 2,
                    },
                ],
            },
            {
                "title": "Dire l'Heure",
                "content": """
Pour demander l'heure :

- 'Котра година?' signifie 'Quelle heure est-il ?'.

Pour indiquer l'heure :

- 'Зараз друга година' signifie 'Il est deux heures'.

Les minutes s'ajoutent après 'година' :

- 'Зараз п'ята година двадцять хвилин' signifie 'Il est cinq heures vingt'.
""",
                "order": 2,
                "exercises": [
                    {
                        "question": "Comment demande-t-on 'Quelle heure est-il ?' en ukrainien ?",
                        "answer": "Котра година?",
                        "order": 1,
                    },
                    {
                        "question": "Comment dit-on 'Il est trois heures' en ukrainien ?",
                        "answer": "Зараз третя година",
                        "order": 2,
                    },
                ],
            },
        ],
    },
    {
        "title": "Famille et Relations",
        "description": "Vocabulaire lié à la famille et aux relations.",
        "order": 4,
        "sections": [
            {
                "title": "Les Membres de la Famille",
                "content": """
- Мати - mère  
- Батько - père  
- Брат - frère  
- Сестра - sœur  
- Син - fils  
- Донька - fille  
- Дідусь - grand-père  
- Бабуся - grand-mère  
""",
                "order": 1,
                "exercises": [
                    {
                        "question": "Comment dit-on 'mère' en ukrainien ?",
                        "answer": "мати",
                        "order": 1,
                    },
                    {
                        "question": "Quel est le mot ukrainien pour 'frère' ?",
                        "answer": "брат",
                        "order": 2,
                    },
                ],
            },
            {
                "title": "Relations",
                "content": """
- Друзі - amis  
- Чоловік - mari  
- Дружина - femme  
- Колега - collègue  
""",
                "order": 2,
                "exercises": [
                    {
                        "question": "Comment dit-on 'ami' au pluriel en ukrainien ?",
                        "answer": "друзі",
                        "order": 1,
                    },
                    {
                        "question": "Quel est le mot pour 'épouse' en ukrainien ?",
                        "answer": "дружина",
                        "order": 2,
                    },
                ],
            },
        ],
    },
    {
        "title": "Grammaire de Base",
        "description": "Introduction aux bases de la grammaire ukrainienne.",
        "order": 5,
        "sections": [
            {
                "title": "Les Genres des Noms",
                "content": """
En ukrainien, les noms ont trois genres :

- Masculin : généralement se terminent par une consonne.
- Féminin : généralement se terminent par 'а' ou 'я'.
- Neutre : généralement se terminent par 'о' ou 'е'.

Exemples :

- 'стіл' (table) - masculin
- 'книга' (livre) - féminin
- 'вікно' (fenêtre) - neutre
""",
                "order": 1,
                "exercises": [
                    {
                        "question": "Le mot 'книга' est de quel genre ?",
                        "answer": "Féminin",
                        "order": 1,
                    },
                    {
                        "question": "Combien de genres grammaticaux y a-t-il en ukrainien ?",
                        "answer": "3",
                        "order": 2,
                    },
                ],
            },
            {
                "title": "Pronoms Personnels",
                "content": """
- Я - je  
- Ти - tu  
- Він - il  
- Вона - elle  
- Ми - nous  
- Ви - vous  
- Вони - ils/elles  
""",
                "order": 2,
                "exercises": [
                    {
                        "question": "Quel est le pronom pour 'nous' en ukrainien ?",
                        "answer": "ми",
                        "order": 1,
                    },
                    {
                        "question": "Comment dit-on 'elle' en ukrainien ?",
                        "answer": "вона",
                        "order": 2,
                    },
                ],
            },
            {
                "title": "Conjugaison des Verbes au Présent",
                "content": """
Les terminaisons des verbes au présent varient selon le sujet :

- Я говорю - Je parle  
- Ти говориш - Tu parles  
- Він/Вона говорить - Il/Elle parle  
- Ми говоримо - Nous parlons  
- Ви говорите - Vous parlez  
- Вони говорять - Ils/Elles parlent  
""",
                "order": 3,
                "exercises": [
                    {
                        "question": "Conjuguez le verbe 'жити' (vivre) avec 'nous'.",
                        "answer": "Ми живемо",
                        "order": 1,
                    },
                    {
                        "question": "Comment dit-on 'Tu manges' en ukrainien ? (verbe 'їсти')",
                        "answer": "Ти їси",
                        "order": 2,
                    },
                ],
            },
        ],
    },
    {
        "title": "Phrases Utiles",
        "description": "Apprenez des phrases utiles pour la vie quotidienne.",
        "order": 6,
        "sections": [
            {
                "title": "Expressions Courantes",
                "content": """
- Так - Oui  
- Ні - Non  
- Можливо - Peut-être  
- Я не розумію - Je ne comprends pas  
- Повторіть, будь ласка - Répétez, s'il vous plaît  
""",
                "order": 1,
                "exercises": [
                    {
                        "question": "Comment dit-on 'Oui' en ukrainien ?",
                        "answer": "так",
                        "order": 1,
                    },
                    {
                        "question": "Quelle est la phrase pour 'Je ne comprends pas' ?",
                        "answer": "Я не розумію",
                        "order": 2,
                    },
                ],
            },
            {
                "title": "Demander de l'Aide",
                "content": """
- Ви можете мені допомогти? - Pouvez-vous m'aider ?  
- Де знаходиться...? - Où se trouve...?  
- Мені потрібна допомога - J'ai besoin d'aide  
""",
                "order": 2,
                "exercises": [
                    {
                        "question": "Comment demander 'Où sont les toilettes ?' en ukrainien ?",
                        "answer": "Де туалет?",
                        "order": 1,
                    },
                    {
                        "question": "Quelle phrase utiliser pour 'J'ai besoin d'aide' ?",
                        "answer": "Мені потрібна допомога",
                        "order": 2,
                    },
                ],
            },
        ],
    },
    {
        "title": "Nourriture et Boissons",
        "description": "Vocabulaire de base sur la nourriture et les boissons.",
        "order": 7,
        "sections": [
            {
                "title": "Au Restaurant",
                "content": """
- Меню - Menu  
- Вода - Eau  
- Хліб - Pain  
- Суп - Soupe  
- М'ясо - Viande  
- Риба - Poisson  
""",
                "order": 1,
                "exercises": [
                    {
                        "question": "Comment dit-on 'eau' en ukrainien ?",
                        "answer": "вода",
                        "order": 1,
                    },
                    {
                        "question": "Quel est le mot pour 'pain' ?",
                        "answer": "хліб",
                        "order": 2,
                    },
                ],
            },
            {
                "title": "Commander de la Nourriture",
                "content": """
- Я хочу замовити... - Je voudrais commander...  
- Рахунок, будь ласка - L'addition, s'il vous plaît  
- Смачного - Bon appétit  
""",
                "order": 2,
                "exercises": [
                    {
                        "question": "Comment demander l'addition en ukrainien ?",
                        "answer": "Рахунок, будь ласка",
                        "order": 1,
                    },
                    {
                        "question": "Quelle phrase utiliser pour 'Je voudrais commander du poisson' ?",
                        "answer": "Я хочу замовити рибу",
                        "order": 2,
                    },
                ],
            },
        ],
    },
    {
        "title": "Directions et Transport",
        "description": "Apprenez à vous déplacer et demander votre chemin.",
        "order": 8,
        "sections": [
            {
                "title": "Demander son Chemin",
                "content": """
- Як дійти до...? - Comment aller à...?  
- Ліворуч - À gauche  
- Праворуч - À droite  
- Прямо - Tout droit  
""",
                "order": 1,
                "exercises": [
                    {
                        "question": "Comment dit-on 'À gauche' en ukrainien ?",
                        "answer": "Ліворуч",
                        "order": 1,
                    },
                    {
                        "question": "Quelle phrase utiliser pour 'Comment aller à la gare ?' ?",
                        "answer": "Як дійти до вокзалу?",
                        "order": 2,
                    },
                ],
            },
            {
                "title": "Transport",
                "content": """
- Автобус - Bus  
- Поїзд - Train  
- Літак - Avion  
- Таксі - Taxi  
""",
                "order": 2,
                "exercises": [
                    {
                        "question": "Quel est le mot pour 'train' en ukrainien ?",
                        "answer": "поїзд",
                        "order": 1,
                    },
                    {
                        "question": "Comment dit-on 'Je prends le bus' ?",
                        "answer": "Я їду автобусом",
                        "order": 2,
                    },
                ],
            },
        ],
    },
    {
        "title": "Temps et Météo",
        "description": "Vocabulaire pour parler du temps qu'il fait.",
        "order": 9,
        "sections": [
            {
                "title": "Les Saisons",
                "content": """
- Весна - Printemps  
- Літо - Été  
- Осінь - Automne  
- Зима - Hiver  
""",
                "order": 1,
                "exercises": [
                    {
                        "question": "Comment dit-on 'hiver' en ukrainien ?",
                        "answer": "зима",
                        "order": 1,
                    },
                    {
                        "question": "Quelle est la saison 'літо' ?",
                        "answer": "Été",
                        "order": 2,
                    },
                ],
            },
            {
                "title": "La Météo",
                "content": """
- Сонячно - Ensoleillé  
- Дощ - Pluie  
- Сніг - Neige  
- Холодно - Froid  
- Спекотно - Chaud  
""",
                "order": 2,
                "exercises": [
                    {
                        "question": "Quel est le mot pour 'pluie' en ukrainien ?",
                        "answer": "дощ",
                        "order": 1,
                    },
                    {
                        "question": "Comment dit-on 'Il fait froid' ?",
                        "answer": "Холодно",
                        "order": 2,
                    },
                ],
            },
        ],
    },
]

skills_data = [
    {
        "name": "Maîtrise de l'Alphabet",
        "description": "Capacité à lire et écrire les lettres ukrainiennes.",
        "difficulty_level": 1,
    },
    {
        "name": "Vocabulaire de Base",
        "description": "Comprendre et utiliser des mots et phrases ukrainiens courants.",
        "difficulty_level": 2,
    },
    {
        "name": "Fondamentaux de la Grammaire",
        "description": "Comprendre les structures grammaticales de base en ukrainien.",
        "difficulty_level": 3,
    },
]
