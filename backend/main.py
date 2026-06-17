from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import os
from dotenv import load_dotenv

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("Application started")
    yield
    # Shutdown
    print("Application shutdown")

app = FastAPI(
    title="UTEHub API",
    description="Internal Social Network API",
    version="1.0.0",
    lifespan=lifespan
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "ok", "message": "UTEHub API is running"}

# Include routers (to be implemented)
# @app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
# @app.include_router(users.router, prefix="/api/users", tags=["users"])
# @app.include_router(posts.router, prefix="/api/posts", tags=["posts"])
# @app.include_router(comments.router, prefix="/api/comments", tags=["comments"])
# @app.include_router(notifications.router, prefix="/api/notifications", tags=["notifications"])
# @app.include_router(groups.router, prefix="/api/groups", tags=["groups"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )