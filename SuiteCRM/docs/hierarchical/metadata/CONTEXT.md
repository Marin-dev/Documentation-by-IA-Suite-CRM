# 📁 metadata

**Chemin :** `metadata/`
**Profondeur :** 2
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier contient les définitions de schéma de toutes les tables de jointure et tables auxiliaires de SuiteCRM. Chaque fichier déclare une entrée dans le dictionnaire global `$dictionary` avec la structure SQL (colonnes, types, index) et la définition de la relation associée (LHS/RHS, type M2M, etc.). Il couvre les relations entre modules CRM (Contacts/Accounts, Meetings/Users, etc.), les tables système (email_addresses, folders, securitygroups, audit) et les modules SuiteCRM spécifiques (projets, événements, cartes, devis, contrats...).

## ⚙️ Responsabilité technique
Fichiers de configuration PHP (données statiques, pas de logique). Chacun alimente `$dictionary` avec une clé correspondant au nom de la table ou de la relation. Le framework SuiteCRM charge ces fichiers au démarrage pour construire les métadonnées de schéma utilisées par `SugarBean`, `RelationshipFactory` et les outils d'administration (Studio, Repair). Aucune dépendance entre les fichiers — chaque métadonnée est indépendante.

---

## 📂 Contenu

### Sous-dossiers
_(aucun)_

### Fichiers documentés (sélection représentative — 80+ fichiers au total)

**Relations inter-modules CRM :**
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `accounts_contactsMetaData.php` | Table jointure Accounts ↔ Contacts (M2M) | [→ fiche](accounts_contactsMetaData.doc.md) |
| `accounts_bugsMetaData.php` | Table jointure Accounts ↔ Bugs | [→ fiche](accounts_bugsMetaData.doc.md) |
| `accounts_casesMetaData.php` | Table jointure Accounts ↔ Cases | [→ fiche](accounts_casesMetaData.doc.md) |
| `accounts_opportunitiesMetaData.php` | Table jointure Accounts ↔ Opportunities | [→ fiche](accounts_opportunitiesMetaData.doc.md) |
| `contacts_casesMetaData.php` | Table jointure Contacts ↔ Cases | [→ fiche](contacts_casesMetaData.doc.md) |
| `opportunities_contactsMetaData.php` | Table jointure Opportunities ↔ Contacts | [→ fiche](opportunities_contactsMetaData.doc.md) |
| `meetings_usersMetaData.php` | Table jointure Meetings ↔ Users | [→ fiche](meetings_usersMetaData.doc.md) |
| `calls_usersMetaData.php` | Table jointure Calls ↔ Users | [→ fiche](calls_usersMetaData.doc.md) |

**Tables système email :**
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `email_addressesMetaData.php` | Tables email_addresses, emails_email_addr_rel, email_addr_bean_rel | [→ fiche](email_addressesMetaData.doc.md) |
| `emails_beansMetaData.php` | Lien polymorphe email ↔ beans | [→ fiche](emails_beansMetaData.doc.md) |
| `foldersMetaData.php` | Tables folders, folders_subscriptions, folders_rel | [→ fiche](foldersMetaData.doc.md) |
| `email_cacheMetaData.php` | Cache emails IMAP | [→ fiche](email_cacheMetaData.doc.md) |

**Sécurité et accès :**
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `securitygroups_usersMetaData.php` | Table jointure SecurityGroups ↔ Users | [→ fiche](securitygroups_usersMetaData.doc.md) |
| `securitygroups_recordsMetaData.php` | Table jointure SecurityGroups ↔ Enregistrements | [→ fiche](securitygroups_recordsMetaData.doc.md) |
| `acl_roles_usersMetaData.php` | Table jointure ACL Roles ↔ Users | [→ fiche](acl_roles_usersMetaData.doc.md) |
| `roles_usersMetaData.php` | Table jointure Roles ↔ Users | [→ fiche](roles_usersMetaData.doc.md) |
| `oauth_nonce.php` | Table nonce OAuth | [→ fiche](oauth_nonce.doc.md) |

**Modules SuiteCRM spécifiques :**
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `aos_quotes_aos_contractsMetaData.php` | Table jointure Quotes ↔ Contracts | [→ fiche](aos_quotes_aos_contractsMetaData.doc.md) |
| `project_users_1MetaData.php` | Table jointure Projects ↔ Users | [→ fiche](project_users_1MetaData.doc.md) |
| `fp_events_contactsMetaData.php` | Table jointure Events ↔ Contacts | [→ fiche](fp_events_contactsMetaData.doc.md) |
| `jjwg_maps_jjwg_markersMetaData.php` | Table jointure Maps ↔ Markers | [→ fiche](jjwg_maps_jjwg_markersMetaData.doc.md) |
| `audit_templateMetaData.php` | Template de table d'audit (utilisé pour tous les modules auditables) | [→ fiche](audit_templateMetaData.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** variable globale `$dictionary` (framework SugarCRM), constante `sugarEntry`
- **Expose :** définitions de schéma chargées par `modules/TableDictionary.php`, utilisées par `data/Relationships/RelationshipFactory.php`, `data/SugarBean.php`, Studio et les outils de Repair
- **Flux typique :** démarrage SuiteCRM → `TableDictionary.php` inclut les `*MetaData.php` → `$dictionary` peuplé → `RelationshipFactory::getRelationship()` utilise ces métadonnées pour instancier les objets de relation

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Voir le schéma de la relation Accounts↔Contacts | [`accounts_contactsMetaData.php`](accounts_contactsMetaData.doc.md) |
| Comprendre les tables email (adresses, destinataires, liens beans) | [`email_addressesMetaData.php`](email_addressesMetaData.doc.md) |
| Comprendre le schéma des dossiers email | [`foldersMetaData.php`](foldersMetaData.doc.md) |
| Voir la structure des groupes de sécurité | [`securitygroups_usersMetaData.php`](securitygroups_usersMetaData.doc.md) |
| Comprendre la table d'audit | [`audit_templateMetaData.php`](audit_templateMetaData.doc.md) |

---

## ⚠️ Zones INCONNU
- 70+ fichiers documentés mais non lus en détail dans ce résumé — consulter les fiches individuelles pour le schéma précis de chaque table
- `custom_fieldsMetaData.php` : structure de la table `fields_meta_data` pour les champs personnalisés Studio (non lue en entier)
- `queues_queueMetaData.php`, `queues_beansMetaData.php` : système de file d'attente (non lus)
