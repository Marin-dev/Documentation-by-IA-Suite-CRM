# SugarEmailAddress.js

**Chemin :** `include/SugarEmailAddress/SugarEmailAddress.js`
**Type :** JavaScript
**Dernière mise à jour doc :** 2026-05-28

---

## Rôle

Widget JavaScript gérant l'interface utilisateur du champ email multi-adresses dans les formulaires SuiteCRM (EditView, QuickCreate). Permet d'ajouter, supprimer et valider plusieurs adresses email par enregistrement, avec gestion des drapeaux primaire, réponse à, opt-out, invalide et opt-in.

## Responsabilités

- Créer et gérer dynamiquement des lignes d'adresses email dans le formulaire (clonage de template HTML)
- Gérer les drapeaux par adresse : primaire, reply-to, opt-out, invalide, opted-in
- Vérifier en temps réel la validité d'un email via AJAX (`index.php?module=Contacts&action=RetrieveEmail`)
- Renuméroter les champs après suppression pour maintenir la cohérence des noms de champs
- Forcer la soumission du formulaire après validation (méthode `forceSubmit()`)
- Préremplir les adresses à partir de données JSON existantes (`prefillEmailAddresses()`)

## Dépendances internes

- `SUGAR.language` — accès aux chaînes de langue (`app_strings`)
- `SUGAR.TabFields` — récupération des indices de tabulation
- `addToValidate` / `removeFromValidate` — fonctions globales de validation de formulaire
- `check_form()` — validation globale du formulaire avant soumission
- `isValidEmail()` — fonction globale de validation d'email
- `trim()` — fonction utilitaire globale
- `SUGAR.subpanelUtils.inlineSave()` — sauvegarde inline pour QuickCreate
- `DCMenu.save()` — sauvegarde pour menu DC

## Exports / Points d'entrée

- `SUGAR.EmailAddressWidget` — constructeur (classe JS)
  - `SUGAR.EmailAddressWidget.instances` — registre global des instances par ID
  - `SUGAR.EmailAddressWidget.count` — compteur par module
  - Prototype : `addEmailAddress()`, `removeEmailAddress()`, `prefillEmailAddresses()`, `retrieveEmailAddress()`, `handleKeyDown()`, `forceSubmit()`, `fixPrimaryRadioCheckboxValue()`

## Notes techniques

- Le widget s'auto-enregistre avec un `id` incrémental par module pour permettre plusieurs widgets sur la même page
- La vérification AJAX est déclenchée au `blur` sur le champ email ou à la pression de Enter/Tab
- La suppression réindexe tous les champs de la liste (noms, ids, valeurs) pour maintenir une séquence continue
- Charge une seule fois grâce au guard `if(SUGAR.EmailAddressWidget) return;`
- Variable `emailAddressWidgetLoaded` exposée globalement après chargement
