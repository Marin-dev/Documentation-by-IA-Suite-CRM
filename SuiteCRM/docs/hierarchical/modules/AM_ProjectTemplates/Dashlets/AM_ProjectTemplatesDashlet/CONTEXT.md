# 📁 AM_ProjectTemplatesDashlet

**Chemin :** `modules/AM_ProjectTemplates/Dashlets/AM_ProjectTemplatesDashlet/`
**Profondeur :** 5
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Dashlet affichant la liste des modèles de projets sur le tableau de bord SuiteCRM. Permet à l'utilisateur de voir rapidement ses templates de projets disponibles.

## ⚙️ Responsabilité technique
Classe PHP héritant du framework Dashlet SuiteCRM standard. Utilise un fichier `.meta.php` pour la configuration des colonnes et options d'affichage.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| — | Aucun sous-dossier | — |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `AM_ProjectTemplatesDashlet.php` | Dashlet liste des templates de projets | [→ fiche](AM_ProjectTemplatesDashlet.php.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** Framework Dashlet SuiteCRM, module `AM_ProjectTemplates`
- **Expose :** Widget tableau de bord listant les templates de projets
- **Flux typique :** Framework de tableau de bord → instancie `AM_ProjectTemplatesDashlet` → affiche liste `AM_ProjectTemplates`

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Modifier le dashlet templates de projets | [`AM_ProjectTemplatesDashlet.php`](AM_ProjectTemplatesDashlet.php.doc.md) |

---

## ⚠️ Zones INCONNU
- Contenu détaillé du dashlet non entièrement lu
