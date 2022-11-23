from varst.utils.substitution import substitution_text


def test_create_substitution():
    assert substitution_text("key", "value") == """.. |key| replace:: value"""
