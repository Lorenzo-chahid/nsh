# app/data/ukrainian_course_data.py

project_name = "Apprendre l'Ukrainien"
project_description = "Un projet complet pour aider les utilisateurs francophones à apprendre l'ukrainien, avec des leçons détaillées, des exemples pratiques et des exercices interactifs."

courses_data = [
    {
        "title": "Alphabet et Prononciation Ukrainiens",
        "description": "Apprenez l'alphabet ukrainien et la prononciation de base avec des explications détaillées et des exemples.",
        "order": 1,
        "sections": [
            {
                "title": "Introduction à l'Alphabet Ukrainien",
                "content": """
L'alphabet ukrainien utilise l'alphabet cyrillique et comporte **33 lettres**. Il est essentiel de maîtriser chaque lettre pour bien prononcer et écrire en ukrainien.

**Voici les lettres de l'alphabet ukrainien avec leur correspondance approximative en français :**

1. **А а** - se prononce comme le 'a' français dans **p**a**p**a.
2. **Б б** - se prononce comme le 'b' français.
3. **В в** - se prononce comme le 'v' français.
4. **Г г** - se prononce comme un 'h' expiré, proche du 'g' anglais dans **g**o.
5. **Ґ ґ** - se prononce comme le 'g' dur français dans **g**are.
6. **Д д** - se prononce comme le 'd' français.
7. **Е е** - se prononce comme le 'é' fermé français dans **é**té.
8. **Є є** - se prononce 'yié'.
9. **Ж ж** - se prononce comme le 'j' français dans **j**ardin.
10. **З з** - se prononce comme le 'z' français.
11. **И и** - se prononce comme le 'i' en français mais plus court, similaire au 'i' dans 'si'.
12. **І і** - se prononce comme le 'i' français dans **i**ci.
13. **Ї ї** - se prononce 'yi'.
14. **Й й** - se prononce comme le 'y' semi-voyelle dans **y**eux.
15. **К к** - se prononce comme le 'k' français.
16. **Л л** - se prononce comme le 'l' français.
17. **М м** - se prononce comme le 'm' français.
18. **Н н** - se prononce comme le 'n' français.
19. **О о** - se prononce comme le 'o' fermé français dans **eau**.
20. **П п** - se prononce comme le 'p' français.
21. **Р р** - se prononce comme un 'r' roulé (vibrant).
22. **С с** - se prononce comme le 's' français dans **s**oleil.
23. **Т т** - se prononce comme le 't' français.
24. **У у** - se prononce comme le 'ou' français dans **ou**til.
25. **Ф ф** - se prononce comme le 'f' français.
26. **Х х** - se prononce comme le 'j' espagnol dans **J**osé ou le 'ch' allemand dans Ba**ch**.
27. **Ц ц** - se prononce comme 'ts' dans **ts**ar.
28. **Ч ч** - se prononce comme 'tch' dans **tch**èque.
29. **Ш ш** - se prononce comme 'ch' français dans **ch**at.
30. **Щ щ** - se prononce comme 'chtch', une combinaison de 'ch' et 'tch'.
31. **Ь ь** - signe mou, adoucit la consonne précédente.
32. **Ю ю** - se prononce 'you'.
33. **Я я** - se prononce 'ya'.

**Remarque :**

- Les lettres **'Г'** et **'Ґ'** représentent des sons différents. **'Г'** est un son fricatif, comme un 'h' aspiré, tandis que **'Ґ'** est un 'g' dur comme dans 'gare'.

**Exemple :**

- **Батько** (bat'ko) signifie **père**.
- **Мати** (maty) signifie **mère**.

Apprendre l'alphabet est la première étape pour lire, écrire et prononcer correctement en ukrainien.
""",
                "order": 1,
                "exercises": [
                    {
                        "question": "Combien de lettres comporte l'alphabet ukrainien ?",
                        "answer": "33",
                        "order": 1,
                    },
                    {
                        "question": "Quelle lettre ukrainienne se prononce comme le 'j' français dans 'jardin' ?",
                        "answer": "Ж",
                        "order": 2,
                    },
                    {
                        "question": "Comment prononce-t-on la lettre 'Р' en ukrainien ?",
                        "answer": "Comme un 'r' roulé.",
                        "order": 3,
                    },
                    {
                        "question": "La lettre 'Г' en ukrainien se prononce comme le 'g' dur français. Vrai ou Faux ?",
                        "answer": "Faux, c'est la lettre 'Ґ' qui se prononce comme le 'g' dur.",
                        "order": 4,
                    },
                ],
            },
            {
                "title": "Les Voyelles Ukrainiennes",
                "content": """
Les voyelles ukrainiennes sont essentielles pour une bonne prononciation. Il y a **10 voyelles** en ukrainien :

1. **А а** - [a] comme dans 'p**a**pa'.
2. **Е е** - [ɛ] comme dans '**è**re' ou 'm**è**re'.
3. **Є є** - [jɛ], se prononce 'yié', combinaison de 'y' + 'é'.
4. **И и** - [ɪ], un son entre 'i' et 'e', inexistant en français, proche du 'i' dans 'r**i**che' mais plus court.
5. **І і** - [i], comme dans '**i**ci'.
6. **Ї ї** - [ji], se prononce 'yi', 'y' + 'i'.
7. **О о** - [ɔ], comme dans 'p**o**mme'.
8. **У у** - [u], comme dans '**ou**'.
9. **Ю ю** - [ju], se prononce 'you', 'y' + 'ou'.
10. **Я я** - [ja], se prononce 'ya', 'y' + 'a'.

**Particularités :**

- Les voyelles **'Є', 'Ї', 'Ю', 'Я'** combinent une semi-voyelle 'y' avec une voyelle.

**Exemples :**

- **Яблуко** (yabluko) - **pomme**.
- **Юнак** (yunak) - **jeune homme**.
- **Їжа** (yizha) - **nourriture**.
- **Європа** (Yevropa) - **Europe**.

**Prononciation de 'И' :**

- Le son [ɪ] de **'И'** est plus fermé que le 'e' français et plus ouvert que le 'i'.

**Exercice de prononciation :**

- Pratiquez la prononciation des mots suivants :

  - **Мати** (maty) - **mère**.
  - **Син** (syn) - **fils**.
  - **Місто** (misto) - **ville**.
  - **Будинок** (budynok) - **maison**.
""",
                "order": 2,
                "exercises": [
                    {
                        "question": "Comment prononce-t-on la voyelle 'І' en ukrainien ?",
                        "answer": "Comme le 'i' dans 'ici'.",
                        "order": 1,
                    },
                    {
                        "question": "Quelle voyelle se prononce comme 'ou' en français ?",
                        "answer": "У",
                        "order": 2,
                    },
                    {
                        "question": "La lettre 'Я' se prononce-t-elle 'ya' ou 'ja' ?",
                        "answer": "'ya'",
                        "order": 3,
                    },
                ],
            },
            {
                "title": "Les Consonnes Ukrainiennes",
                "content": """
Les consonnes ukrainiennes comprennent des sons similaires au français et des sons spécifiques à l'ukrainien.

**Consonnes et prononciations :**

- **Б б** - [b], comme 'b' français.
- **В в** - [v], comme 'v' français.
- **Г г** - [ɦ], un son 'h' fricatif, un 'h' expiré.
- **Ґ ґ** - [g], comme 'g' dur dans 'gare'.
- **Д д** - [d], comme 'd' français.
- **Ж ж** - [ʒ], comme 'j' dans 'jambe'.
- **З з** - [z], comme 'z' français.
- **Й й** - [j], comme 'y' dans 'yaourt'.
- **К к** - [k], comme 'k' français.
- **Л л** - [l], comme 'l' français.
- **М м** - [m], comme 'm' français.
- **Н н** - [n], comme 'n' français.
- **П п** - [p], comme 'p' français.
- **Р р** - [r], un 'r' roulé, plus vibrant que le 'r' français.
- **С с** - [s], comme 's' dans 'salut'.
- **Т т** - [t], comme 't' français.
- **Ф ф** - [f], comme 'f' français.
- **Х х** - [x], comme 'j' espagnol dans 'José' ou 'ch' allemand dans 'Bach'.
- **Ц ц** - [ts], comme 'ts' dans 'tsar'.
- **Ч ч** - [tʃ], comme 'tch' dans 'tchèque'.
- **Ш ш** - [ʃ], comme 'ch' dans 'chat'.
- **Щ щ** - [ʃtʃ], une combinaison de 'ch' et 'tch', plus long que 'ч'.
- **Ь ь** - signe mou, indique que la consonne précédente est palatalisée (adoucie).

**Particularités :**

- **Le signe mou 'Ь' :** Il n'est pas prononcé en lui-même, mais modifie la consonne précédente pour la rendre plus douce.

**Exemples :**

- **День** (den') - **jour**.
- **Любов** (lyubov') - **amour**.
- **Щастя** (shchastya) - **bonheur**.

**Prononciation de 'Г' et 'Ґ' :**

- **'Г'** se prononce comme un 'h' aspiré.
- **'Ґ'** se prononce comme un 'g' dur.

**Exercice de prononciation :**

- Pratiquez les mots suivants :

  - **Хліб** (khlib) - **pain**.
  - **Сад** (sad) - **jardin**.
  - **Місяць** (misyats') - **mois**.
  - **Річка** (richka) - **rivière**.
""",
                "order": 3,
                "exercises": [
                    {
                        "question": "Quelle consonne ukrainienne se prononce comme le 'kh' espagnol ou 'ch' allemand ?",
                        "answer": "Х",
                        "order": 1,
                    },
                    {
                        "question": "La consonne 'Р' en ukrainien est-elle roulée ?",
                        "answer": "Oui, elle se prononce comme un 'r' roulé.",
                        "order": 2,
                    },
                    {
                        "question": "Comment le signe mou 'Ь' affecte-t-il la consonne précédente ?",
                        "answer": "Il adoucit la consonne précédente, la palatalise.",
                        "order": 3,
                    },
                ],
            },
            {
                "title": "Règles de Prononciation",
                "content": """
**Accent tonique :**

- L'accent tonique en ukrainien peut tomber sur n'importe quelle syllabe et peut changer le sens du mot.
- Il n'y a pas de règle fixe, donc il est important de mémoriser l'accentuation des mots.

**Prononciation des consonnes finales :**

- Les consonnes finales sont prononcées clairement, sans assourdissement.

**Palatalisation :**

- Certaines consonnes peuvent être palatalisées (adoucies) lorsqu'elles sont suivies d'une voyelle molle ('Є', 'І', 'Ї', 'Ю', 'Я') ou du signe mou 'Ь'.

**Exemples :**

- **Кіт** (kit) - **chat**.
- **Кінь** (kin') - **cheval**.

**Différence entre 'кіт' et 'кінь' :**

- **'Кіт'** a un 't' dur, signifiant 'chat'.
- **'Кінь'** a un 'n' palatalisé, signifiant 'cheval'.

**Prononciation de 'Щ' :**

- **'Щ'** est prononcé comme 'chtch', un son plus long que 'ч'.

**Exercices :**

1. Prononcez les paires de mots suivants en faisant attention à l'accent tonique :

   - **За́мок** (zámok) - **château**.
   - **Замо́к** (zamók) - **serrure**.

2. Pratiquez les mots avec palatalisation :

   - **День** (den') - **jour**.
   - **Сіль** (sil') - **sel**.
""",
                "order": 4,
                "exercises": [
                    {
                        "question": "L'accent tonique en ukrainien est-il toujours sur la première syllabe ?",
                        "answer": "Non, il peut tomber sur n'importe quelle syllabe.",
                        "order": 1,
                    },
                    {
                        "question": "Quelle est la fonction du signe mou 'Ь' ?",
                        "answer": "Il adoucit (palatalise) la consonne précédente.",
                        "order": 2,
                    },
                    {
                        "question": "Comment prononce-t-on le son 'Щ' en ukrainien ?",
                        "answer": "Comme 'chtch', une combinaison de 'ch' et 'tch'.",
                        "order": 3,
                    },
                ],
            },
        ],
    },
    {
        "title": "Salutations et Présentations",
        "description": "Apprenez à saluer, vous présenter et utiliser des expressions de politesse en ukrainien.",
        "order": 2,
        "sections": [
            {
                "title": "Salutations de Base",
                "content": """
Pour saluer en ukrainien, il existe plusieurs expressions selon le moment de la journée et le degré de formalité.

**Salutations informelles :**

- **Привіт** (pryvit) - **Salut**.
- **Вітаю** (vitayu) - **Je te/vous salue**.

**Salutations formelles :**

- **Добрий ранок** (dobryy ranok) - **Bon matin** (jusqu'à environ 12h).
- **Добрий день** (dobryy den') - **Bonjour** (utilisé tout au long de la journée).
- **Добрий вечір** (dobryy vechir) - **Bonsoir** (après 18h).

**Formules pour dire au revoir :**

- **До побачення** (do pobachennya) - **Au revoir** (formel).
- **Па-па** (pa-pa) - **Bye-bye** (informel).
- **На все добре** (na vse dobre) - **Tout de bon**, **Prenez soin de vous**.

**Exemples de dialogues :**

- **Personne A :** Добрий день!
- **Personne B :** Добрий день! Як справи? (Comment ça va?)

""",
                "order": 1,
                "exercises": [
                    {
                        "question": "Comment dit-on 'Bonjour' en ukrainien pendant la journée ?",
                        "answer": "Добрий день",
                        "order": 1,
                    },
                    {
                        "question": "Quelle est la traduction de 'Добрий вечір' ?",
                        "answer": "Bonsoir",
                        "order": 2,
                    },
                    {
                        "question": "Comment dire 'Au revoir' de manière formelle en ukrainien ?",
                        "answer": "До побачення",
                        "order": 3,
                    },
                ],
            },
            {
                "title": "Se Présenter",
                "content": """
Pour vous présenter en ukrainien, vous pouvez utiliser les phrases suivantes :

**Donner son nom :**

- **Мене звати...** (Mene zvaty...) - **Je m'appelle...**

  - Exemple : Мене звати Олександр. (Je m'appelle Oleksandr.)

- **Я є...** (Ya ye...) - **Je suis...**

  - Exemple : Я є Анна. (Je suis Anna.)

**Demander le nom de quelqu'un :**

- **Як вас звати?** (Yak vas zvaty?) - **Comment vous appelez-vous ?** (formel)
- **Як тебе звати?** (Yak tebe zvaty?) - **Comment t'appelles-tu ?** (informel)

**Dire d'où vous venez :**

- **Я з Франції.** (Ya z Frantsiyi.) - **Je viens de France.**
- **Я француз/француженка.** (Ya frantsuz/frantsuzhenka.) - **Je suis français/française.**

**Exprimer son plaisir de rencontrer quelqu'un :**

- **Радий знайомству.** (Radyi znayomstvu.) - **Enchanté.** (masculin)
- **Рада знайомству.** (Rada znayomstvu.) - **Enchantée.** (féminin)

**Exemple de dialogue :**

- **Personne A :** Привіт! Як тебе звати?
- **Personne B :** Привіт! Мене звати Марія. А тебе?
- **Personne A :** Мене звати Сергій. Радий знайомству!
- **Personne B :** Рада знайомству!

""",
                "order": 2,
                "exercises": [
                    {
                        "question": "Comment dire 'Je m'appelle Anna' en ukrainien ?",
                        "answer": "Мене звати Анна",
                        "order": 1,
                    },
                    {
                        "question": "Quelle phrase utiliser pour demander 'Comment vous appelez-vous ?' de manière formelle ?",
                        "answer": "Як вас звати?",
                        "order": 2,
                    },
                    {
                        "question": "Comment dire 'Je suis français' (masculin) en ukrainien ?",
                        "answer": "Я француз",
                        "order": 3,
                    },
                ],
            },
            {
                "title": "Expressions de Politesse",
                "content": """
Les expressions de politesse sont essentielles pour communiquer respectueusement.

**Remercier :**

- **Дякую** (dyakuyu) - **Merci**.
- **Дуже дякую** (duzhe dyakuyu) - **Merci beaucoup**.

**Répondre à un remerciement :**

- **Будь ласка** (bud' laska) - **De rien**, **Je vous en prie**, **S'il vous plaît** (selon le contexte).

**S'excuser :**

- **Вибачте** (vybachte) - **Excusez-moi**, **Pardon** (formel).
- **Вибач** (vybach) - **Excuse-moi** (informel).
- **Пробачте** (probachte) - **Pardonnez-moi**.

**Demander poliment :**

- **Будь ласка** (bud' laska) - **S'il vous plaît**.

**Autres expressions utiles :**

- **Будьте здорові** (bud'te zdorovi) - **À vos souhaits** (après un éternuement).
- **Прошу** (proshu) - **Je vous en prie**, utilisé pour inviter ou permettre.

**Exemples :**

- **Дякую за допомогу.** (Dyakuyu za dopomohu.) - **Merci pour votre aide.**
- **Вибачте, ви говорите англійською?** (Vybachte, vy hovoryte anhliyskoyu?) - **Excusez-moi, parlez-vous anglais ?**

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
                    {
                        "question": "Comment s'excuser de manière formelle en ukrainien ?",
                        "answer": "Вибачте",
                        "order": 3,
                    },
                ],
            },
        ],
    },
    {
        "title": "Les Nombres et le Temps",
        "description": "Apprenez les nombres, comment compter et exprimer le temps en ukrainien.",
        "order": 3,
        "sections": [
            {
                "title": "Les Nombres de 1 à 20",
                "content": """
**Nombres de 1 à 10 :**

1. **Один** (odyn) - **un**
2. **Два** (dva) - **deux**
3. **Три** (try) - **trois**
4. **Чотири** (chotyry) - **quatre**
5. **П'ять** (p'yat') - **cinq**
6. **Шість** (shist') - **six**
7. **Сім** (sim) - **sept**
8. **Вісім** (visim) - **huit**
9. **Дев'ять** (dev'yat') - **neuf**
10. **Десять** (desyat') - **dix**

**Nombres de 11 à 19 :**

- **Одинадцять** (odynadtsyat') - **onze**
- **Дванадцять** (dvanadtsyat') - **douze**
- **Тринадцять** (trynadtsyat') - **treize**
- **Чотирнадцять** (chotyrynadtsyat') - **quatorze**
- **П'ятнадцять** (p'yatnadtsyat') - **quinze**
- **Шістнадцять** (shistnadtsyat') - **seize**
- **Сімнадцять** (simnadtsyat') - **dix-sept**
- **Вісімнадцять** (visimnadtsyat') - **dix-huit**
- **Дев'ятнадцять** (dev'yatnadtsyat') - **dix-neuf**

**Le nombre 20 :**

- **Двадцять** (dvadtsyat') - **vingt**

**Formation des nombres :**

- Les nombres de 11 à 19 se forment en ajoutant 'надцять' au nombre de base (par exemple, 'три' + 'надцять' = 'тринадцять').

**Exemples :**

- **Я маю три книги.** (Ya mayu try knyhy.) - **J'ai trois livres.**
- **В кімнаті сім вікон.** (V kimnati sim vikon.) - **Il y a sept fenêtres dans la pièce.**

""",
                "order": 1,
                "exercises": [
                    {
                        "question": "Comment dit-on '7' en ukrainien ?",
                        "answer": "Сім",
                        "order": 1,
                    },
                    {
                        "question": "Quel est le nombre 'двана́дцять' en chiffres ?",
                        "answer": "12",
                        "order": 2,
                    },
                    {
                        "question": "Comment dit-on 'quinze' en ukrainien ?",
                        "answer": "П'ятнадцять",
                        "order": 3,
                    },
                ],
            },
            {
                "title": "Les Dizaines et les Centaines",
                "content": """
**Les dizaines :**

- **30** - **Тридцять** (trydtsyat')
- **40** - **Сорок** (sorok)
- **50** - **П'ятдесят** (p'yatdesyat')
- **60** - **Шістдесят** (shistdesyat')
- **70** - **Сімдесят** (simdesyat')
- **80** - **Вісімдесят** (visimdesyat')
- **90** - **Дев'яносто** (dev'yanosto)
- **100** - **Сто** (sto)

**Formation des nombres composés :**

- Pour les nombres entre les dizaines, on ajoute le chiffre après la dizaine avec un espace.

  - Exemple : **Двадцять один** (dvadtsyat' odyn) - **21**
  - **Тридцять п'ять** (trydtsyat' p'yat') - **35**

**Les centaines :**

- **200** - **Двісті** (dvisti)
- **300** - **Триста** (trysta)
- **400** - **Чотириста** (chotyrysta)
- **500** - **П'ятсот** (p'yatsot)
- **600** - **Шістсот** (shistsot)
- **700** - **Сімсот** (simsot)
- **800** - **Вісімсот** (visimsot)
- **900** - **Дев'ятсот** (dev'yatsot)

**Exemples :**

- **У мене сорок дві гривні.** (U mene sorok dvi hryvni.) - **J'ai quarante-deux hryvnias.**
- **В класі тридцять учнів.** (V klasi trydtsyat' uchniv.) - **Il y a trente élèves dans la classe.**

""",
                "order": 2,
                "exercises": [
                    {
                        "question": "Comment dit-on '80' en ukrainien ?",
                        "answer": "Вісімдесят",
                        "order": 1,
                    },
                    {
                        "question": "Quel nombre est 'шістдесят п'ять' ?",
                        "answer": "65",
                        "order": 2,
                    },
                    {
                        "question": "Comment dit-on '100' en ukrainien ?",
                        "answer": "Сто",
                        "order": 3,
                    },
                ],
            },
            {
                "title": "Dire l'Heure",
                "content": """
**Demander l'heure :**

- **Котра година?** (Kotra hodyna?) - **Quelle heure est-il ?**

**Répondre :**

- **Зараз перша година.** (Zaraz persha hodyna.) - **Il est une heure.**
- **Зараз друга година.** (Zaraz druha hodyna.) - **Il est deux heures.**
- **Зараз третя година.** (Zaraz tretia hodyna.) - **Il est trois heures.**

**Minutes :**

- **П'ять хвилин на другу.** (P'yat' khvylyn na druho.) - **Deux heures cinq.**
- **Половина третьої.** (Polovyna tret'oyi.) - **Deux heures et demie.**

**Exemples :**

- **Зустрінемось о п'ятій годині.** (Zustrinemos' o p'yati hodyni.) - **Nous nous rencontrerons à cinq heures.**
- **Зараз четверта година п'ятнадцять хвилин.** (Zaraz chetverta hodyna p'yatnadtsyat' khvylyn.) - **Il est quatre heures quinze.**

**Expressions utiles :**

- **Ранок** (ranok) - **Matin**
- **День** (den') - **Jour**
- **Вечір** (vechir) - **Soir**
- **Ніч** (nich) - **Nuit**

""",
                "order": 3,
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
                    {
                        "question": "Comment exprime-t-on 'Il est deux heures et demie' en ukrainien ?",
                        "answer": "Половина третьої",
                        "order": 3,
                    },
                ],
            },
        ],
    },
    # Les autres cours peuvent être développés de la même manière avec des explications détaillées, des exemples et des exercices pour chaque section.
]

skills_data = [
    {
        "name": "Maîtrise de l'Alphabet",
        "description": "Capacité à lire et écrire les lettres ukrainiennes, à prononcer correctement les sons, et à comprendre les règles de prononciation.",
        "difficulty_level": 1,
    },
    {
        "name": "Vocabulaire de Base",
        "description": "Comprendre et utiliser des mots et phrases ukrainiens courants dans des situations quotidiennes.",
        "difficulty_level": 2,
    },
    {
        "name": "Fondamentaux de la Grammaire",
        "description": "Comprendre les structures grammaticales de base en ukrainien, y compris les genres, les cas, et la conjugaison des verbes.",
        "difficulty_level": 3,
    },
    # Vous pouvez ajouter d'autres compétences telles que "Communication orale", "Lecture et compréhension", etc.
]
