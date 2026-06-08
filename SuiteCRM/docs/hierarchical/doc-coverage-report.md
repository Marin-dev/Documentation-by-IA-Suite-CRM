# Rapport de couverture — Documentation hiérarchique SuiteCRM

**Date :** 2026-06-03 (2e itération)
**Repo audité :** `c:\Github\Documentation by IA Suite CRM\SuiteCRM`
**Doc root :** `docs/hierarchical/`
**Généré par :** agent `hierdoc_verifier`

---

## Score global : 66/100

| Critère | Score | Détail |
|---|---|---|
| Couverture fichiers | 14/30 | 2 895 fiches `.doc.md` / 6 182 fichiers sources (46,8 %) |
| Couverture dossiers | 12/25 | 686 `CONTEXT.md` / 1 414 dossiers planifiés (48,5 %) |
| CONTEXT.md racine | 10/10 | Complet — 14 entrées de navigation, 4 flux décrits, démarrage rapide opérationnel |
| Qualité des fiches | 16/20 | 7/10 fiches échantillonnées conformes ; 239 stubs < 300 octets ; 28 fichiers avec marqueur TODO |
| Navigation et liens | 14/15 | 11/11 liens de premier niveau du CONTEXT.md racine valides ; `doc-plan.json` présent |

**Statut : Corrections requises**

---

## Évolution vs 1re itération (2026-06-02)

| Critère | Avant | Après | Delta |
|---|---|---|---|
| Score global | 63/100 | 66/100 | +3 pts |
| Fiches `.doc.md` | 2 537 | 2 895 | +358 (+14,1 %) |
| `CONTEXT.md` | 560 | 686 | +126 (+22,5 %) |
| Couverture fichiers | 41,0 % | 46,8 % | +5,8 pts |
| Couverture dossiers | 39,6 % | 48,5 % | +8,9 pts |
| Dossiers sans CONTEXT.md | 854 | 728 | -126 |
| Stubs < 300 octets | 49 | 239 | +190 (nouvelles fiches courtes) |
| Fichiers avec TODO | 23 | 28 | +5 |
| Occurrences INCONNU | 1 753 | 1 779 | +26 |

**Gains principaux :** 54 nouveaux CONTEXT.md pour sous-dossiers de `modules/` (désormais 121/121 modules couverts au premier niveau, 481/483 sous-dossiers couverts) + 38 nouvelles fiches `include/` (Dashlets, ListView, EditView, DetailView, SugarObjects templates).

---

## Points forts

- **Couverture modules/ quasi-complète au niveau sous-dossiers** : tous les 121 modules de premier niveau ont un `CONTEXT.md`. Sur 483 sous-dossiers de `modules/`, 481 sont couverts (99,6 %) — seuls `modules/AOR_Charts/lib/pChart` et `modules/OAuthTokens/views` restent sans CONTEXT.md.
- **tests/ et lib/ : couverture dossiers à 100 %** : respectivement 58/58 et 56/56 sous-dossiers ont un `CONTEXT.md`.
- **include/ enrichi** : 38 nouvelles fiches `.doc.md` sur les composants critiques du framework : `ListView`, `EditView`, `DetailView`, `Dashlets`, `SugarObjects/templates` — les fichiers les plus consultes par les développeurs ont maintenant une documentation.
- **CONTEXT.md racine exceptionnel** : architecture MVC, stack complète, 4 flux end-to-end détaillés, guide de navigation 14 cas d'usage, démarrage rapide opérationnel, 13 zones INCONNU explicitement listées.
- **Api/ et service/ entièrement couverts** : 23/23 sous-dossiers `Api/` et 9/9 sous-dossiers `service/` ont leur CONTEXT.md.
- **Traçabilité INCONNU exemplaire** : 1 779 occurrences sur l'ensemble de la documentation, toutes justifiées — conformité stricte aux règles anti-hallucination.

---

## Lacunes résiduelles

### Couverture fichiers : 3 287 fichiers non documentés

| Dossier | Doc produits | Estimation manquants | Langages principaux |
|---|---|---|---|
| `modules/` | 2 133 | ~1 100 | PHP, Smarty, JS (vues, helpers, language files) |
| `include/` | 93 | ~1 210 | PHP, Smarty, JS (sous-dossiers profonds non couverts) |
| `tests/` | 90 | ~230 | PHP Codeception |
| `lib/` | 203 | ~60 | PHP |
| `install/` | 89 | ~20 | PHP |
| `Api/` | 79 | ~10 | PHP |
| `service/` | 44 | ~20 | PHP |
| `metadata/` | 84 | ~5 | PHP |
| `data/` | 12 | ~10 | PHP |
| Autres (`soap/`, `custom/`, `themes/`, `jssource/`) | 69 | ~622 | PHP, JS, CSS |

