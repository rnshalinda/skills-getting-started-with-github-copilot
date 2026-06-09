def test_root_redirects_to_static(client):
    # Arrange
    url = "/"

    # Act
    resp = client.get(url, follow_redirects=False)

    # Assert
    assert resp.status_code in (301, 302, 307, 308)
    assert resp.headers.get("location") == "/static/index.html"
