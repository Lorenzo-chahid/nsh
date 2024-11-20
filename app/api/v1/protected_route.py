from fastapi import FastAPI, Depends
from app.api.v1.dependencies import get_current_user

app = FastAPI()

# Route protégée par JWT
@app.get("/api/v1/protected-route")
def protected_route(current_user: str = Depends(get_current_user)):
    return {"message": "This is a protected route", "user": current_user}
