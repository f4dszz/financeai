# FinanceAI Platform - Frontend Dockerfile
# Last Updated: 2024-12-14

FROM python:3.10-slim

WORKDIR /app

# Install streamlit and dependencies
RUN pip install --no-cache-dir streamlit httpx

# Copy application code
COPY . .

# Expose port
EXPOSE 8501

# Run Streamlit
CMD ["streamlit", "run", "Home.py", "--server.port", "8501", "--server.address", "0.0.0.0"]
