# 📁 EmailTemplates

**Chemin :** `modules/EmailTemplates/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module EmailTemplates gère les modèles d'emails pour les campagnes marketing et les workflows. Un template définit le sujet, le corps HTML et texte d'un email avec des variables de substitution `{contact_name}` etc.

## ⚙️ Responsabilité technique
Bean `EmailTemplate` (hérite de `SugarBean`). Parseur de template `EmailTemplateParser`. Support des pièces jointes. Utilisé par Campaigns (EmailMarketing) et AOW_Actions (actionSendEmail).

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `views/` | Vue classique du template | [→ CONTEXT](views/CONTEXT.md) |
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |
| `metadata/` | Configuration des vues | [→ CONTEXT](metadata/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `EmailTemplate.php` | Bean principal des templates email | [→ fiche](EmailTemplate.doc.md) |
| `EmailTemplateParser.php` | Parseur de variables dans les templates | [→ fiche](EmailTemplateParser.doc.md) |
| `EmailTemplateFormBase.php` | Logique de base du formulaire | [→ fiche](EmailTemplateFormBase.doc.md) |
| `EmailTemplateData.php` | Données du template | [→ fiche](EmailTemplateData.doc.md) |
| `AttachFiles.php` | Gestion des pièces jointes | [→ fiche](AttachFiles.doc.md) |
| `Save.php` | Action de sauvegarde | [→ fiche](Save.doc.md) |
| `vardefs.php` | Schéma de la table `email_templates` | [→ fiche](vardefs.doc.md) |
| `Menu.php` | Menu de navigation | [→ fiche](Menu.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `SugarBean`, gestion des pièces jointes
- **Consommé par :** `EmailMarketing` (campagnes), `AOW_Actions/actionSendEmail` (workflows)
- **Flux typique :** Création template → sélection dans campagne/workflow → variables substituées à l'envoi

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
