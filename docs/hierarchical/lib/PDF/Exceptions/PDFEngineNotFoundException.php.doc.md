# PDFEngineNotFoundException.php

## Rôle
Exception spécialisée levée lorsqu'un moteur PDF demandé est introuvable (classe inexistante, fichier absent, ou classe non sous-classe de `PDFEngine`).

## Responsabilités
- Signaler qu'un moteur PDF nommé n'a pas pu être résolu par `PDFWrapper`
- Permettre un catch ciblé distinct des autres erreurs PDF

## Dépendances internes
- `PDFException` (`lib/PDF/Exceptions/PDFException.php`) — classe parente

## Exports / Points d'entrée
- `PDFEngineNotFoundException` (classe) — namespace `SuiteCRM\PDF\Exceptions`

## Notes techniques
- Classe vide, comportement entièrement hérité de `PDFException` / `RuntimeException`
- Levée par `PDFWrapper::fetchEngine()` en cas de moteur non trouvé (lignes 157, 165, 173)
