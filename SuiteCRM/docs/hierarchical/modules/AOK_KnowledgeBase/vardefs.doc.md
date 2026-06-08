# Fichier : vardefs.php

**Chemin :** `modules/AOK_KnowledgeBase/vardefs.php`
**Type :** PHP — configuration (vardefs SugarCRM)
**Derniere mise a jour doc :** 2026-06-02

---

## Ce que ce fichier configure
Definit le schema de la table `aok_knowledgebase` pour SugarCRM. Champs specifiques : `status` (enum), `revision` (varchar), `author` (`user_id_c`), `approver` (`user_id1_c`). Definit la relation avec AOK_Knowledge_Base_Categories.

## Parametres cles
| Champ | Type | Effet |
|---|---|---|
| `status` | enum | Statut de l'article (Draft, Published, Expired, etc.) |
| `revision` | varchar | Numero de revision |
| `user_id_c` (author) | relate | Auteur de l'article |
| `user_id1_c` (approver) | relate | Approbateur de l'article |

## Impacte par / impacte
- Consomme par `AOK_KnowledgeBase.php`, BeanFactory
- Relation vers `AOK_Knowledge_Base_Categories`

## Points d'attention
- Les champs `user_id_c` et `user_id1_c` ont le suffixe `_c` — champs custom generes par Module Builder.
