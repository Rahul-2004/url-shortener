# A single file for all tests

def test_health_check(client):
    """Test that the health check endpoint is available."""
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json == {"status": "ok"}

def test_full_workflow(client):
    """Tests the entire E2E flow: shorten -> redirect -> stats."""
    # 1. Shorten
    resp_shorten = client.post("/api/shorten", json={"url": "https://www.google.com"})
    assert resp_shorten.status_code == 201
    data = resp_shorten.get_json()
    code = data["short_code"]
    assert len(code) == 6

    # 2. Redirect
    resp_redirect = client.get(f"/{code}", follow_redirects=False)
    assert resp_redirect.status_code == 302
    assert resp_redirect.headers["Location"] == "https://www.google.com"

    # 3. Stats
    resp_stats = client.get(f"/api/stats/{code}")
    assert resp_stats.status_code == 200
    stats_data = resp_stats.get_json()
    assert stats_data["url"] == "https://www.google.com"
    assert stats_data["clicks"] == 1

def test_click_tracking(client):
    """Tests that clicks are incremented correctly."""
    resp = client.post("/api/shorten", json={"url": "https://www.apple.com"})
    code = resp.get_json()["short_code"]

    # Visit the link three times
    client.get(f"/{code}")
    client.get(f"/{code}")
    client.get(f"/{code}")

    stats_resp = client.get(f"/api/stats/{code}")
    assert stats_resp.get_json()["clicks"] == 3

def test_404_on_nonexistent_code(client):
    """Tests that both redirect and stats endpoints return 404 for a bad code."""
    resp_redirect = client.get("/notreal")
    assert resp_redirect.status_code == 404

    resp_stats = client.get("/api/stats/notreal")
    assert resp_stats.status_code == 404

def test_400_on_invalid_url(client):
    """Tests for a 400 error when the provided URL is invalid."""
    resp = client.post("/api/shorten", json={"url": "not-a-valid-url"})
    assert resp.status_code == 400
    assert "error" in resp.get_json()

def test_400_on_missing_body_field(client):
    """Tests for a 400 error when the 'url' field is missing from the body."""
    resp = client.post("/api/shorten", json={"wrong_field": "https://example.com"})
    assert resp.status_code == 400
    assert "missing 'url' field" in resp.get_json()["error"]
