# CalendarEventType.php

**Chemin :** `include/CalendarSync/domain/enums/CalendarEventType.php`
**Type :** PHP (enum)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Enum representant le type d'evenement calendrier (Meeting, etc.). Permet de distinguer les differents types d'enregistrements SuiteCRM synchronises avec des calendriers externes.

## Role technique

INCONNU — enum non lue entierement. Au minimum contient le cas `MEETING` (reference dans `CalendarAccountEvent`, ligne 61).

---

## Exports / Symboles principaux

| Cas | Signification |
|---|---|
| `MEETING` | Reunion SuiteCRM |

- **Consommateurs identifies :** `CalendarAccountEvent`, `CalendarEventSerializer`

---

## Points d'attention

- Fiche partielle — d'autres cas eventuels non confirmes.
