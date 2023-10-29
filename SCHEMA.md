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

## Fine Print
* note 1: May or may not be used for OGF's iD editor.
