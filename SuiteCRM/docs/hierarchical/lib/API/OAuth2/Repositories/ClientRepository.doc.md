# 📄 ClientRepository.php

**Chemin :** `lib/API/OAuth2/Repositories/ClientRepository.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Repository OAuth2 pour les clients enregistrés dans SuiteCRM. Charge les informations client depuis la table `OAuth2Clients` et valide les credentials + grant type autorisé.

## ⚙️ Rôle technique
Implémente `ClientRepositoryInterface`. Méthodes :
- `getClientEntity(string $clientIdentifier)` : charge le bean `OAuth2Clients` par identifiant, retourne null si inexistant, sinon crée un `ClientEntity` avec `name`, `redirect_uri`, `is_confidential`
- `validateClient(string $clientIdentifier, string $clientSecret, string $grantType)` : vérifie que le `grantType` correspond à `allowed_grant_type` (ou est `refresh_token`), puis compare `hash('sha256', $clientSecret)` avec `$client->secret`

---

## 📥 Entrées / Dépendances
- `League\OAuth2\Server\Repositories\ClientRepositoryInterface`
- `SuiteCRM\API\OAuth2\Entities\ClientEntity`
- `\OAuth2Clients` (SugarBean)

## 📤 Sorties / Exports
- `ClientRepository` — classe (repository)
  - `getClientEntity(string): ?ClientEntity`
  - `validateClient(string, string, string): bool|null`
- **Consommateurs identifiés :** librairie League OAuth2 (interne)

---

## 💡 Points d'attention
- Le secret client est stocké haché en SHA-256 dans la BD — vérifier que ce hachage est cohérent avec la création de clients via l'interface SuiteCRM.
- `validateClient()` peut retourner `null` si le client n'existe pas (au lieu de `false`) — comportement à vérifier avec la librairie League.
- `refresh_token` est toujours autorisé quel que soit le `allowed_grant_type` configuré.
