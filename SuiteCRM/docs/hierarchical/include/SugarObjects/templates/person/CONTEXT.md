# 📁 person

**Chemin :** `include/SugarObjects/templates/person/`
**Profondeur :** 5
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier contient le template de bean pour les objets représentant des personnes physiques dans SuiteCRM (Contacts, Leads). Il étend `Basic` avec les champs spécifiques aux personnes : identité, coordonnées et conformité RGPD.

## ⚙️ Responsabilité technique
Étend `Basic`. Déclare les propriétés publiques typiques d'une personne (nom, prénom, emails, téléphones, champs RGPD).

---

## 📂 Contenu

### Sous-dossiers
Aucun.

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `Person.php` | Template bean pour les personnes physiques (Contact, Lead) avec champs RGPD | [→ fiche](Person.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `Basic` (héritage)
- **Expose :** classe `Person` — héritée par les modules Contacts et Leads

---

## ⚠️ Zones INCONNU
- Méthodes internes de `Person` non entièrement lues — comportement complet INCONNU.
