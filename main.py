"""
Script Name : main.py
Description : Main application
Author      : @tonybnya
"""

from fastapi import FastAPI
from pydantic import BaseModel

app: FastAPI = FastAPI()


class UserInfo(BaseModel):
    """
    Definition of the nested user object
    """

    email: str
    name: str
    stack: str


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
