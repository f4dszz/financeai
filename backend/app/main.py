"""
FinanceAI Platform - FastAPI Backend
Last Updated: 2024-12-14 23:15
"""

from contextlib import asynccontextmanager
from datetime import datetime, timezone
from typing import Any

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


# === Lifespan Event Handler ===
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan handler for startup/shutdown events."""
    # Startup
    print("FinanceAI Platform starting up...")
    print("API docs available at: http://localhost:8000/docs")
    yield
    # Shutdown
    print("FinanceAI Platform shutting down...")


# === App Configuration ===
app = FastAPI(
    title="FinanceAI Platform",
    description="Compliance/Risk AI Copilot for banking and securities",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

# === CORS Middleware ===
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# === Response Models ===
class HealthResponse(BaseModel):
    """Health check response model."""

    status: str
    timestamp: str
    version: str


class DisclaimerResponse(BaseModel):
    """Standard disclaimer for all AI outputs."""

    disclaimer: str = (
        "This content is AI-generated for reference only and does not "
        "constitute investment advice. Please consult licensed professionals "
        "for financial decisions."
    )
    disclaimer_zh: str = (
        "本内容由AI生成，仅供参考，不构成任何投资建议。"
        "金融决策请咨询持牌专业人士。"
    )


# === Health Check Endpoint ===
@app.get("/health", response_model=HealthResponse, tags=["System"])
async def health_check() -> HealthResponse:
    """
    Health check endpoint.

    Returns:
        HealthResponse: Current system status
    """
    return HealthResponse(
        status="ok",
        timestamp=datetime.now(timezone.utc).isoformat(),
        version="0.1.0",
    )


@app.get("/", tags=["System"])
async def root() -> dict[str, Any]:
    """Root endpoint with API information."""
    return {
        "name": "FinanceAI Platform",
        "version": "0.1.0",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/disclaimer", response_model=DisclaimerResponse, tags=["System"])
async def get_disclaimer() -> DisclaimerResponse:
    """Get standard disclaimer for AI outputs."""
    return DisclaimerResponse()


# === Placeholder API Routes ===
# These will be implemented in subsequent weeks


@app.get("/api/v1/status", tags=["API"])
async def api_status() -> dict[str, Any]:
    """API status endpoint."""
    return {
        "api_version": "v1",
        "modules": {
            "rag": "planned",      # Week 2
            "chart": "planned",    # Week 3
            "anomaly": "planned",  # Week 4
        },
        "disclaimer": DisclaimerResponse().disclaimer,
    }


# === Main Entry ===
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
