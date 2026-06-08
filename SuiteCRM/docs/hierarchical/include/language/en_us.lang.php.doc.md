# ⚙️ en_us.lang.php (configuration)

**Chemin :** `include/language/en_us.lang.php`
**Configure :** `Système de traduction applicatif SuiteCRM (langue anglaise US)`
**Dernière mise à jour doc :** 2026-06-02

## 🎯 Ce que ce fichier configure
Fichier de langue principal de l'application pour l'anglais US. Définit `$app_list_strings` (listes déroulantes : modules, statuts, priorités, types, etc.) et `$app_strings` (libellés globaux de l'interface). Ces tableaux sont chargés en mémoire au démarrage et utilisés dans tous les templates Smarty et contrôleurs.

## 🔑 Paramètres clés
| Paramètre | Valeur | Effet | Preuve |
|---|---|---|---|
| `$app_list_strings['language_pack_name']` | `'US English'` | Nom affiché du pack de langue | ligne 50 |
| `$app_list_strings['moduleList']` | Array des noms de modules | Labels des modules dans la navigation | ligne 51 |
| `$app_list_strings` | ~200+ entrées | Toutes les listes déroulantes de l'interface | ligne 48+ |
| `$app_strings` | ~500+ entrées | Tous les libellés texte globaux | INCONNU (fin du fichier non lue) |

## 🔗 Impacté par / impacte
- Chargé par `return_application_language()` et `return_app_list_strings_language()`
- Surchargé par `custom/include/language/en_us.lang.php` (personnalisations)
- Consommé par `include/language/jsLanguage.php` pour la génération du cache JS
- Utilisé dans l'ensemble des templates Smarty via `$app_strings` et `$app_list_strings`

## 💡 Points d'attention
- Fichier très volumineux (plusieurs centaines de lignes) — ne jamais modifier directement ; utiliser `custom/include/language/en_us.lang.php`.
- Mis à jour à chaque version de SuiteCRM — les personnalisations dans `custom/` sont préservées.
