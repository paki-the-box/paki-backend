import uuid
from datetime import date
from enum import Enum
from typing import List
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pakibackend.settings")

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from fastapi.middleware.wsgi import WSGIMiddleware
from pakibackend.wsgi import get_wsgi_application



application = get_wsgi_application()

app = FastAPI()
app.mount("/admin", WSGIMiddleware(application))


class Contact(BaseModel):
    id: int
    name: str
    picture: str
    favorite_boxes: List[uuid.UUID]


class Box(BaseModel):
    id: uuid.UUID
    # Random "Name" of Station
    label: str
    address: str
    lat: float
    lon: float


class ShipmentSizes(str, Enum):
    S: 'S'
    M: 'M'
    L: 'L'
    XL: 'XL'


class DropoffStatus(str, Enum):
    ACCEPTED: 'accepted'
    DENIED: 'denied'


# Step 1
class SendRequest(BaseModel):
    """
    I want to drop you something off
    Sender -> Backend -> Receiver
    """
    id: uuid.UUID
    sender: EmailStr
    receiver: EmailStr
    box: uuid.UUID
    size: ShipmentSizes
    dropoff_date: date


# Step 2
class SendResponse(BaseModel):
    """
    I accept and will pick it up
    Receiver -> Backend
    """
    request: SendRequest
    status: DropoffStatus
    pickup_date: date


# Step 3
class ShipmentConfirmation(BaseModel):
    """
    You have a DEAL!
    Backend -> Sender
    Backend -> Receiver
    """
    sender: EmailStr
    receiver: EmailStr
    box: uuid.UUID
    size: ShipmentSizes
    dropoff_date: date
    pickup_date: date


@app.get("/boxes/all", response_model=List[Box])
async def get_all_boxes():
    return [
        Box(id=uuid.uuid4(), label="", address="", lat=1.0, lon=2.0),
        Box(id=uuid.uuid4(), label="2", address="", lat=1.0, lon=2.0),
    ]


@app.post("/boxes/new")
async def get_all_boxes(box: Box):
    print("Got a Box:")
    print(box)


@app.post("/requests/new")
async def new_request(send_request: SendRequest):
    pass


@app.get('/requests/{user_id}', response_model=List[SendRequest])
async def get_open_requests(user_id: uuid.UUID):
    """
    Fetch all open Requets to given user
    :param user_id:
    :return:
    """
    pass


@app.post("/responses/new")
async def new_response(send_response: SendResponse):
    pass


@app.post("/responses/{user_id}", response_model=List[SendResponse])
async def get_open_responses(user_id: uuid.UUID):
    pass


@app.post("/confirmations/{user_id}", response_model=List[ShipmentConfirmation])
async def get_open_confirmations(user_id: uuid.UUID):
    pass


@app.get("/contacts", response_model=List[Contact])
async def contacts():
    pass


@app.get("/shipment/{id}/delivery_code")
async def get_delivery_code(id: uuid.UUID):
    return "Hier dein Code"
