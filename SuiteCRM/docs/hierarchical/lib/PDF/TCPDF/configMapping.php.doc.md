# configMapping.php (TCPDF)

**Chemin :** `lib/PDF/TCPDF/configMapping.php`
**Configure :** Moteur TCPDF
**Derniere mise a jour doc :** 2026-05-30

---

## Ce que ce fichier configure
Fichier de configuration PHP inclus dynamiquement par `TCPDFEngine::configurePDF()`. Mappe les options transmises vers les parametres TCPDF. Similaire a `LegacyMPDF/configMapping.php` mais inclut `image_scale`.

## Parametres cles
| Parametre | Valeur par defaut | Effet |
|---|---|---|
| `page_size` | `'A4'` | Taille de page |
| `orientation` | `'P'` | Portrait / Paysage |
| `unit` | `'mm'` | Unite |
| `default_font_size` | `11` | Taille fonte (pt) |
| `default_font` | `'DejaVuSansCondensed'` | Police |
| `margin_left/right` | `15` | Marges (mm) |
| `margin_top/bottom` | `16` | Marges (mm) |
| `margin_header/footer` | `9` | Marges (mm) |
| `image_scale` | `1.33` | Facteur d'echelle image |

## Impacte par / impacte
- Consomme par : `lib/PDF/TCPDF/TCPDFEngine.php` (ligne 171)
- Variable `$options` injectee depuis `configurePDF(array $options)`

## Points d'attention
- `image_scale` est specifique a TCPDF (absent du mapping LegacyMPDF).
