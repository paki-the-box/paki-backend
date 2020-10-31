import uuid
from datetime import date
from enum import Enum
from typing import List
import os

from starlette.middleware.cors import CORSMiddleware

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pakibackend.settings")

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from fastapi.middleware.wsgi import WSGIMiddleware
from pakibackend.wsgi import get_wsgi_application

from paki.models import HandoverTransaction,Contacts,FavBoxes
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]



application = get_wsgi_application()

app = FastAPI()
app.mount("/admin", WSGIMiddleware(application))

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Contact(BaseModel):
    id: int
    user_uuid: uuid.UUID
    email: EmailStr
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
    S= 'S'
    M= 'M'
    L= 'L'
    XL= 'XL'


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


requests = {}


@app.get("/contacts/", response_model=List[Contact])
def get_all_contacts():
    resulting_contacts = []
    contacts = Contacts.objects.all()
    for c in contacts:
        fav_boxes = []
        fav_boxes_qr = FavBoxes.objects.filter(contact_id=c.id)
        for box in fav_boxes_qr:
            fav_boxes.append(uuid.UUID("{%s}" % box.boxId))
        contact = Contact(id=c.id,
                          user_uuid=uuid.UUID("{%s}" % c.contactId),
                          email=c.email,
                          name=c.name,
                          picture=c.pictureLink,
                          favorite_boxes=fav_boxes)
        resulting_contacts.append(contact)

    return resulting_contacts


@app.post("/boxes/new")
async def get_all_boxes(box: Box):
    print("Got a Box:")
    print(box)


@app.post("/requests/new")
def new_request(send_request: SendRequest):
    transaction = HandoverTransaction()
    transaction.transactionId = send_request.id
    transaction.sending_contact= send_request.sender 
    transaction.receiving_contact= send_request.receiver
    transaction.box_id = send_request.box
    transaction.size = send_request.size
    transaction.transaction_state = 'C'
    transaction.dropoff_date = send_request.dropoff_date

    transaction.save()

    


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


# @app.get("/contacts", response_model=List[Contact])
# async def contacts():
#     pass


@app.get("/shipment/{id}/delivery_code")
async def get_delivery_code(id: uuid.UUID):
    return "Hier dein Code"
