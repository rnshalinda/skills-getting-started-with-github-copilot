def test_get_activities_returns_dict(client):
    # Arrange
    url = "/activities"

    # Act
    resp = client.get(url)

    # Assert
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    # spot-check a known activity
    assert "Chess Club" in data
