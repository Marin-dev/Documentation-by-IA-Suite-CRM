# 📄 utils.php (Surveys)

**Chemin :** `modules/Surveys/Utils/utils.php`
**Type :** PHP — Utilitaire
**Dernière mise à jour doc :** 2026-05-31

---

## 🎯 Rôle fonctionnel
Fournit une fonction utilitaire pour générer l'URL d'accès public à un sondage. Affichée dans l'interface admin pour partager le lien du sondage.

## ⚙️ Rôle technique
Fonction PHP globale `survey_url_display()`. Retourne un lien HTML `<a>` vers `entryPoint=survey` avec l'ID du sondage, uniquement si le statut est `Public`.

---

## 📥 Entrées / Dépendances
- `Surveys $survey` — objet sondage
- `$sugar_config['site_url']` — URL de base du site

## 📤 Sorties / Exports
- `survey_url_display(Surveys): string` — lien HTML ou chaîne vide

## 🔗 Relations clés
- **Appelé par :** Métadonnées de vue Edit/Detail (champ custom `survey_url`) — INCONNU exact
- **Position dans le flux global :** Affichage du lien de partage du sondage

---

## 💡 Points d'attention
- Retourne vide si statut != 'Public' — comportement attendu.
