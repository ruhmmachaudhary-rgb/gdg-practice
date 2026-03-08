from fastapi import FastAPI, Header, HTTPException

from git_day_practice.settings import settings

app = FastAPI(title=settings.APP_NAME)


# Health check
@app.get("/health")
def health():
    return {"status": "ok"}


# Config endpoint (non-secret)
@app.get("/config")
def get_config():
    return {"APP_NAME": settings.APP_NAME}


# Secure endpoint
@app.get("/secure-data")
def secure_data(x_api_key: str | None = Header(None)):
    if x_api_key != settings.API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return {"data": "This is secure data!"}
