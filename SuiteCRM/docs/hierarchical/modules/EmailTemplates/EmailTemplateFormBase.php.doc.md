# EmailTemplateFormBase.php

**Chemin :** `modules/EmailTemplates/EmailTemplateFormBase.php`
**Type :** helper

**Dernière mise à jour doc :** 2026-06-02

---

## Rôle

Classe de base pour les formulaires de gabarits email. Fournit les méthodes de génération du formulaire HTML et de gestion des pièces jointes (images inline, fichiers) dans l'éditeur de template.

## Type

helper

---

## Dépendances clés

- `EmailTemplate` (modèle)
- `BeanFactory` — instanciation Notes
- `UploadFile` (probable)

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `EmailTemplateFormBase` | classe | Base pour les formulaires de template email |
| `getFormBody()` | méthode | Génère le corps HTML du formulaire de template |
| `handleAttachmentsProcessImages()` | méthode | Traite les images et pièces jointes du template |

## Interactions

- **Appelé par :** `EmailTemplateData.php`, vues EditView/DetailView EmailTemplates
- **Appelle :** BeanFactory (Notes), UploadFile

## Notes

- Utilisée comme helper de traitement lors de la sauvegarde via AJAX (EmailTemplateData.php).
