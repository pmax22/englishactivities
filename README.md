# English Activities

Activités d'anglais interactives pour mes élèves : grammaire, lexique, phonologie, compréhension, expression et culture des pays anglophones.

**Le site :** <https://pmax22.github.io/englishactivities/>

Tout fonctionne dans le navigateur, sans compte. La progression est enregistrée uniquement sur l'appareil de l'élève, et rien n'est envoyé. Le site peut s'installer comme une application et marche hors connexion.

## Organisation du dépôt

| Emplacement | Contenu |
| --- | --- |
| `index.html` | Page d'accueil : catalogue, recherche, filtres par section et par niveau |
| `*.html` (racine) | Une page par activité (308 activités) |
| `progres.html`, `test_niveau.html`, `prof.html`, `devoir.html` | Suivi de progression, test de niveau, espace professeur, devoirs |
| `assets/` | Script commun (`ea.js`), catalogue généré (`catalog.js`), icônes |
| `manifest.json`, `sw.js` | Installation comme application et fonctionnement hors connexion |
| `outils/` | Scripts qui **fabriquent** les pages (à modifier plutôt que les `.html`) |

Les pages restent à la racine : leurs liens relatifs entre elles, vers `assets/` et dans le cache hors connexion, restent ainsi simples.

### Préfixes des noms de fichiers

| Préfixe | Type d'activité |
| --- | --- |
| `cu_` | Dossiers culture : lecture, vocabulaire, quiz, sources « Pour aller plus loin » |
| `co_` | Compréhension de l'oral |
| `ce_` | Compréhension de l'écrit |
| `pr_` | Pragmatique (actes de parole, téléphoner, réclamer…) |
| `so_` | Sociolinguistique (accents, registres, anglais britannique / américain…) |
| `phono_` | Phonologie (sons) |
| `cap_`, `ccf_` | Activités pour le CAP |
| sans préfixe | Grammaire, lexique, syntaxe, phonologie (accent, rythme…) |

La section et le niveau de chaque page (Novice, Intermédiaire, Avancé, Expert) sont définis dans `outils/index_gen2.py`, puis écrits dans `assets/catalog.js`.

## Modifier le site

Les pages sont **générées** : une modification faite directement dans un `.html` serait écrasée à la génération suivante.

| Pour modifier… | Fichier dans `outils/` |
| --- | --- |
| Un dossier culture | `content19.py` à `content38.py`, `dossiers*.py` |
| Les sources « Pour aller plus loin » | `sources.py` |
| Les compléments ajoutés aux dossiers | `extras.py` |
| Le glossaire des dossiers culture | `gloss.py` |
| L'accueil, les sections et les niveaux | `index_gen2.py` |
| Le moteur des exercices | `engine.js`, `generic.js` et les autres `.js` |

Puis, depuis la racine du dépôt :

```bash
bash outils/build.sh                          # régénère et vérifie tout
bash outils/build.sh cu_salem.html prof.html  # + teste ces pages dans un navigateur
```

Les tests navigateur demandent Playwright (`pip install playwright && playwright install chromium`).

Les autres scripts de `outils/` (`content1.py` à `content18.py`, `gen.py`, `gen2.py`, `flow*.py`, `shot*.py`) ont servi à créer les premières pages ou à faire des captures d'écran. Ils sont conservés comme référence, mais la construction normale ne les utilise pas.
