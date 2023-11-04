import xml.etree.cElementTree as ET
import json
import glob
import os

PRESET_GROUPS = json.load(open("../data/preset_groups.json"))["preset_groups"]
DATA_DIR = "../data"

def make_josm_presets(preset):
    root = ET.Element(
        "presets",
        xmlns="http://josm.openstreetmap.de/tagging-preset-1.0",
        author="Lemuria",
        version="1.0",
        shortdescription="Lemurian OpenGeofiction Presets",
        description="OGF brands",
    )
    ogf_root = ET.SubElement(
        ET.SubElement(root, "group", name="OGF"), "group", name=preset.get("name")
    )
    data = amalgamate_jsons()
    for first_level in data.keys():
        first_level_xml = ET.SubElement(ogf_root, "group", name=first_level)
        for second_level in data[first_level].keys():
            second_level_xml = ET.SubElement(
                first_level_xml, "group", name=second_level
            )
            for brand in data[first_level][second_level]:
                allowed = [
                    should_include(brand.get('country_restrictions'), country)
                    for country in preset.get('countries')]
                if True in allowed or preset.get('name') == 'all':
                    make_preset_xml(brand, second_level_xml)
    tree = ET.ElementTree(root)
    if 'output' not in os.listdir('.'):
        os.mkdir('output')
    tree.write(f"output/ogf_presets.{preset.get('name')}.dist.xml")


def make_all_josm_presets():
    for preset in PRESET_GROUPS:
        make_josm_presets(preset)


def make_preset_xml(brand: dict, parent_xml):
    brand_xml = ET.SubElement(parent_xml, "item", name=brand.get("display_name"),
        type="node,closedway,multipolygon",
        preset_name_label="true",
    )
    for key in brand.get('tags').keys():
        ET.SubElement(brand_xml, "key", key=key, value=brand.get('tags').get(key))


def amalgamate_jsons():
    data = {}
    for item in glob.glob("../data/brands/*"):
        top_level_tag = item.split("/")[-1]
        data[top_level_tag] = {}
        for second_level_item in glob.glob(f"../data/brands/{top_level_tag}/*.json"):
            json_name = second_level_item.split("/")[-1].split(".")[0]
            data[top_level_tag][json_name] = json.loads(
                open(second_level_item).read()
            ).get("items")
    return data


def should_include(restrictions, country):
    """
    Determine if a preset should be included for a country by checking
    the country restrictions.
    """
    allowed = restrictions.get("allowed")
    no = restrictions.get("no")
    # Assume that an empty "no" field means "*".
    for list in [no, allowed]:
        if len(list) == 0:
            list.append('*')

    if country in no:
        result = False
    elif country in allowed:
        result = True
    elif allowed == ['*']:
        result = True
    else:
        result = False

    return result


def main():
    make_all_josm_presets()


if __name__ == "__main__":
    main()
