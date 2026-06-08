# 📁 language

**Chemin :** `modules/ACL/language/`
**Profondeur :** 4
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier contient les fichiers de traduction du module ACL. Il fournit les libellés en anglais utilisés dans l'interface utilisateur du module ACL (labels, options de liste déroulante, messages).

## ⚙️ Responsabilité technique
Fichiers de langue PHP déclaratifs au format standard SuiteCRM (`$mod_strings`, `$app_list_strings`). Chargés automatiquement par le framework selon la locale active.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| — | Aucun sous-dossier | — |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `en_us.lang.php` | Traductions anglaises du module ACL | [→ fiche](en_us.lang.doc.md) |

### Fichiers non documentés (volontairement)
| Fichier | Raison |
|---|---|
| — | — |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** Framework SuiteCRM (chargement automatique des fichiers de langue)
- **Expose :** Tableaux `$mod_strings` utilisés par les vues du module ACL
- **Flux typique :** Le framework charge `en_us.lang.php` au démarrage de la page selon la locale configurée

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Modifier un libellé du module ACL | [`en_us.lang.php`](en_us.lang.doc.md) |

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
