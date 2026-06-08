# Fichier : ShowDuplicates.php

**Chemin :** `modules/Accounts/ShowDuplicates.php`
**Type :** `PHP`
**Categorie :** controller / vue (page de doublons)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Affiche la page de detection de doublons lors de la creation d'un compte. Permet a l'utilisateur de choisir entre utiliser un compte existant ou continuer la creation. Les donnees du formulaire d'origine sont recuperees depuis la session.

## Role technique

Script procedural. Recupere les donnees stockees dans `$_SESSION['SHOW_DUPLICATES']` par `AccountFormBase::handleSave()`, les desserialise via `parse_str`, interroge la base pour reconstruire la liste des comptes doublons. Utilise `XTemplate` pour le rendu HTML et `AccountFormBase::buildTableForm()` pour le tableau de selection.

---

## Dependances cles

| Dependance | Role |
| --- | --- |
| `AccountFormBase` | Construction du tableau HTML de doublons |
| `BeanFactory` | Creation d'un bean Account pour iterer les champs |
| `DBManagerFactory` | Requete SQL pour recuperer les doublons par ID |
| `XTemplate` | Rendu HTML de la page (`ShowDuplicates.html`) |
| `SugarEmailAddress` | Widget email pour la vue doublons |

## Relations cles

- **Appele par :** `AccountFormBase::handleSave()` (redirection HTTP apres detection de doublon)
- **Appelle :** `AccountFormBase::buildTableForm()`, `SugarEmailAddress::getEmailAddressWidgetDuplicatesView()`
- **Position dans le flux :** etape intermediaire dans le flux de creation de compte (entre le POST initial et la sauvegarde definitive)

---

## Points d'attention

- Necessite `$_SESSION['SHOW_DUPLICATES']` : si absent, appel a `sugar_die` (acces non autorise).
- Les donnees POST sont sanitisees via `securexss()` apres desserialisation depuis la session.
- La session est immediatement detruite apres lecture (`unset`) pour eviter les replays.
- Gere le mode popup via `insert_popup_header()` si `$_REQUEST['popup'] == 'true'`.
