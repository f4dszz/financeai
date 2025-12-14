"""
FinanceAI Platform - API Tests
Last Updated: 2024-12-14
"""


class TestHealthEndpoint:
    """Test /health endpoint."""

    def test_health_check_returns_ok(self, client):
        """Test that health check returns status ok."""
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"
        assert "timestamp" in data
        assert "version" in data

    def test_health_check_version(self, client):
        """Test that health check returns correct version."""
        response = client.get("/health")
        data = response.json()
        assert data["version"] == "0.1.0"
