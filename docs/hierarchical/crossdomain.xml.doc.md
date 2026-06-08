# crossdomain.xml (configuration)

**Chemin :** `crossdomain.xml`
**Configure :** `Politique cross-domain Adobe Flash/Silverlight`
**Dernière mise à jour doc :** 2026-05-28

---

## Ce que ce fichier configure
Déclare la politique d'accès cross-domain pour les clients Flash et Silverlight (technologie Adobe). Interdit explicitement tout accès cross-domain depuis ces clients.

## Paramètres clés

| Paramètre | Valeur | Effet |
|---|---|---|
| `site-control permitted-cross-domain-policies` | `none` | Aucune politique cross-domain n'est autorisée — refuse tout accès Flash/Silverlight cross-domain |

## Impacté par / impacte
- Consommé automatiquement par les clients Flash/Silverlight lors de requêtes cross-origin vers le domaine SuiteCRM
- Aucune dépendance interne au code SuiteCRM

## Notes techniques
- Flash et Silverlight sont des technologies obsolètes (support arrêté en 2020-2021). Ce fichier est maintenu pour des raisons de sécurité défensive.
- La valeur `none` est la posture la plus restrictive possible — recommandée comme bonne pratique de sécurité.
- Ce fichier doit être accessible à l'URL racine : `https://[domaine]/crossdomain.xml`.
