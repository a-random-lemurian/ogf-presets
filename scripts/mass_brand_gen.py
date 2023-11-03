"""
Quickly output JSON for multiple brands with similar tagging
"""
import json

data = json.loads(open("mass_brand_gen.json").read())

print(json.dumps([{
            "display_name": brand,
            "country_restrictions": data['country_restrictions'],
            "tags": data['tags']|{"brand":brand,"name":brand}
        }
        for brand in data['brands']
]))

