def test_signup_success(client):
    # Arrange
    email = "newstudent@example.com"
    activity = "Chess Club"

    # Act
    resp = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert resp.status_code == 200
    body = resp.json()
    assert "Signed up" in body.get("message", "")

    # verify participant was added
    activities = client.get("/activities").json()
    assert email in activities[activity]["participants"]


def test_signup_duplicate_fails(client):
    # Arrange
    email = "michael@mergington.edu"  # already registered
    activity = "Chess Club"

    # Act
    resp = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert resp.status_code == 400


def test_signup_nonexistent_activity_fails(client):
    # Arrange
    email = "ghost@example.com"
    url = "/activities/NotAnActivity/signup"

    # Act
    resp = client.post(url, params={"email": email})

    # Assert
    assert resp.status_code == 404
