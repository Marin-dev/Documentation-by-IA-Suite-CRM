# pdf.php

**Chemin :** `pdf.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle fonctionnel

Point d'entrée HTTP pour la génération de documents PDF depuis les enregistrements CRM. Charge le bean cible et délègue la génération au fichier d'action spécifique du module.

**Type :** entrypoint

## Rôle technique

Vérifie la présence des paramètres obligatoires (`module`, `action`, `record`), récupère l'entité via `BeanFactory`, charge l'enregistrement, puis inclut dynamiquement `modules/{module}/{action}.php` pour exécuter la génération PDF.

---

## Dépendances clés

- **Globals utilisés :** `$beanList`, `$beanFiles`, `$locale`
- **Paramètres d'entrée ($_REQUEST) :**
  - `module` — module CRM (ex: `AOS_PDF_Templates`, `Quotes`)
  - `action` — action à exécuter dans le module (ex: `Popup`, `index`)
  - `record` — ID de l'enregistrement à convertir en PDF
- **Sécurité :** bloque si `sugarEntry` non défini (ligne 2)

## Sorties / Comportement

- Inclut `modules/{module}/{action}.php` avec `$GLOBALS['focus']` préchargé contenant l'enregistrement
- La sortie (PDF binaire) est produite par le fichier d'action inclus

## Relations clés

- **Appelé par :** liens "Générer PDF" dans les modules supportant la génération PDF (AOS_PDF_Templates, Quotes, AOS_Invoices…)
- **Appelle :** `BeanFactory::newBean()`, `$focus->retrieve()`, `modules/{module}/{action}.php`

---

## Points d'attention

- `clean_string()` appliqué sur `module` et `action` (ligne 48-50) pour éviter la traversée de répertoire.
- La génération PDF effective est dans le fichier d'action du module — ce fichier est uniquement un dispatcher.
- Aucune vérification ACL explicite dans ce fichier — délégué aux modules inclus.
