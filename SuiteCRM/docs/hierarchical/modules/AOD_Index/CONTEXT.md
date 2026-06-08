# 📁 AOD_Index

**Chemin :** `modules/AOD_Index/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module AOD_Index (Advanced OpenDiscovery) gère l'indexation full-text basée sur Lucene dans SuiteCRM. Il permet la recherche globale dans tous les modules et documents. **Ce module est déprécié depuis v7.12.0** et remplacé par ElasticSearch/AOSearch. Il est conservé pour compatibilité arrière.

## ⚙️ Responsabilité technique
Bean `AOD_Index` (hérite de `Basic`/SugarBean) avec moteur Zend Lucene. Logic hooks déclenchent l'indexation sur save/delete de tout bean. La librairie Zend dans `Lib/` est remplacée par des stubs vides, la vraie librairie étant chargée via Composer. `LuceneUtils` convertit les fichiers (PDF, DOCX, ODT...) en documents Lucene.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `language/` | Traductions anglaises du module | [→ CONTEXT](language/CONTEXT.md) |
| `metadata/` | Configuration des vues | [→ CONTEXT](metadata/CONTEXT.md) |
| `views/` | Vue des statistiques de l'index | [→ CONTEXT](views/CONTEXT.md) |
| `Lib/` | Stubs de compatibilité Zend Lucene (vides) | [→ CONTEXT](Lib/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `AOD_Index.php` | Service central d'indexation Lucene | [→ fiche](AOD_Index.doc.md) |
| `LuceneUtils.php` | Utilitaires de conversion fichier → document Lucene | [→ fiche](LuceneUtils.doc.md) |
| `PdfParser.php` | Parseur PDF pour extraction de texte | [→ fiche](PdfParser.doc.md) |
| `AOD_LogicHooks.php` | Logic hooks déclenchant l'indexation sur save/delete | [→ fiche](AOD_LogicHooks.doc.md) |
| `controller.php` | Contrôleur HTTP (stats index + optimisation manuelle) | [→ fiche](controller.doc.md) |
| `vardefs.php` | Schéma du bean AOD_Index | [→ fiche](vardefs.doc.md) |

### Fichiers non documentés (volontairement)
| Fichier | Raison |
|---|---|
| `AOD_Index_sugar.php` | Classe générée automatiquement |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `Zend_Search_Lucene` (via Composer), `BeanFactory`, `VardefManager`, `$sugar_config['aod']['enable_aod']`
- **Consommé par :** Logic hooks sur tous les beans SuiteCRM, interface d'administration (optimisation manuelle)
- **Flux typique :** Bean save → `AOD_LogicHooks::after_save()` → `AOD_Index::getIndex()->index($module, $id)` → document Lucene écrit sur disque

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre le service d'indexation principal | [`AOD_Index.php`](AOD_Index.doc.md) |
| Voir comment les fichiers sont convertis pour Lucene | [`LuceneUtils.php`](LuceneUtils.doc.md) |
| Comprendre le déclenchement automatique de l'indexation | [`AOD_LogicHooks.php`](AOD_LogicHooks.doc.md) |
| Déclencher une optimisation manuelle | [`controller.php`](controller.doc.md) |

---

## ⚠️ Zones INCONNU
- **Déprécié depuis v7.12.0** — ne pas utiliser pour de nouveaux développements
- Bug potentiel : `case 'application/rtf'` sans break dans `LuceneUtils.php`
- `getLuceneIndex()` recharge l'index à chaque appel — performance potentiellement dégradée en boucle
- Chemin du scheduler d'indexation batch non vérifié
