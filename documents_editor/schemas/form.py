from os import name
from turtle import position
from pydantic import BaseModel


class OrderForm(BaseModel):
    
    position: str
    rank: str
    name: str
