from chords_mqtt import config


def test_default_config():
    c = config.config
    assert isinstance(c, dict)
    assert 'mqtt' in c
    assert 'chords' in c