### Dossiers sans CONTEXT.md : 14 restants

Sur 699 sous-dossiers dans l'arbre documentaire, 685 ont un `CONTEXT.md` (98,0 %). Les 14 manquants :

| Dossier manquant | Observation |
|---|---|
| `include/Dashlets` | Fiches `.doc.md` présentes (5) mais pas de CONTEXT.md |
| `include/DetailView` | Fiches `.doc.md` présentes (2) mais pas de CONTEXT.md |
| `include/EditView` | Fiches `.doc.md` présentes (7) mais pas de CONTEXT.md |
| `include/ListView` | Fiches `.doc.md` présentes (7) mais pas de CONTEXT.md |
| `include/language` | Fiches `.doc.md` présentes (3) mais pas de CONTEXT.md |
| `include/SugarObjects/templates/company` | Fiche présente, pas de CONTEXT.md |
| `include/SugarObjects/templates/file` | Fiche présente, pas de CONTEXT.md |
| `include/SugarObjects/templates/issue` | Fiche présente, pas de CONTEXT.md |
| `include/SugarObjects/templates/sale` | Fiche présente, pas de CONTEXT.md |
| `.github` | Dossier CI/GitHub — CONTEXT.md non critique |
| `.github/ISSUE_TEMPLATE` | Dossier CI/GitHub — CONTEXT.md non critique |
| `.github/workflows` | Dossier CI/GitHub — CONTEXT.md non critique |
| `modules/AOR_Charts/lib/pChart` | Librairie tierce — CONTEXT.md souhaitable |
| `modules/OAuthTokens/views` | Module OAuth legacy — CONTEXT.md manquant |

### Fiches stub ou incomplètes

- **239 fiches `.doc.md` inférieures à 300 octets** (forte augmentation vs 49 en 1re itération — les nouvelles fiches générées pour les fichiers simples `language/`, `metadata/`, `Forms.php` contiennent peu de contenu substantiel). Exemples : `modules/ACL/Forms.doc.md` (287 octets), `modules/ACL/Menu.doc.md` (244 octets), `modules/ACL/language/en_us.lang.doc.md` (220 octets).
- **28 fiches `.doc.md` avec marqueur TODO** (vs 23 en 1re itération) : `download.doc.md`, `install/installConfig.doc.md`, `modules/Calendar/CalendarActivity.doc.md`, `modules/Campaigns/Charts.doc.md`, `Api/V8/Service/ModuleService.php.doc.md`, etc.
- **Hétérogénéité de format** : certaines fiches utilisent "Role fonctionnel" / "Role technique" (sans accent), d'autres "Rôle fonctionnel" — la normalisation UTF-8 n'est pas uniforme.

---

## Zones INCONNU prioritaires

**Total :** 1 779 occurrences dans l'ensemble de la documentation (848 dans les `.doc.md`, 931 dans les `CONTEXT.md`).

Ces zones sont documentées et justifiées conformément aux règles anti-hallucination du projet. Top 10 :

| Rang | Zone INCONNU | Fréquence | Nature |
|---|---|---|---|
| 1 | Routes Slim des contrôleurs API V8 | ~30 fiches | Routes définies dans `Api/V8/Config/routes.php`, non visibles dans les contrôleurs |
| 2 | Point d'entrée HTTP de l'API V8 | ~15 fiches | `lib/API/public/index.php` vs `Api/entryPoint.php` — lien Apache/Nginx non confirmé |
| 3 | Classes `Param\*` et `BaseOption` (Api/V8/Param/) | ~10 fiches | Comportement exact des paramètres de validation non documenté |
| 4 | `BeanFactory::$touched` | 2 fiches | Usage exact de la variable de cache interne non confirmé |
| 5 | `modules/Spots` | 1 fiche | Finalité fonctionnelle non déductible depuis le code |
| 6 | Scopes OAuth2 | 3 fiches | Non implémentés (stub) dans l'API V8 — droits par scope non opérationnels |
| 7 | `FilterValidator.isValid()` | 1 fiche | Retourne toujours `true` (bug/dette technique) |
| 8 | `lib/API/` vs `Api/V8/` | 5 fiches | État exact de la migration non confirmé |
| 9 | Triple DES `SoapHelperWebService` | 1 fiche | IV fixe `"password"` — dette de sécurité API legacy |
| 10 | Séquence wizard `install.php` | 2 fiches | Étapes exactes du wizard non confirmées par lecture complète |

---

## Actions recommandées (par priorité)

### [Critique] 1. Documenter les fichiers manquants dans `include/`

Environ 1 210 fichiers dans `include/` sont sans fiche. Ce dossier contient le framework partagé de SuiteCRM (vues, formulaires, recherche, contrôleurs). Les sous-dossiers prioritaires non couverts :

