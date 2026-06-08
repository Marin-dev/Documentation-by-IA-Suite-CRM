# 📁 OptimisticLock

**Chemin :** `modules/OptimisticLock/`
**Profondeur :** 2
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module OptimisticLock implémente le mécanisme de verrouillage optimiste pour prévenir les conflits d'édition concurrente dans SuiteCRM. Lorsque deux utilisateurs modifient le même enregistrement simultanément, ce module détecte les conflits, affiche les différences champ par champ entre la version de l'utilisateur et la version en base, et permet à l'utilisateur de choisir quelle version conserver.

## ⚙️ Responsabilité technique
`LockResolve.php` est la pièce centrale : la fonction `display_conflict_between_objects()` compare deux états d'un bean (version session vs version BDD) et génère un tableau HTML des différences. Il utilise la session PHP (`$_SESSION['o_lock_object']`, `o_lock_module`, `o_lock_save`) pour stocker l'état en conflit. La résolution se fait via deux liens : "Accepter la vôtre" (rejoue la sauvegarde depuis la session) ou "Accepter la base" (redirige vers la DetailView). `Forms.php` fournit des helpers pour la détection de conflit.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `language/` | Traductions (LBL_YOURS, LBL_IN_DATABASE, LBL_CONFLICT_EXISTS, etc.) | Pas de CONTEXT.md |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `LockResolve.php` | Affichage et résolution des conflits de sauvegarde concurrente | Pas de fiche |
| `Forms.php` | Helpers pour la détection de verrou optimiste avant sauvegarde | Pas de fiche |

### Fichiers non documentés (volontairement)
| Fichier | Raison |
|---|---|
| `Menu.php` | Menu standard minimal |
| `language/en_us.lang.php` | Traductions standard |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `BeanFactory::getBean()` (chargement de l'état courant en BDD), `$_SESSION` (stockage de l'objet en conflit), `SugarApplication::redirect()` (redirection après résolution), `SugarCleaner::cleanHtml()` (sanitisation des valeurs), `return_module_language()` (strings de traduction).
- **Expose :** Action `LockResolve` accessible via `index.php?module=OptimisticLock&action=LockResolve`. Utilisé par la couche de sauvegarde SugarBean quand un conflit est détecté.
- **Flux typique :** Utilisateur A et B éditent le même enregistrement → A sauvegarde en premier → B tente de sauvegarder → mécanisme de détection (dans `Forms.php`) déclenche le redirect vers `LockResolve` → affichage des différences → B choisit quelle version garder → résolution.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre la résolution de conflits | [`LockResolve.php`](LockResolve.php) |
| Comprendre la détection de conflit au save | [`Forms.php`](Forms.php) |
| Voir les libellés de l'interface | [`language/en_us.lang.php`](language/en_us.lang.php) |

---

## ⚠️ Zones INCONNU
- Mécanisme exact dans `Forms.php` pour détecter le conflit avant sauvegarde (timestamp comparaison ?) : non lu en détail.
- Quels modules déclenchent effectivement ce mécanisme (opt-in ou global ?) : INCONNU sans analyse de la couche SugarBean.
