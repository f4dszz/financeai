"""
FinanceAI Platform - Test Configuration
Last Updated: 2024-12-14
"""

import pytest
from fastapi.testclient import TestClient

from backend.app.main import app


@pytest.fixture
def client():
    """Create a test client for FastAPI app."""
    return TestClient(app)


@pytest.fixture
def sample_pdf_path(tmp_path):
    """Create a temporary sample PDF path for testing."""
    pdf_file = tmp_path / "sample.pdf"
    pdf_file.write_bytes(b"%PDF-1.4 sample content")
    return pdf_file


@pytest.fixture
def sample_trade_data():
    """Sample trade data for anomaly detection testing."""
    return [
        {"timestamp": "2024-12-01T09:30:00", "symbol": "AAPL", "price": 150.25, "volume": 100, "side": "buy"},
        {"timestamp": "2024-12-01T09:30:01", "symbol": "AAPL", "price": 150.30, "volume": 200, "side": "sell"},
        {"timestamp": "2024-12-01T09:30:02", "symbol": "AAPL", "price": 150.28, "volume": 150, "side": "buy"},
    ]
