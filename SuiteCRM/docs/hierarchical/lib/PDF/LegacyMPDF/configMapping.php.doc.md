# configMapping.php (LegacyMPDF)

**Chemin :** `lib/PDF/LegacyMPDF/configMapping.php`
**Configure :** Moteur mPDF legacy
**Derniere mise a jour doc :** 2026-05-30

---

## Ce que ce fichier configure
Fichier de configuration PHP inclus dynamiquement par `LegacyMPDFEngine::configurePDF()`. Mappe les options de la requete vers les parametres mPDF. Retourne un tableau `$configOptions` avec les valeurs de mise en page.

## Parametres cles
| Parametre | Valeur par defaut | Effet |
|---|---|---|
| `mode` | `''` | Mode de langue/codage mPDF |
| `page_size` | `'A4'` | Taille de page |
| `default_font_size` | `11` | Taille de fonte (pt) |
| `default_font` | `'DejaVuSansCondensed'` | Fonte par defaut |
| `margin_left/right` | `15` | Marges laterales (mm) |
| `margin_top/bottom` | `16` | Marges verticales (mm) |
| `margin_header/footer` | `9` | Marges en-tete/pied (mm) |
| `orientation` | `'P'` | Portrait (`P`) ou Paysage (`L`) |
| `unit` | `'mm'` | Unite de mesure |

## Impacte par / impacte
- Consomme par : `lib/PDF/LegacyMPDF/LegacyMPDFEngine.php` (ligne 148, `include self::$configMapperFile`)
- Variable `$options` injectee depuis `configurePDF(array $options)`

## Points d'attention
- Ce fichier utilise `$options` qui doit etre defini dans le scope avant l'inclusion (passage par `include`).
