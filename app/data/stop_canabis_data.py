# app/data/arreter_cannabis_course_data.py

project_name = "Auto-Apprentissage pour Arrêter le Cannabis"
project_description = "Un projet pour aider les utilisateurs à augmenter leur résilience et apprendre à arrêter de consommer du cannabis par eux-mêmes."

courses_data = [
    {
        "title": "Comprendre la Dépendance au Cannabis",
        "description": "Apprenez les bases de la dépendance au cannabis et comment elle affecte votre corps et votre esprit.",
        "order": 1,
        "sections": [
            {
                "title": "Les Effets du Cannabis sur le Corps et l'Esprit",
                "content": """
Le cannabis affecte le corps et l'esprit de diverses manières. Comprendre ces effets est une première étape importante pour reconnaître l'impact de sa consommation.

**Effets physiques courants :**
- Augmentation du rythme cardiaque
- Yeux rouges
- Bouche sèche
- Diminution de la coordination motrice

**Effets psychologiques courants :**
- Altération de la perception du temps et de l'espace
- Troubles de la mémoire à court terme
- Sentiments d'anxiété ou de paranoïa
- Euphorie temporaire
""",
                "order": 1,
                "exercises": [
                    {
                        "question": "Nommez deux effets physiques courants de la consommation de cannabis.",
                        "answer": "Augmentation du rythme cardiaque, yeux rouges, bouche sèche, diminution de la coordination motrice.",
                        "order": 1,
                    },
                    {
                        "question": "Comment le cannabis peut-il affecter la mémoire à court terme?",
                        "answer": "Il peut causer des troubles de la mémoire à court terme, rendant difficile la rétention d'informations récentes.",
                        "order": 2,
                    },
                ],
            },
            {
                "title": "Comprendre la Dépendance Physique et Psychologique",
                "content": """
La dépendance au cannabis peut être à la fois physique et psychologique.

**Dépendance physique :**
- Le corps s'habitue à la présence du cannabis et peut montrer des symptômes de sevrage lorsqu'il est arrêté.

**Dépendance psychologique :**
- Fort désir ou besoin de consommer pour ressentir certains effets ou pour faire face à des situations difficiles.
""",
                "order": 2,
                "exercises": [
                    {
                        "question": "Quelle est la différence entre la dépendance physique et psychologique au cannabis?",
                        "answer": "La dépendance physique est liée aux adaptations du corps à la substance, tandis que la dépendance psychologique est le désir ou le besoin mental de consommer pour ressentir certains effets.",
                        "order": 1,
                    },
                    {
                        "question": "Peut-on ressentir des symptômes de sevrage en arrêtant le cannabis? Si oui, donnez un exemple.",
                        "answer": "Oui, des symptômes comme l'irritabilité, l'insomnie ou la perte d'appétit peuvent survenir.",
                        "order": 2,
                    },
                ],
            },
            {
                "title": "Mythes et Réalités sur le Cannabis",
                "content": """
Il existe de nombreux mythes autour du cannabis. Il est important de distinguer les faits de la fiction.

**Mythe :** Le cannabis n'entraîne pas de dépendance.
**Réalité :** Le cannabis peut entraîner une dépendance chez certaines personnes.

**Mythe :** Le cannabis améliore toujours la créativité.
**Réalité :** Bien que certains puissent ressentir un effet sur la créativité, cela peut aussi nuire à la concentration et à la productivité.
""",
                "order": 3,
                "exercises": [
                    {
                        "question": "Est-il vrai que le cannabis ne peut pas entraîner de dépendance?",
                        "answer": "Non, c'est un mythe. Le cannabis peut entraîner une dépendance physique et psychologique.",
                        "order": 1,
                    },
                    {
                        "question": "Pourquoi est-il important de comprendre les mythes et réalités sur le cannabis?",
                        "answer": "Pour prendre des décisions informées sur sa consommation et comprendre les risques réels associés.",
                        "order": 2,
                    },
                ],
            },
        ],
    },
    {
        "title": "Développer la Motivation pour Arrêter",
        "description": "Identifiez vos motivations personnelles pour arrêter et fixez des objectifs réalistes.",
        "order": 2,
        "sections": [
            {
                "title": "Identifier les Raisons Personnelles",
                "content": """
Comprendre vos raisons personnelles pour arrêter est essentiel.

Quelques raisons possibles :
- Améliorer la santé physique et mentale
- Réduire l'impact financier
- Améliorer les relations avec les proches
- Atteindre des objectifs personnels ou professionnels
""",
                "order": 1,
                "exercises": [
                    {
                        "question": "Nommez deux raisons personnelles qui pourraient vous motiver à arrêter le cannabis.",
                        "answer": "Améliorer la santé, économiser de l'argent, améliorer les relations, atteindre des objectifs.",
                        "order": 1,
                    },
                    {
                        "question": "Pourquoi est-il important d'identifier vos propres motivations pour arrêter?",
                        "answer": "Cela aide à renforcer la détermination et fournit un rappel des raisons pour lesquelles vous voulez changer.",
                        "order": 2,
                    },
                ],
            },
            {
                "title": "Fixer des Objectifs Réalistes",
                "content": """
Établir des objectifs réalistes rend le processus plus gérable.

Conseils pour fixer des objectifs :
- Soyez spécifique (par exemple, réduire la consommation de moitié cette semaine)
- Fixez des échéances (par exemple, arrêter complètement d'ici un mois)
- Établissez des étapes intermédiaires
- Célébrez les petites victoires
""",
                "order": 2,
                "exercises": [
                    {
                        "question": "Donnez un exemple d'objectif réaliste pour arrêter le cannabis.",
                        "answer": "Réduire la consommation de 25% chaque semaine jusqu'à l'arrêt complet en un mois.",
                        "order": 1,
                    },
                    {
                        "question": "Pourquoi est-il bénéfique de célébrer les petites victoires?",
                        "answer": "Cela maintient la motivation et reconnaît les progrès réalisés.",
                        "order": 2,
                    },
                ],
            },
        ],
    },
    {
        "title": "Stratégies pour Gérer les Envies",
        "description": "Apprenez des techniques pour faire face aux envies de consommer.",
        "order": 3,
        "sections": [
            {
                "title": "Identifier les Déclencheurs",
                "content": """
Les déclencheurs sont des situations, émotions ou personnes qui augmentent l'envie de consommer.

**Exemples de déclencheurs :**
- Stress au travail
- Fréquentation de certains lieux ou personnes
- Ennui
- Sentiments négatifs comme la tristesse ou la colère
""",
                "order": 1,
                "exercises": [
                    {
                        "question": "Qu'est-ce qu'un déclencheur dans le contexte de la dépendance?",
                        "answer": "C'est une situation, émotion ou stimulus qui provoque l'envie de consommer.",
                        "order": 1,
                    },
                    {
                        "question": "Pourquoi est-il important d'identifier vos déclencheurs personnels?",
                        "answer": "Pour pouvoir les éviter ou développer des stratégies pour y faire face.",
                        "order": 2,
                    },
                ],
            },
            {
                "title": "Techniques pour Surmonter les Envies",
                "content": """
Des stratégies peuvent aider à gérer les envies :

- Pratiquer la respiration profonde
- Se distraire avec une activité (lecture, sport, hobbies)
- Parler à un ami ou un proche
- Noter ses pensées et sentiments dans un journal
""",
                "order": 2,
                "exercises": [
                    {
                        "question": "Nommez deux techniques pour gérer une envie soudaine de consommer.",
                        "answer": "Respiration profonde, se distraire avec une activité, parler à quelqu'un, écrire dans un journal.",
                        "order": 1,
                    },
                    {
                        "question": "Comment la distraction peut-elle aider à surmonter une envie?",
                        "answer": "Elle détourne l'attention de l'envie, permettant au désir de passer.",
                        "order": 2,
                    },
                ],
            },
            {
                "title": "Planifier en Avance",
                "content": """
Anticiper les situations difficiles et planifier comment y faire face est crucial.

- Prévoir des réponses aux offres de cannabis
- Éviter les situations à risque quand possible
- Avoir des alternatives saines à portée de main
""",
                "order": 3,
                "exercises": [
                    {
                        "question": "Pourquoi est-il utile de préparer des réponses à l'avance aux offres de cannabis?",
                        "answer": "Pour être prêt à refuser sans hésitation et réduire la pression sociale.",
                        "order": 1,
                    },
                    {
                        "question": "Donnez un exemple d'alternative saine à la consommation.",
                        "answer": "Faire de l'exercice, pratiquer un hobby, méditer.",
                        "order": 2,
                    },
                ],
            },
        ],
    },
    {
        "title": "Techniques de Gestion du Stress et des Émotions",
        "description": "Apprenez à gérer le stress et les émotions difficiles sans recourir au cannabis.",
        "order": 4,
        "sections": [
            {
                "title": "Pratiquer la Relaxation",
                "content": """
Techniques de relaxation efficaces :

- Méditation
- Yoga
- Exercices de respiration
- Relaxation musculaire progressive
""",
                "order": 1,
                "exercises": [
                    {
                        "question": "Nommez une technique de relaxation que vous pouvez pratiquer quotidiennement.",
                        "answer": "Méditation, yoga, exercices de respiration.",
                        "order": 1,
                    },
                    {
                        "question": "Comment les exercices de respiration peuvent-ils aider à réduire le stress?",
                        "answer": "Ils calment le système nerveux, réduisant les sensations de stress et d'anxiété.",
                        "order": 2,
                    },
                ],
            },
            {
                "title": "Gestion des Émotions",
                "content": """
Apprendre à gérer les émotions :

- Reconnaître et accepter vos émotions
- Utiliser un journal pour exprimer vos sentiments
- Parler à quelqu'un de confiance
- Pratiquer la pleine conscience
""",
                "order": 2,
                "exercises": [
                    {
                        "question": "Pourquoi est-il important de reconnaître et d'accepter vos émotions?",
                        "answer": "Pour mieux les comprendre et y répondre de manière appropriée.",
                        "order": 1,
                    },
                    {
                        "question": "Qu'est-ce que la pleine conscience et comment peut-elle aider?",
                        "answer": "C'est la pratique d'être présent dans l'instant; elle aide à réduire le stress et à gérer les émotions.",
                        "order": 2,
                    },
                ],
            },
        ],
    },
    {
        "title": "Construire un Plan d'Action pour Arrêter",
        "description": "Élaborez un plan détaillé pour arrêter de consommer du cannabis.",
        "order": 5,
        "sections": [
            {
                "title": "Établir un Calendrier",
                "content": """
Un calendrier vous aide à structurer votre démarche.

- Définissez une date d'arrêt
- Planifiez des étapes intermédiaires
- Notez vos progrès régulièrement
""",
                "order": 1,
                "exercises": [
                    {
                        "question": "Pourquoi est-il utile de fixer une date d'arrêt spécifique?",
                        "answer": "Cela crée un objectif clair et renforce l'engagement.",
                        "order": 1,
                    },
                    {
                        "question": "Comment un calendrier peut-il vous aider dans votre démarche?",
                        "answer": "Il structure le processus et permet de suivre les progrès.",
                        "order": 2,
                    },
                ],
            },
            {
                "title": "Créer un Environnement Favorable",
                "content": """
Modifier votre environnement peut soutenir vos efforts.

- Éloignez les objets liés à la consommation
- Informez vos proches de votre démarche
- Évitez les lieux ou situations à risque
""",
                "order": 2,
                "exercises": [
                    {
                        "question": "Comment vos proches peuvent-ils vous soutenir?",
                        "answer": "En offrant du soutien, de la compréhension, et en respectant vos efforts.",
                        "order": 1,
                    },
                    {
                        "question": "Pourquoi est-il important d'éloigner les objets liés à la consommation?",
                        "answer": "Pour réduire les tentations et les rappels de la consommation.",
                        "order": 2,
                    },
                ],
            },
        ],
    },
    {
        "title": "Maintenir l'Abstinence et Prévenir les Rechutes",
        "description": "Stratégies pour rester abstinent sur le long terme.",
        "order": 6,
        "sections": [
            {
                "title": "Reconnaître les Signes de Rechute",
                "content": """
Les signes avant-coureurs peuvent inclure :

- Pensées fréquentes sur le cannabis
- Retour aux anciens lieux ou fréquentations
- Sentiments accrus de stress ou de frustration
""",
                "order": 1,
                "exercises": [
                    {
                        "question": "Nommez un signe avant-coureur potentiel de rechute.",
                        "answer": "Pensées fréquentes sur le cannabis, sentiment accru de stress.",
                        "order": 1,
                    },
                    {
                        "question": "Comment pouvez-vous agir si vous reconnaissez un signe de rechute?",
                        "answer": "Utiliser vos stratégies de gestion, chercher du soutien.",
                        "order": 2,
                    },
                ],
            },
            {
                "title": "Renforcer les Nouveaux Habitudes",
                "content": """
Maintenir de nouvelles habitudes saines :

- Continuer les activités qui vous font du bien
- Fixer de nouveaux objectifs personnels
- Rester engagé avec votre réseau de soutien
""",
                "order": 2,
                "exercises": [
                    {
                        "question": "Pourquoi est-il important de fixer de nouveaux objectifs après avoir arrêté?",
                        "answer": "Pour continuer à avancer et rester motivé.",
                        "order": 1,
                    },
                    {
                        "question": "Comment un réseau de soutien peut-il aider à prévenir les rechutes?",
                        "answer": "En offrant encouragement et assistance lorsque c'est nécessaire.",
                        "order": 2,
                    },
                ],
            },
        ],
    },
    {
        "title": "Renforcer la Résilience Personnelle",
        "description": "Développez votre capacité à faire face aux défis et aux obstacles.",
        "order": 7,
        "sections": [
            {
                "title": "Comprendre la Résilience",
                "content": """
La résilience est la capacité à rebondir face aux difficultés.

- Accepter que les obstacles font partie de la vie
- Voir les défis comme des opportunités d'apprentissage
- Cultiver une attitude positive
""",
                "order": 1,
                "exercises": [
                    {
                        "question": "Qu'est-ce que la résilience?",
                        "answer": "La capacité à rebondir face aux difficultés et à s'adapter aux défis.",
                        "order": 1,
                    },
                    {
                        "question": "Comment pouvez-vous cultiver une attitude positive?",
                        "answer": "En pratiquant la gratitude, en se concentrant sur le présent, en reconnaissant les progrès.",
                        "order": 2,
                    },
                ],
            },
            {
                "title": "Développer des Compétences d'Adaptation",
                "content": """
Compétences pour renforcer la résilience :

- Résolution de problèmes
- Gestion du temps
- Établissement de limites saines
- Pratique régulière d'activités physiques
""",
                "order": 2,
                "exercises": [
                    {
                        "question": "Nommez une compétence qui peut aider à renforcer la résilience.",
                        "answer": "Résolution de problèmes, gestion du temps, etc.",
                        "order": 1,
                    },
                    {
                        "question": "Pourquoi est-il bénéfique de pratiquer une activité physique régulière?",
                        "answer": "Améliore la santé mentale et physique, réduit le stress.",
                        "order": 2,
                    },
                ],
            },
        ],
    },
    {
        "title": "Techniques de Relaxation et de Pleine Conscience",
        "description": "Apprenez des méthodes pour rester présent et réduire le stress.",
        "order": 8,
        "sections": [
            {
                "title": "Introduction à la Pleine Conscience",
                "content": """
La pleine conscience consiste à être pleinement présent.

- Observant sans jugement
- Focalisation sur le moment présent
- Acceptation de ses pensées et sentiments
""",
                "order": 1,
                "exercises": [
                    {
                        "question": "Qu'est-ce que la pleine conscience?",
                        "answer": "La pratique d'être pleinement présent et conscient du moment présent.",
                        "order": 1,
                    },
                    {
                        "question": "Comment la pleine conscience peut-elle aider à réduire le stress?",
                        "answer": "En aidant à gérer les pensées anxieuses et en favorisant le calme.",
                        "order": 2,
                    },
                ],
            },
            {
                "title": "Pratiquer des Exercices de Pleine Conscience",
                "content": """
Exercices simples :

- Scan corporel
- Méditation sur la respiration
- Marche en pleine conscience
""",
                "order": 2,
                "exercises": [
                    {
                        "question": "Décrivez brièvement comment pratiquer un scan corporel.",
                        "answer": "Se détendre et porter attention à chaque partie du corps, de la tête aux pieds.",
                        "order": 1,
                    },
                    {
                        "question": "Quelle est l'importance de la respiration dans la méditation?",
                        "answer": "Elle sert de point focal pour ancrer l'esprit dans le présent.",
                        "order": 2,
                    },
                ],
            },
        ],
    },
    {
        "title": "Améliorer son Mode de Vie",
        "description": "Découvrez comment une vie saine peut soutenir vos efforts pour arrêter.",
        "order": 9,
        "sections": [
            {
                "title": "Sommeil et Alimentation",
                "content": """
Une bonne hygiène de vie est essentielle.

- Dormir suffisamment (7-9 heures par nuit)
- Manger équilibré avec beaucoup de fruits et légumes
- Limiter la consommation de caféine et de sucre
""",
                "order": 1,
                "exercises": [
                    {
                        "question": "Pourquoi le sommeil est-il important dans le processus d'arrêt?",
                        "answer": "Le sommeil aide à réguler l'humeur et réduit le stress.",
                        "order": 1,
                    },
                    {
                        "question": "Comment une alimentation équilibrée peut-elle aider?",
                        "answer": "Elle fournit l'énergie nécessaire et favorise le bien-être général.",
                        "order": 2,
                    },
                ],
            },
            {
                "title": "Activité Physique",
                "content": """
L'exercice physique offre de nombreux avantages.

- Libère des endorphines qui améliorent l'humeur
- Réduit le stress et l'anxiété
- Améliore la confiance en soi
""",
                "order": 2,
                "exercises": [
                    {
                        "question": "Nommez un bénéfice mental de l'activité physique régulière.",
                        "answer": "Amélioration de l'humeur, réduction du stress.",
                        "order": 1,
                    },
                    {
                        "question": "Quelle quantité d'exercice est recommandée par semaine?",
                        "answer": "Au moins 150 minutes d'activité modérée.",
                        "order": 2,
                    },
                ],
            },
        ],
    },
    {
        "title": "Se Connecter avec un Réseau de Soutien",
        "description": "Apprenez l'importance du soutien social dans votre démarche.",
        "order": 10,
        "sections": [
            {
                "title": "Importance du Soutien Social",
                "content": """
Le soutien d'autrui peut faire une grande différence.

- Offre de l'encouragement
- Fournit une écoute empathique
- Partage d'expériences et de conseils
""",
                "order": 1,
                "exercises": [
                    {
                        "question": "Comment le soutien social peut-il aider à arrêter le cannabis?",
                        "answer": "En offrant encouragement, conseils et une écoute attentive.",
                        "order": 1,
                    },
                    {
                        "question": "Pourquoi est-il bénéfique de partager vos objectifs avec les autres?",
                        "answer": "Cela renforce l'engagement et permet aux autres de vous soutenir.",
                        "order": 2,
                    },
                ],
            },
            {
                "title": "Participer à des Groupes ou Communautés",
                "content": """
Rejoindre des groupes peut renforcer votre réseau.

- Groupes de soutien en ligne
- Communautés locales
- Forums dédiés
""",
                "order": 2,
                "exercises": [
                    {
                        "question": "Quels sont les avantages de rejoindre un groupe de soutien?",
                        "answer": "Se sentir moins seul, partager des expériences, obtenir des conseils.",
                        "order": 1,
                    },
                    {
                        "question": "Comment pouvez-vous trouver des communautés en ligne?",
                        "answer": "En recherchant des forums, groupes sur les réseaux sociaux dédiés à l'arrêt du cannabis.",
                        "order": 2,
                    },
                ],
            },
        ],
    },
]

skills_data = [
    {
        "name": "Connaissance de la Dépendance",
        "description": "Comprendre les aspects physiques et psychologiques de la dépendance au cannabis.",
        "difficulty_level": 1,
    },
    {
        "name": "Gestion des Envies",
        "description": "Capacité à reconnaître et gérer les envies de consommer.",
        "difficulty_level": 2,
    },
    {
        "name": "Résilience Émotionnelle",
        "description": "Développer des compétences pour gérer le stress et les émotions sans recourir au cannabis.",
        "difficulty_level": 3,
    },
    {
        "name": "Planification et Prévention des Rechutes",
        "description": "Créer des plans d'action et stratégies pour maintenir l'abstinence.",
        "difficulty_level": 4,
    },
    {
        "name": "Renforcement du Soutien Social",
        "description": "Établir et utiliser un réseau de soutien pour aider dans le processus d'arrêt.",
        "difficulty_level": 5,
    },
]
