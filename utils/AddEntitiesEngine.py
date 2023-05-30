import os
import importlib
from src.configs.database import engine

def addentities():
    moduleNamesOST = os.listdir("src/entities")
    for moduleName in moduleNamesOST:
        name, ext = os.path.splitext(moduleName)
        if (ext == ".py"):
            module = importlib.import_module("src.entities." + name)

def addentitiesengine():
    moduleNamesOST = os.listdir("src/entities")
    for moduleName in moduleNamesOST:
        name, ext = os.path.splitext(moduleName)
        if (ext == ".py"):
            module = importlib.import_module("src.entities." + name)
            module.Base.metadata.create_all(bind=engine)