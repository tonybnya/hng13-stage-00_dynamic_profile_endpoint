"""
Script Name : main.py
Description : Main application
Author      : @tonybnya
"""

from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app: FastAPI = FastAPI()


class UserInfo(BaseModel):
    """
    Definition of the nested user object
    """

    email: EmailStr
    name: str
    stack: str


class ProfileResponse(BaseModel):
    """
    Definition of the response model
    """

    status: str
    user: UserInfo
    timestamp: datetime
    fact: str


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
