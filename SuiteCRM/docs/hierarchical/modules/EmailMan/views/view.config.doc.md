# view.config.php (EmailMan)

**Chemin :** `modules/EmailMan/views/view.config.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Vue de configuration globale de l'envoi email (SMTP, opt-in, securite XSS, import). Accessible uniquement aux administrateurs. Alimente le template Smarty `modules/EmailMan/tpls/config.tpl`.

**Type :** view

---

## Dependances cles
- `SugarView` (classe parente)
- `Forms.php` (EmailMan)
- `OutboundEmail` (`include/OutboundEmail/OutboundEmail.php`)
- `Configurator`
- `BeanFactory` (Administration, Emails)

---

## Exports / Symboles principaux
| Symbole | Type | Role |
|---|---|---|
| `ViewConfig` | classe | Vue configuration email globale |
| `display()` | methode | Rendu de la page de configuration |
| `preDisplay()` | methode | Controle d'acces admin |

---

## Notes
- Expose les parametres SMTP, opt-in confirme, import email, securite XSS via Smarty.
- Lit `$sugar_config['legacy_email_behaviour']` pour basculer l'affichage legacy.
