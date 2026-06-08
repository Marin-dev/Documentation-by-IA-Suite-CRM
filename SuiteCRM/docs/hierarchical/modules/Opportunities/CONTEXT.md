# 📁 Opportunities

**Chemin :** `modules/Opportunities/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module Opportunities gère les opportunités commerciales dans SuiteCRM. Une opportunité représente une transaction commerciale potentielle avec un montant, une date de clôture et une étape de vente. Pivot entre les comptes, contacts et activités commerciales. Central dans le pipeline de vente.

## ⚙️ Responsabilité technique
Bean `Opportunity` (hérite de `SugarBean`). Table `opportunities`. Conversion automatique des montants en USD via `SaveOverload.php`. Probabilité calculée depuis `sales_probability_dom`. Relations M:M vers `accounts_opportunities` et `opportunities_contacts`. Hook de géolocalisation JJWG.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `views/` | Vue détail personnalisée | [→ CONTEXT](views/CONTEXT.md) |
| `Dashlets/` | Dashlets mes opportunités (ouvertes et clôturées) | [→ CONTEXT](Dashlets/CONTEXT.md) |
| `SugarFeeds/` | Feed SugarFeed | [→ CONTEXT](SugarFeeds/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `Opportunity.php` | Bean principal des opportunités | [→ fiche](Opportunity.doc.md) |
| `Save.php` | Action de sauvegarde | [→ fiche](Save.doc.md) |
| `SaveOverload.php` | Conversion montant en USD | [→ fiche](SaveOverload.doc.md) |
| `OpportunityFormBase.php` | Logique de base du formulaire | [→ fiche](OpportunityFormBase.doc.md) |
| `OpportunitiesJjwg_MapsLogicHook.php` | Hook de géolocalisation | [→ fiche](OpportunitiesJjwg_MapsLogicHook.doc.md) |
| `OpportunitiesListViewSmarty.php` | Rendu Smarty de la vue liste | [→ fiche](OpportunitiesListViewSmarty.doc.md) |
| `vardefs.php` | Schéma de la table `opportunities` | [→ fiche](vardefs.doc.md) |
| `field_arrays.php` | Tableaux de champs | [→ fiche](field_arrays.doc.md) |
| `Menu.php` | Menu de navigation | [→ fiche](Menu.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `SugarBean`, `BeanFactory`, `SecurityGroup`, `SaveOverload`
- **Consommé par :** Modules Accounts, Contacts (relations), Leads (après conversion), `AOS_Quotes` (via `createOpportunity`)
- **Flux typique :** Création opportunité → liaison compte+contacts → suivi étapes → conversion → clôture

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre le bean Opportunity | [`Opportunity.php`](Opportunity.doc.md) |
| Voir la conversion USD des montants | [`SaveOverload.php`](SaveOverload.doc.md) |

---

## ⚠️ Zones INCONNU
- `getCurrencyType()` : fonction vide hors classe (vestige de code)
- `update_currency_id()` n'affecte que les opportunités non clôturées
