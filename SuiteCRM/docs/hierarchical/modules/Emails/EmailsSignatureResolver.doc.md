# Fichier : EmailsSignatureResolver.php

**Chemin :** `modules/Emails/EmailsSignatureResolver.php`
**Type :** PHP — Helper / Resolveur
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Resout la signature a utiliser pour un compte email en choisissant entre plusieurs representations possibles (cles `html`/`signature_html` pour HTML, `plain`/`signature` pour texte). Detecte les ambiguites et l'absence de signature.

## Role technique

Classe avec etat interne. Methode `setSignatureArray()` prend un tableau de signature, resout les deux variants et definit un flag `noDefaultAvailable` si aucune signature n'est trouvee. Retourne HTML et plaintext via accesseurs.

---

## Dependances

- Aucun import explicite
- **Utilise :** `LoggerManager`

## Exports / Symboles principaux

- `EmailsSignatureResolver` — classe
  - `setSignatureArray(array $signatureArray)` — initialise et resout, retourne les erreurs trouvees
  - `getHtml()` — retourne la signature HTML resolue
  - `getPlaintext()` — retourne la signature texte resolue
  - `isNoDefaultAvailable()` — true si aucune signature n'a ete trouvee
  - Constantes d'erreur : `ERR_HTML_AMBIGUOUS` (301), `ERR_HTML_NONE` (302), `ERR_PLAINTEXT_AMBIGUOUS` (303), `ERR_PLAINTEXT_NONE` (304)

- **Consommateurs :**
  - `modules/Emails/EmailsDataAddress.php`

## Relations cles

- **Appele par :** `EmailsDataAddress::getDataArray()`
- **Position :** resolution finale de la signature avant injection dans le payload compose

---

## Points d'attention

- Deux cles possibles par format (html/signature_html et plain/signature) : si les deux sont presentes et differentes, l'erreur AMBIGUOUS est loguee et la premiere cle (`html`/`plain`) est privilegiee.
