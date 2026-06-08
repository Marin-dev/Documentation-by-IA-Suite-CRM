# Save.php (Campaigns)

**Chemin :** `modules/Campaigns/Save.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Script de traitement du formulaire de sauvegarde d'une campagne. Cree ou met a jour un enregistrement Campaign, et gere les cas particuliers : duplication de campagne (copie des listes cibles), creation automatique des listes de souscription/desouscription pour les newsletters.

**Type :** controller (script d'action)

---

## Dependances cles
- `BeanFactory::newBean('Campaigns')` — bean principal
- `BeanFactory::newBean('ProspectLists')` — creation des listes par defaut pour newsletter
- `include/formbase.php` — `populateFromPost()`, `handleRedirect()`
- `ACLController::displayNoAccess()` — controle d'acces

## Symboles principaux
Pas de classe exportee. Script procedural execute a l'appel HTTP.

## Interactions
- **Appele par :** Formulaire HTML POST depuis les vues EditView / WizardNewsletter
- **Appelle :** `$focus->save()`, `$focus->prospectlists->add()`, `handleRedirect()`
- **Tables DB modifiees :** `campaigns`, `prospect_list_campaigns`

## Notes
- Pour les newsletters sans listes cibles, cree automatiquement 3 listes ProspectLists : `default` (souscription), `exempt` (desouscription), `test` (lignes 113-135).
- En cas de duplication (`duplicateSave`), copie les `prospectlists` de la campagne source vers la nouvelle (lignes 73-87).
- Les champs `relate_to` et `relate_id` sont effaces lors d'une duplication de newsletter pour eviter que les listes soient attachees a la campagne originale (lignes 96-99).
- Necessite une verification ACL Save avant toute modification (ligne 50-53).
