# 📄 view.detail.php

**Chemin :** `modules/AOK_KnowledgeBase/views/view.detail.php`
**Type :** PHP — Vue (DetailView)
**Dernière mise à jour doc :** 2026-05-31

---

## 🎯 Rôle fonctionnel
Vue de détail d'un article de base de connaissances. Décode les entités HTML dans le champ `description` avant affichage pour garantir un rendu correct du contenu riche (HTML/texte).

## ⚙️ Rôle technique
Étend `ViewDetail`. Surcharge `display()` pour appeler `setDecodeHTML()` qui remplace `&nbsp;` par des espaces et décode les entités HTML du champ `description` avant le rendu standard.

---

## 📥 Entrées / Dépendances
- `ViewDetail` — classe parente SuiteCRM
- `$this->bean->description` — contenu de l'article

## 📤 Sorties / Exports
- `AOK_KnowledgeBaseViewDetail extends ViewDetail` — vue détail article KB

## 🔗 Relations clés
- **Appelé par :** Framework MVC (action DetailView du module AOK_KnowledgeBase)
- **Position dans le flux global :** Affichage d'un article de la base de connaissances

---

## 💡 Points d'attention
- `html_entity_decode` + `str_replace('&nbsp;', ' ')` corrige les problèmes d'encodage du contenu HTML stocké — indique que le champ description contient du HTML entity-encodé.
