# 📁 vCals

**Chemin :** `modules/vCals/`
**Profondeur :** 2
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce module gère la **synchronisation calendrier au format vCal/iCal** (RFC 5545). Il permet d'exporter les rendez-vous (`Meetings`) et les tâches (`Tasks`) de SuiteCRM au format iCalendar, consommable par des clients externes (Outlook, Google Calendar, etc.). Il implémente également un serveur WebDAV pour la synchronisation bidirectionnelle.

## ⚙️ Responsabilité technique
La classe `vCal` étend `SugarBean` et mappe la table `vcals`. Elle définit des constantes de formatage iCal (`UTC_FORMAT`, `EOL`, `TAB`, `CHARSPERLINE`). Elle dépend de `modules/Calendar/Calendar.php`. `HTTP_WebDAV_Server_vCal.php` implémente un serveur WebDAV pour le protocole CalDAV. `Server.php` est le point d'entrée du serveur. Le tracking est désactivé (`$tracker_visibility = false`). La sécurité par équipes est désactivée.

---

## 📂 Contenu

### Sous-dossiers
Aucun sous-dossier.

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `vCal.php` | Entité principale : génération de contenu iCal depuis les meetings/tasks SuiteCRM | — |
| `HTTP_WebDAV_Server_vCal.php` | Serveur WebDAV pour synchronisation calendrier bidirectionnelle | — |
| `Server.php` | Point d'entrée du serveur WebDAV/vCal | — |
| `vardefs.php` | Définition des champs de l'entité | — |
| `field_arrays.php` | Tableaux de colonnes DB | — |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `modules/Calendar/Calendar.php` ; modules `Meetings` et `Tasks` pour récupérer les données à exporter.
- **Expose :** Endpoint `vcal_server.php` (à la racine du repo) pour les clients calendrier externes.
- **Flux typique :** Client calendrier externe (Outlook) envoie une requête WebDAV → `vcal_server.php` instancie `Server.php` → `HTTP_WebDAV_Server_vCal.php` construit le flux iCal depuis `vCal::buildVCalendarFromMeetings()` → retour au client.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre la génération du contenu iCal | `vCal.php` |
| Modifier le serveur WebDAV | `HTTP_WebDAV_Server_vCal.php` |
| Trouver le point d'entrée externe | `vcal_server.php` (racine repo) |
| Consulter la structure DB | `vardefs.php` |

---

## ⚠️ Zones INCONNU
- Le support exact du protocole CalDAV vs WebDAV simple n'est pas confirmé depuis le seul code lu.
- Les méthodes de `vCal.php` au-delà de la ligne 80 (constructeur) nécessitent lecture complète.
