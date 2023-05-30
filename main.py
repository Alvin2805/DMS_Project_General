from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import src.utils.AddControllers #manual function that created using basic libraries in python
from src.utils.AddEntitiesEngine import addentities, addentitiesengine #manual function that created entities and base engine


app = FastAPI(title="DMS Microservices - General",docs_url="/")

addentities()

# utilized for incoming request from Front End / API Gateway
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#add the entities engine automatically
addentitiesengine()

#including the router
app.include_router(src.utils.AddControllers.populate_router)