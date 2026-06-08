# 📁 metadata

**Chemin :** `modules/ACL/metadata/`
**Profondeur :** 4
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier contient les métadonnées de configuration des vues du module ACL. Il définit les sous-panneaux affichés dans les vues détail des enregistrements ACL.

## ⚙️ Responsabilité technique
Fichiers PHP déclaratifs au format standard SuiteCRM (`$subpanel_def`). Chargés par le moteur de vues SuiteCRM pour construire dynamiquement les sous-panneaux.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| — | Aucun sous-dossier | — |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `subpaneldefs.php` | Définition des sous-panneaux du module ACL | [→ fiche](subpaneldefs.doc.md) |

### Fichiers non documentés (volontairement)
| Fichier | Raison |
|---|---|
| — | — |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** Framework SuiteCRM (moteur de vues, SubpanelFactory)
- **Expose :** Configuration des sous-panneaux pour les vues ACL
- **Flux typique :** Le moteur de vues charge `subpaneldefs.php` pour afficher les relations sous forme de sous-panneaux dans les vues détail

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Configurer les sous-panneaux ACL | [`subpaneldefs.php`](subpaneldefs.doc.md) |

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
