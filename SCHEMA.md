# The Schema
Here is a detailed explanation of the schema, for adding new brands to
the Lemurian OGF index.

```json
        {
            "display_name": "Nalani's",
            "creator": "Lemuria",
            "origin_country": "Lutang",
            // "logo": "Nalani's doesn't have a logo yet.svg"
            "country_restrictions": {
                "allowed": ["*"],
                "ask": [],
                "no": []
            },
            "tags": {
                "amenity": "restaurant",
                "brand": "Nalani's",
                "cuisine": "asian",
                "name": "Nalani's"
            }
        }
```

* `display_name` - What you see in JOSM presets, or iD (note 1)
* `origin_country` - The country where the brand came from.
* `logo` - Filename of brand's logo on OGF wiki. Do not append `File:`.
* `creator` - The creator of the brand (Lemuria)
* `country_restrictions` - countries where you may or may not map a Nalani's.
  Use `*` to denote all countries.
  * `allowed` - If you are in these countries, you may map a Nalani's without
    Lemuria's permission.
  * `ask` - Countries that must have Lemuria's explicit permission to map a
    Nalani's.
  * `no` - Countries that may NOT map a Nalani's.
* `tags` - The tags to use. Key-value pairs.

## `country_restrictions`: Finer Details
Specific entries will always override wildcard entries.

When producing region-specific preset files for JOSM, the scripts will
not include a brand at all if the region is included as a `no` entry on
the brand.

### Examples
#### One country only
```json
{"country_restrictions": {
    "allowed": ["FSA"],
    "ask": [],
    "no": ["*"]
}}
```
This brand may only be mapped in the FSA. A Lutang preset file will not
include this brand.

#### Every country, but not one
```json
{"country_restrictions": {
    "allowed": ["*"],
    "ask": [],
    "no": ["Lutang"]
}}
```
This brand really hates Lutang, for some reason.

### Special "countries"
These "countries" are not at all countries, but are used for more fine-tuned
control over where brands may be mapped. These FSA regions are used for
entries in the database that are also part of the
FSA's [franchise index](https://wiki.opengeofiction.net/index.php/Collab:Federal_States/Franchises).

* FSA-NW: Northwest
* FSA-HL: Heartland
* FSA-WL: West Lakes
* FSA-AL: Alormen
* FSA-MD: Massodeyas
* FSA-CT: Central
* FSA-NE: Northeast
* FSA-MA: Mid-Ardentic
* FSA-SE: Southeast

## Fine Print
* note 1: May or may not be used for OGF's iD editor.
