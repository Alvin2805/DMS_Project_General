import os
import importlib
from fastapi import APIRouter

populate_router = APIRouter()

path = os.getcwd()
prev_path = path + "//src/controllers"
router = os.listdir(prev_path)
for ch in router:
    name,ext = os.path.splitext(ch)
    if ext == ".py":
        from_module = importlib.import_module("src.controllers." + name)
        populate_router.include_router(from_module.router)  