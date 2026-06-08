# 📁 samples

**Chemin :** `modules/AOS_PDF_Templates/samples/`
**Profondeur :** 4
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Contient des templates PDF d'exemple pour les principaux modules AOS (Account, Contact, Invoice, Quote, Lead). Ces exemples illustrent l'utilisation des variables `{tablename_fieldname}` dans les templates.

## ⚙️ Responsabilité technique
Scripts PHP procéduraux qui créent des enregistrements `AOS_PDF_Templates` en base lors de l'installation/démo. Référencés par `TemplateSampleService`.

---

## 📂 Contenu

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `smpl_Account_Sample.php` | Template exemple pour les comptes | [→ fiche](smpl_Account_Sample.php.doc.md) |
| `smpl_Contact_Sample.php` | Template exemple pour les contacts | [→ fiche](smpl_Contact_Sample.php.doc.md) |
| `smpl_Invoice_Sample.php` | Template exemple pour les factures | [→ fiche](smpl_Invoice_Sample.php.doc.md) |
| `smpl_Invoice_Group_Sample.php` | Template exemple avec groupes de lignes (facture) | [→ fiche](smpl_Invoice_Group_Sample.php.doc.md) |
| `smpl_Lead_Sample.php` | Template exemple pour les prospects | [→ fiche](smpl_Lead_Sample.php.doc.md) |
| `smpl_Quote_Sample.php` | Template exemple pour les devis | [→ fiche](smpl_Quote_Sample.php.doc.md) |
| `smpl_Quote_Group_Sample.php` | Template exemple avec groupes de lignes (devis) | [→ fiche](smpl_Quote_Group_Sample.php.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consommé par :** `TemplateSampleService` pour l'installation des templates démo

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
