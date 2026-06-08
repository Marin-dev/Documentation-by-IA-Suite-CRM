# crossdomain.xml (configuration)

**Chemin :** `crossdomain.xml`
**Configure :** `Politique d'accès cross-domaine pour Flash/Flex (Adobe)`
**Dernière mise à jour doc :** 2026-05-30

## Rôle

Fichier de politique de sécurité cross-domaine au format XML destiné aux clients Flash/Flex. Indique aux clients Flash que l'accès cross-domaine est interdit (`none`).

**Type :** config

## Ce que ce fichier configure

Interdit explicitement toute politique cross-domaine pour les clients Flash en définissant `permitted-cross-domain-policies="none"`.

## Paramètres clés

| Paramètre | Valeur | Effet |
|---|---|---|
| `permitted-cross-domain-policies` | `none` | Interdit aux clients Flash d'accéder à SuiteCRM depuis un autre domaine |

## Impacté par / impacte

- Consommé automatiquement par les plugins Flash/Flex lors de requêtes cross-domaine
- Conforme au DTD Macromedia : `http://www.macromedia.com/xml/dtds/cross-domain-policy.dtd`

## Points d'attention

- Flash Player est en fin de vie (EOL décembre 2020) — ce fichier est obsolète dans la pratique mais conservé pour compatibilité.
- La politique `none` est la plus restrictive et sécurisée — ne pas l'assouplir.
- Pour les politiques CORS modernes (JavaScript), voir la configuration Apache/Nginx, non ce fichier.
