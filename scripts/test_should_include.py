import pytest
from build_josm_presets import should_include

no_lutang = {"allowed": ["*"], "ask": [], "no": ["Lutang"]}
country_restrictions_test = [
    (no_lutang, "Lutang", False),
    (no_lutang, "FSA", True),
    ({"allowed": ["FSA"], "ask": [], "no": ["Lutang"]}, "FSA", True),
    ({"allowed": ["FSA"], "ask": [], "no": ["Lutang"]}, "Lutang", False),
    ({"allowed": ["FSA"], "ask": [], "no": ["Lutang"]}, "Izaland", False),

    # test FSA subregions
    ({"allowed": ["FSA:NW"], "ask": [], "no": ["*"]}, "FSA:NE", False),
    ({"allowed": ["FSA:NE"], "ask": [], "no": ["*"]}, "FSA", True),
    ({"allowed": ["FSA"], "ask": [], "no": ["*"]}, "FSA:NE", True)
]

@pytest.mark.parametrize('restrictions, country, expected', country_restrictions_test)
def test_restrictions(restrictions, country, expected):
    assert should_include(restrictions, country) == expected
