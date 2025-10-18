"""
Script Name : main.py
Description : Main application
Author      : @tonybnya
"""

from fastapi import FastAPI

ROOT_PATH: str = "/api/v1"
app: FastAPI = FastAPI()


@app.get("/")
def root() -> dict[str, str]:
    """
    Root endpoint
    """
    info: dict[str, str] = {
        "name": "Profile API",
        "version": "1.0.0",
        "description": "Dynamic profile endpoint",
    }
    return info
