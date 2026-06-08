# 📁 v4_1

**Chemin :** `service/v4_1/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Version 4_1 de l'API web service SuiteCRM — version la plus récente et recommandée pour les intégrations tierces (Outlook, applications mobiles). Ajoute le support `limit`/`offset` dans `get_relationships` et la méthode `sync_get_modified_relationships` pour la synchronisation des données.

## ⚙️ Responsabilité technique
Dernier maillon de la chaîne d'héritage v2 → v2_1 → v3 → v3_1 → v4 → v4_1. Le helper `SugarWebServiceUtilv4_1` surcharge `validate_authenticated()` avec des vérifications de session supplémentaires. Cette version est le point d'entrée par défaut pour les nouveaux développements d'intégration.

---

## 📂 Contenu

### Sous-dossiers
_(aucun)_

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `rest.php` | Point d'entrée REST v4_1 (URL recommandée pour intégrations) | [→ fiche](rest.doc.md) |
| `soap.php` | Point d'entrée SOAP v4_1 | [→ fiche](soap.doc.md) |
| `registry.php` | Registre le plus complet de l'API (toutes fonctions cumulées) | [→ fiche](registry.doc.md) |
| `SugarWebServiceImplv4_1.php` | Implémentation v4_1 (get_relationships paginé, sync_modified) | [→ fiche](SugarWebServiceImplv4_1.doc.md) |
| `SugarWebServiceUtilv4_1.php` | Helper v4_1 (validate_authenticated enrichi) | [→ fiche](SugarWebServiceUtilv4_1.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Hérite de :** `service/v4/`
- **Non étendu** — dernier maillon de la chaîne
- **Expose :** `{site_url}/service/v4_1/rest.php` et `{site_url}/service/v4_1/soap.php`

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Intégrer SuiteCRM via API (point d'entrée à utiliser) | [`rest.php`](rest.doc.md) |
| Synchroniser les relations modifiées (mobile/Outlook) | [`SugarWebServiceImplv4_1.php`](SugarWebServiceImplv4_1.doc.md) |
| Voir la validation de session v4_1 | [`SugarWebServiceUtilv4_1.php`](SugarWebServiceUtilv4_1.doc.md) |
| Voir toutes les fonctions disponibles dans l'API | [`registry.php`](registry.doc.md) |

---

## ⚠️ Zones INCONNU
- Liste complète des fonctions ajoutées au registre v4_1 vs v4 : INCONNU
- Détail complet des méthodes de `SugarWebServiceImplv4_1` non lues entièrement
