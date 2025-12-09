FROM python:3.11-slim

WORKDIR /app

# Install uv globally
RUN pip install uv

# Copy project files
COPY . .

# Install dependencies via uv
RUN uv pip install --system -r requirements.txt

# Expose port for Azure
EXPOSE 8000

# Start FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]