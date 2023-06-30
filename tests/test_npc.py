from non_panicked_character.npc import (
    generate_alignment,
    generate_background,
    generate_class,
    generate_name,
    generate_race
)

def test_generate_alignment_returns_a_alignment():
    response = generate_alignment()
    assert response is not None
    assert isinstance(response, str)

def test_generate_background_returns_a_background():
    response = generate_background()
    assert response is not None
    assert isinstance(response, str)

def test_generate_class_returns_a_class():
    response = generate_class()
    assert response is not None
    assert isinstance(response, str)

def test_generate_name_returns_a_name():
    response = generate_name()
    assert response is not None
    assert isinstance(response, str)

def test_generate_race_returns_a_race():
    response = generate_race()
    assert response is not None
    assert isinstance(response, str)
