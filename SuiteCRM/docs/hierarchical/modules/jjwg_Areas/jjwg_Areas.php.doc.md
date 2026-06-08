# jjwg_Areas.php

**Chemin :** `modules/jjwg_Areas/jjwg_Areas.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Modele principal du module "Zones geographiques" (jjwg_Areas). Represente une zone polygonale sur une carte Google Maps. Fournit les algorithmes de calcul geometrique (polygone, centroide, surface) et de detection de points dans un polygone.

**Type :** model

---

## Dependances cles
- `modules/jjwg_Areas/jjwg_Areas_sugar.php` — classe parente auto-generee (Basic + ACL)
- `modules/jjwg_Maps/jjwg_Maps.php` — chargement de la configuration globale `$GLOBALS['jjwg_config']`
- `BeanFactory` — creation du bean jjwg_Maps pour la configuration
- `LoggerManager` — journalisation des avertissements
- `$GLOBALS['jjwg_config']` — parametres de carte (lat/lng par defaut)

---

## Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `jjwg_Areas` | Classe | Bean principal du module zones |
| `configuration()` | Methode | Charge les settings depuis jjwg_Maps et `$GLOBALS['jjwg_config']` |
| `retrieve($id)` | Methode | Recupere un enregistrement et calcule polygon, surface, centroide |
| `define_polygon()` | Methode | Parse le champ `coordinates` (texte lng,lat,elv separes par espaces/retours) en tableau de points |
| `define_area()` | Methode | Calcule la surface du polygone via formule de Shoelace |
| `define_centroid()` | Methode | Calcule le centre de gravite (barycentre) du polygone |
| `define_area_loc()` | Methode | Retourne un tableau `['name','lat','lng']` base sur le centroide |
| `define_loc($marker)` | Methode | Normalise une location (objet ou tableau) en `['name','lat','lng']` |
| `is_marker_in_area($marker)` | Methode | Teste si un marqueur (objet ou tableau) est dans le polygone |
| `is_point_in_area($lng, $lat)` | Methode | Appelle `point_in_polygon()` pour un point donne |
| `point_in_polygon($point)` | Methode | Algorithme ray-casting : determine si un point est dans le polygone |
| `point_on_vertex($point, $vertices)` | Methode | Verifie si le point coincide avec un sommet |
| `point_string_to_coordinates($str)` | Methode | Parse une chaine "lng,lat,elv" en tableau `['x','y']` |
| `is_valid_lng($lng)` | Methode | Valide une longitude (-180..180) |
| `is_valid_lat($lat)` | Methode | Valide une latitude (-90..90) |

---

## Interactions
- **Appelle :** `jjwg_Maps_sugar` (via heritage), `BeanFactory::newBean('jjwg_Maps')`, `LoggerManager::getLogger()`
- **Appele par :** `jjwg_AreasController` (controller.php), `jjwg_AreasDashlet` (Dashlets), `jjwg_MapsController::getAreaDataCustom()` (recupere les zones liees a une carte)
- **Position dans le flux :** Bean racine du module jjwg_Areas ; instancie via `get_module_info('jjwg_Areas')` ou `BeanFactory`

---

## Notes
- Le format des coordonnees stocke en base est un texte libre `lng,lat,elv` separe par espaces ou retours a la ligne (ligne 88-91). Tout parsing se fait a l'execution.
- L'algorithme point-in-polygon est une implementation adaptee de assemblysys.com (ligne 309). Attention aux cas limites sur les bords horizontaux.
- La surface calculee est en unites de degres carres (non converties en km2).
- `optimistic_locking` active dans vardefs.php : les conflits d'edition concurrente sont detectes.
