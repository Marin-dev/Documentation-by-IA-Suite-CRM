# 📁 EmailText

**Chemin :** `modules/EmailText/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module EmailText stocke le corps texte brut des emails (séparation du corps HTML vs texte). Utilisé pour stocker le corps texte des emails archivés dans SuiteCRM.

## ⚙️ Responsabilité technique
Bean `EmailText` (hérite de `SugarBean`). Module de stockage simple sans interface utilisateur significative.

---

## 📂 Contenu

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `EmailText.php` | Bean corps texte brut d'un email | [→ fiche](EmailText.doc.md) |
| `vardefs.php` | Schéma de la table | [→ fiche](vardefs.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consommé par :** Module `Emails` (stockage du corps texte)

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
