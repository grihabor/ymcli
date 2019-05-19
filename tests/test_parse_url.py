import pytest
from ymcli.interfaces import parse_url, Song


@pytest.mark.parametrize("url, expected_count", [
    ("https://music.yandex.ru/album/4898647/track/38342740", 1),
    ("https://music.yandex.ru/album/4898647", 11)
])
def test_parse_url_track(url, expected_count):
    result = parse_url(url)
    assert len(result) == expected_count
    for song in result:
        assert isinstance(song, Song)
