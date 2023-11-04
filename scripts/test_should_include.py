import pytest
from build_josm_presets import should_include

no_lutang = {"allowed": ["*"], "ask": [], "no": ["Lutang"]}
country_restrictions_test = [
    (no_lutang, "Lutang", False),
    (no_lutang, "FSA", True),
    ({"allowed": ["FSA"], "ask": [], "no": ["Lutang"]}, "FSA", True),
    ({"allowed": ["FSA"], "ask": [], "no": ["Lutang"]}, "Lutang", False),
    ({"allowed": ["FSA"], "ask": [], "no": ["Lutang"]}, "Izaland", False),
    ({"allowed": ["FSA:NW"], "ask": [], "no": ["*"]}, "FSA:NE", False)
]

@pytest.mark.parametrize('restrictions, country, expected', country_restrictions_test)
def test_restrictions(restrictions, country, expected):
    assert should_include(restrictions, country) == expected