- `include/controller/` — contrôleurs MVC partagés
- `include/database/` — couche d'abstraction DB
- `include/generic/` — composants génériques (SugarWidgets, layouts)
- `include/MVC/` — dispatch MVC (entryPoint, preDispatch)
- `include/Connectors/` — connecteurs externes (déjà partiellement couvert)
- `include/pdf/` — génération PDF legacy

Action : relancer `hierdoc_file_documenter` sur ces sous-dossiers.

### [Critique] 2. Documenter les fichiers manquants dans `modules/`

Environ 1 100 fichiers manquants dans `modules/` (vues Smarty, helpers JS, fichiers de config secondaires). Priorité aux modules CRM core :

- `modules/Accounts/`, `modules/Contacts/`, `modules/Leads/` — vues et helpers non documentés
- `modules/Campaigns/` — plusieurs fiches avec TODO
- `modules/AOW_WorkFlow/`, `modules/AOW_Actions/` — moteur de workflow

Action : relancer `hierdoc_file_documenter` sur les sous-dossiers ciblés.

### [Important] 3. Générer les CONTEXT.md manquants dans `include/`

9 sous-dossiers d'`include/` ont des fiches `.doc.md` mais pas de `CONTEXT.md` : `Dashlets/`, `DetailView/`, `EditView/`, `ListView/`, `language/`, et 4 sous-dossiers de `SugarObjects/templates/`.

Action : relancer `hierdoc_folder_summarizer` (bottom-up) sur ces 9 dossiers.

### [Important] 4. Compléter ou régénérer les fiches stub

239 fiches inférieures à 300 octets — principalement des fichiers `language/`, `metadata/`, `Forms.php` générés rapidement sans analyse approfondie. Ces fiches sont fonctionnellement vides.

Action : identifier les fiches via `Get-ChildItem docs/hierarchical -Recurse | Where-Object { $_.Name.EndsWith('.doc.md') -and $_.Length -lt 300 }` et les resoumettre à `hierdoc_file_documenter`. Lots suggérés : `modules/ACL*`, `modules/ACLActions`, `modules/*/language/`, `modules/*/metadata/`.

### [Important] 5. Compléter les 28 fiches avec TODO

Fiches partiellement rédigées à compléter en priorité : `install/installConfig.doc.md`, `modules/Calendar/CalendarActivity.doc.md`, `modules/Campaigns/Charts.doc.md`, `Api/V8/Service/ModuleService.php.doc.md`, `modules/Contacts/views/view.quickcreate.doc.md`.

### [Mineur] 6. Générer les CONTEXT.md restants pour modules/ et .github/

Deux sous-dossiers de `modules/` sans CONTEXT.md : `modules/AOR_Charts/lib/pChart` (librairie tierce pChart) et `modules/OAuthTokens/views`. Les dossiers `.github` peuvent être ignorés (hors périmètre applicatif).

### [Investigation] 7. Lever les INCONNU prioritaires

| INCONNU | Action suggérée |
|---|---|
| Routes Slim contrôleurs API V8 | Lire `Api/V8/Config/routes.php` et documenter la correspondance contrôleur ↔ route |
| Point d'entrée HTTP API V8 | Confirmer le front controller réel (`lib/API/public/index.php`) et la config Apache/Nginx |
| Classes `Param\*` non documentées | Soumettre `Api/V8/Param/` complet à `hierdoc_file_documenter` |
| `modules/Spots` | Interroger les interlocuteurs métier ou lire les données de configuration |
| Scopes OAuth2 non implémentés | Confirmer avec l'équipe SuiteCRM (limitation documentée ou bug connu ?) |

---

## Résumé des métriques

| Métrique | 1re itération | 2e itération | Delta |
|---|---|---|---|
| Fichiers source dans le plan | 6 182 | 6 182 | — |
| Fiches `.doc.md` produites | 2 537 | 2 895 | +358 |
| Taux couverture fichiers | 41,0 % | 46,8 % | +5,8 pts |
| Dossiers dans le plan | 1 414 | 1 414 | — |
| `CONTEXT.md` produits | 560 | 686 | +126 |
| Taux couverture dossiers | 39,6 % | 48,5 % | +8,9 pts |
| Sous-dossiers doc sans CONTEXT.md | n.d. | 14/699 | — |
| `CONTEXT.md` racine | Présent et complet | Présent et complet | — |
| Fiches stub (< 300 octets) | 49 | 239 | +190 |
| Fiches avec TODO | 23 | 28 | +5 |
| Occurrences INCONNU total | 1 753 | 1 779 | +26 |
| Liens racine vérifiés | 13/13 valides | 11/11 valides | — |
| Score global | 63/100 | 66/100 | +3 pts |
