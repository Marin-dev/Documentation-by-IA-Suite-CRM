# View.php (Search/ElasticSearch)

**Chemin :** `modules/Administration/Search/ElasticSearch/View.php`
**Namespace :** `SuiteCRM\Modules\Administration\Search\ElasticSearch`
**Type :** PHP (View MVC)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Vue de la page de configuration ElasticSearch. Assigne la config ES specifique au template Smarty.

## Role technique
Etend `MVC\View`. `preDisplay()` : charge `$sugar_config['search']['ElasticSearch']` et assigne a Smarty sous `config`. `display()` : heritee de `MVC\View`.

---

## Interactions
- **Instanciee par :** `ElasticSearch\Controller`
- **Template :** `modules/Administration/Search/ElasticSearch/view.tpl`
