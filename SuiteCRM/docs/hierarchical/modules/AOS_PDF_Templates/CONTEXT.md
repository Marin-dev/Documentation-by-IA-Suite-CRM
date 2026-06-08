# 📁 AOS_PDF_Templates

**Chemin :** `modules/AOS_PDF_Templates/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module AOS_PDF_Templates gère les modèles de documents PDF dans SuiteCRM. Il permet de créer des gabarits avec en-tête, corps et pied de page contenant des variables `{tablename_fieldname}` substituées dynamiquement. Utilisé pour générer des PDF de devis, factures, contrats et autres documents officiels.

## ⚙️ Responsabilité technique
Bean `AOS_PDF_Templates` (hérite de `AOS_PDF_Templates_sugar`) avec purification HTML anti-XSS. Moteur de substitution `templateParser` remplace les variables par les valeurs des beans. `generatePdf.php` produit le PDF via `SuiteCRM\PDF\PDFWrapper` (mPDF). Des templates d'exemple sont fournis dans `samples/`.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `views/` | Vues détail et édition des templates | [→ CONTEXT](views/CONTEXT.md) |
| `Dashlets/` | Dashlet liste des templates PDF | [→ CONTEXT](Dashlets/CONTEXT.md) |
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |
| `samples/` | Templates PDF d'exemple par module | [→ CONTEXT](samples/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `AOS_PDF_Templates.php` | Bean template PDF (avec purification HTML) | [→ fiche](AOS_PDF_Templates.doc.md) |
| `templateParser.php` | Moteur de substitution des variables `{tablename_field}` | [→ fiche](templateParser.doc.md) |
| `generatePdf.php` | Script de génération et téléchargement PDF | [→ fiche](generatePdf.doc.md) |
| `sendEmail.php` | Envoi du PDF généré par email | [→ fiche](sendEmail.doc.md) |
| `formLetter.php` / `formLetterPdf.php` | Génération de lettres type | [→ fiche](formLetter.doc.md) |
| `TemplateSampleService.php` | Service d'installation des templates démo | [→ fiche](TemplateSampleService.doc.md) |
| `vardefs.php` | Schéma de la table `aos_pdf_templates` | [→ fiche](vardefs.php.doc.md) |
| `Menu.php` | Menu de navigation | [→ fiche](Menu.doc.md) |
| `Forms.php` | Helpers de formulaire | [→ fiche](Forms.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `SuiteCRM\PDF\PDFWrapper` (mPDF), `BeanFactory`, `purify_html()`, `$locale`
- **Consommé par :** Boutons "Générer PDF" sur les DetailViews AOS, `AOW_Actions` (workflows), `AOS_PDF_Templates/generatePdf.php`
- **Flux typique :** Utilisateur clique "PDF" → `generatePdf.php` → `templateParser::parse_template()` → `PDFWrapper::getPDFEngine()` → téléchargement

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre le moteur de variables | [`templateParser.php`](templateParser.doc.md) |
| Voir la génération PDF | [`generatePdf.php`](generatePdf.doc.md) |
| Voir des exemples de templates | [`samples/`](samples/CONTEXT.md) |

---

## ⚠️ Zones INCONNU
- `templateParser` : logique complète des line_item_groups non lue entièrement
- `generatePdf.php` : construction complète du PDF non lue
- Purification HTML : seul `<iframe>` est interdit — autres balises dangereuses non filtrées
