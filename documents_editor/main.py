from fastapi import FastAPI
from routes import file_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    prefix='/api/v1/'
)
app.include_router(file_router.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)
