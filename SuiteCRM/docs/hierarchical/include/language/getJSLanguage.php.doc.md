# 📄 getJSLanguage.php

**Chemin :** `include/language/getJSLanguage.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-06-02

---

## 🎯 Rôle fonctionnel
Point d'entrée HTTP qui génère et retourne le fichier de cache JavaScript des chaînes de langue pour le frontend. Appelé par le navigateur via une balise `<script src="...?lang=en_us">` pour charger les traductions côté client.

## ⚙️ Rôle technique
Fonction procédurale `getJSLanguage()`. Lit `$_REQUEST['lang']` pour déterminer la langue demandée, délègue la génération à `jsLanguage.php` et retourne le contenu JS mis en cache. Retourne une erreur texte si la langue n'est pas spécifiée.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `include/language/jsLanguage.php` — générateur de cache JS
- **Variables d'environnement :** `$_REQUEST['lang']` — code de langue (ex: `en_us`)
- **Variables globales :** `$app_list_strings`

## 📤 Sorties / Exports
- `getJSLanguage()` — fonction (helper/endpoint) — génération du cache JS de langue
- **Sortie :** contenu JavaScript (`SUGAR.language.setLanguage(...)`)

## 🔗 Relations clés
- **Appelé par :** navigateur client via balise `<script>` dans les templates de layout
- **Appelle :** `jsLanguage.php`
- **Position dans le flux global :** chargement des traductions côté client au rendu de la page

---

## 💡 Points d'attention
- `clean_path($_REQUEST['lang'])` est appliqué (ligne 60) — protection contre les path traversal.
- Si la langue demandée n'existe pas, le comportement de fallback est INCONNU.
