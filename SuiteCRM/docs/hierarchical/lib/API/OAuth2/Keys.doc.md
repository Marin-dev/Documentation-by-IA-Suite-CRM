# 📄 Keys.php

**Chemin :** `lib/API/OAuth2/Keys.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Gère les clés RSA (publique et privée) utilisées pour signer et vérifier les tokens JWT OAuth2. Génère automatiquement les clés si elles n'existent pas encore sur le système de fichiers.

## ⚙️ Rôle technique
Classe avec trois méthodes : `getPublicKey()`, `getPrivateKey()` (vérifient l'existence du fichier, génèrent via OpenSSL si absent), `setUpKeys()` (génère une paire RSA 2048 bits avec SHA-512, écrit `public.key` et `private.key` dans le même répertoire que ce fichier : `lib/API/OAuth2/`).

---

## 📥 Entrées / Dépendances
- `SuiteCRM\API\v8\Exception\ApiException`
- Extension PHP `openssl` requise
- Fichiers : `lib/API/OAuth2/private.key`, `lib/API/OAuth2/public.key` (créés automatiquement)

## 📤 Sorties / Exports
- `Keys` — classe (service)
  - `getPublicKey(): string` — contenu de la clé publique
  - `getPrivateKey(): string` — contenu de la clé privée
- **Consommateurs identifiés :** INCONNU (probablement containers OAuth2 dans `lib/API/v8/container/`)

## 🔗 Relations clés
- **Appelé par :** INCONNU (bootstrap OAuth2)
- **Position dans le flux global :** initialisation des clés JWT pour `AuthorizationServer`

---

## 💡 Points d'attention
- Les clés sont stockées en clair dans `lib/API/OAuth2/` — ce répertoire doit être protégé par le serveur web (non accessible publiquement).
- Lève `ApiException` si OpenSSL ne peut pas générer les clés.
- La génération est automatique au premier appel : en production, il est préférable de pré-générer les clés et de les stocker dans un emplacement sécurisé hors du dossier web.
