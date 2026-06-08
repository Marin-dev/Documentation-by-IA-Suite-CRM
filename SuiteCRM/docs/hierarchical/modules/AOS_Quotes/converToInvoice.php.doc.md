# Fichier converToInvoice.php — AOS_Quotes

**Chemin :** `modules/AOS_Quotes/converToInvoice.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel
Script de conversion d'un devis (AOS_Quotes) en facture (AOS_Invoices). Crée un nouvel enregistrement AOS_Invoices en copiant les données du devis (lignes de produits, adresses, devise, etc.) et redirige vers la facture créée.

## Type
autre (script de conversion)

## Dépendances clés
- `AOS_Quotes`, `AOS_Invoices`, `AOS_Line_Item_Groups`, `AOS_Products_Quotes`

## Notes
Invoqué depuis la DetailView de AOS_Quotes (bouton "Convert to Invoice"). Crée un lien entre le devis et la facture via une relation. Le nom contient une faute de frappe ("conver" au lieu de "convert") — à surveiller.
