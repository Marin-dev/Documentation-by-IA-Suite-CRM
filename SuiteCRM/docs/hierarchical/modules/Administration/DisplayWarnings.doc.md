# DisplayWarnings.php

**Chemin :** `modules/Administration/DisplayWarnings.php`
**Type :** PHP (helper / affichage)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Affiche les avertissements systeme a l'administrateur lors de la navigation : rebuild relationships/extensions en attente, problemes FastCGI IIS, echec de connexion recente, absence de serveur SMTP, installateur non verrouille, versions de modules invalides, et erreurs administrateur generiques.

## Role technique
Script procedral inclus dans le header de l'administration. Lit depuis `$_SESSION` les flags de rebuild en attente, verifie la configuration serveur, et appelle `displayAdminError()` pour chaque avertissement detecte.

---

## Dependances cles
| Element | Role |
|---|---|
| `include/utils.php` | Fonctions utilitaires |
| `BeanFactory::newBean('Administration')` | Verification SMTP |
| `$_SESSION['rebuild_relationships']` | Flag rebuild relations |
| `$_SESSION['rebuild_extensions']` | Flag rebuild extensions |
| `$_SESSION['administrator_error']` | Message d'erreur administrateur |
| `$sugar_config['installer_locked']` | Verification verrouillage installateur |

## Symboles principaux
- Aucune classe ni fonction — script d'affichage inclus

## Interactions
- **Inclus par :** Header des pages d'administration (INCONNU - chemin exact non identifie dans ce contexte)
- **Appelle :** `Administration::checkSmtpError()`, `displayAdminError()`

---

## Notes
- `$_SESSION['administrator_error']` est efface apres affichage (ligne 92) pour ne pas reecrire a chaque page.
- La detection FastCGI IIS (lignes 61-63) est specifique Windows et peu courante.
