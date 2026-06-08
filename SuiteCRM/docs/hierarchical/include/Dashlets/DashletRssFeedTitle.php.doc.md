# 📄 DashletRssFeedTitle.php

**Chemin :** `include/Dashlets/DashletRssFeedTitle.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-06-02

---

## 🎯 Rôle fonctionnel
Classe utilitaire permettant de parser le titre d'un flux RSS en préservant l'encodage UTF-8. Utilisée par le dashlet RSS pour afficher le titre du flux distant dans le tableau de bord.

## ⚙️ Rôle technique
Lit les premiers octets d'un flux RSS (`$readBytes = 8192`) via un parser XML SAX (`xml_parser_create()`). L'encodage par défaut est UTF-8 (`$defaultEncoding`). Ne hérite d'aucune classe — classe helper autonome sans dépendances internes déclarées.

---

## 📥 Entrées / Dépendances
- **Imports principaux :** aucun `require_once` dans le fichier
- **Arguments :** URL ou contenu du flux RSS (INCONNU — méthodes à vérifier)

## 📤 Sorties / Exports
- `DashletRssFeedTitle` — classe (helper) — extracteur de titre RSS
- **Consommateurs identifiés dans le repo :** INCONNU (dashlet RSS dans `modules/`)

## 🔗 Relations clés
- **Appelé par :** dashlet RSS (INCONNU — chemin exact non identifié)
- **Appelle :** fonctions PHP natives XML (`xml_parser_create`)
- **Position dans le flux global :** utilitaire de parsing appelé lors du rendu du dashlet RSS

---

## 💡 Points d'attention
- Le fichier ne contient pas le guard `sugarEntry` (présence de la licence mais pas du `die('Not A Valid Entry Point')`).
- La constante `$readBytes = 8192` limite la lecture à 8 Ko — les flux avec un titre loin dans le XML pourraient ne pas être parsés correctement.
