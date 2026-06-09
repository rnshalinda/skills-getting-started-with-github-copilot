def test_unregister_success(client):
    # Arrange
    activity = "Basketball Team"
    email = "alex@mergington.edu"

    # ensure alex is present initially
    data_before = client.get("/activities").json()
    assert email in data_before[activity]["participants"]

    # Act
    resp = client.delete(f"/activities/{activity}/participants", params={"email": email})

    # Assert
    assert resp.status_code == 200
    body = resp.json()
    assert "Unregistered" in body.get("message", "")

    data_after = client.get("/activities").json()
    assert email not in data_after[activity]["participants"]


def test_unregister_not_registered_fails(client):
    # Arrange
    activity = "Chess Club"
    email = "not-registered@example.com"

    # Act
    resp = client.delete(f"/activities/{activity}/participants", params={"email": email})

    # Assert
    assert resp.status_code == 400


def test_unregister_nonexistent_activity_fails(client):
    # Arrange
    url = "/activities/NoSuchActivity/participants"

    # Act
    resp = client.delete(url, params={"email": "a@b.com"})

    # Assert
    assert resp.status_code == 404
