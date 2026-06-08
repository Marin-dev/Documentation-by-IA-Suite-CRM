# ⚙️ vardefs.php (vCals)

**Chemin :** `modules/vCals/vardefs.php`
**Configure :** Schéma de données du module vCals
**Dernière mise à jour doc :** 2026-05-31

## 🎯 Ce que ce fichier configure
Définit le schéma de la table `vcals` : champs `id`, `user_id`, `content`, `type` (vfb), `source` (sugar), `date_modified`, `deleted`.

## 🔑 Paramètres clés
| Paramètre | Valeur | Effet |
|---|---|---|
| `table` | `vcals` | Table du cache vCal/FREEBUSY |
| `type` | string | `vfb` pour free/busy |
| `source` | string | `sugar` pour données SuiteCRM |
| `content` | text | Contenu iCal/vCal sérialisé |

## 🔗 Impacté par / impacte
- Utilisé par `vCal::cache_sugar_vcal_freebusy()`
