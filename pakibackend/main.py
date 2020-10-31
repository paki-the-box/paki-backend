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
from fastapi import FastAPI, HTTPException


from paki.services.shipment import ShipmentService
from paki.services.lockerlocation import LockerLocationService
from paki.services.errors import ShipmentCreationFailedException

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
    id: uuid.UUID
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
    ACCEPTED = 'accepted'
    DENIED = 'denied'


# Step 1
class SendRequest(BaseModel):
    """
    I want to drop you something off
    Sender -> Backend -> Receiver
    """
    id: uuid.UUID
    sender: uuid.UUID
    receiver: uuid.UUID
    box: uuid.UUID
    size: ShipmentSizes
    dropoff_date: date

# Step 2
class SendResponse(BaseModel):
    """
    I accept and will pick it up
    Receiver -> Backend
    """
    id: uuid.UUID
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


requests = []


@app.get("/contacts/", response_model=List[Contact])
def get_all_contacts():
    resulting_contacts = []
    contacts = Contacts.objects.all()
    for c in contacts:
        fav_boxes = []
        fav_boxes_qr = FavBoxes.objects.filter(contact_id=c.id)
        for box in fav_boxes_qr:
            fav_boxes.append(uuid.UUID("{%s}" % box.boxId))
        contact = Contact(id=uuid.UUID("{%s}" % c.contactId),
                          email=c.email,
                          name=c.name,
                          picture=c.pictureLink,
                          favorite_boxes=fav_boxes)
        resulting_contacts.append(contact)

    return resulting_contacts


@app.get("/boxes/all", response_model=List[Box])
async def get_all_boxes():
    boxes = LockerLocationService.get_all_lockers()

    box_models = []
    for box in boxes:
        box_model = Box(id = box.location_id,
        label = f"Irgendwo in {box.address.publicName}",
        address =  box.address.publicName,
        lat = box.geolocation.latitude, 
        lon = box.geolocation.longitude)
        box_models.append(box_model)

    return box_models

    # return [
    #     Box(id='a8f5e8ca-b55d-4f9e-9a98-145b62ad37b1', label="Die Box in Kirchheim", address="Irgendwo in Kirchheim",
    #         lat=48.6355632, lon=9.4052465),
    #     Box(id='2bc06d25-067c-493f-a32a-79bcc2ba88ff', label="Die Box in Fulda", address="Irgendwo in Fulda", lat=50.4296862, lon=9.5423249),
    # ]


@app.post("/requests/new")
def new_request(send_request: SendRequest):
    sdr = Contacts.objects.get(contactId__exact = send_request.sender)
    rcvr = Contacts.objects.get(contactId__exact = send_request.receiver)

    transaction = HandoverTransaction()
    transaction.transactionId = send_request.id
    transaction.sending_contact= sdr 
    transaction.receiving_contact= rcvr
    transaction.box_id = send_request.box
    transaction.size = send_request.size
    transaction.transaction_state = 'C'
    transaction.dropoff_date = send_request.dropoff_date

    transaction.save()


@app.post("/requests/sent/count/{user_id}", response_model=int)
async def open_sent_requests_for_user(user_id: uuid.UUID):
    """
    Get Number of Open Sent Requetsts that wait for confirmation
    :param user_id:
    :return:
    """
    return len(requests)


@app.get('/requests/{user_id}', response_model=List[SendRequest])
async def get_open_requests(user_id: uuid.UUID):
    """
    Fetch all open Requets to given user
    :param user_id:
    :return:
    """
    print(user_id)
    print(user_id.hex)
    response_collection = []
    currentUser = Contacts.objects.get(contactId=user_id.hex)
    print(currentUser)
    allOpenRequests=HandoverTransaction.objects.filter(sending_contact=currentUser.id) #,transaction_state__exact="C")
    print(allOpenRequests)
    # for oreq in allOpenRequests:
    #     pending=SendRequest(
    #     id=oreq.transactionId,
    #     sender=oreq.sending_contact.id,
    #     receiver=oreq.receiving_contact.id,
    #     box= oreq.box_id,
    #     size=oreq.size,
    #     dropoff_date=oreq.dropoff_date
    #     )
    #     response_collection.append(pending)

    return response_collection


@app.post("/responses/new", status_code=204)
def new_response(send_response: SendResponse):
    transaction = HandoverTransaction.objects.get(transactionId = send_response.id)

    if send_response.status == DropoffStatus.ACCEPTED:
        # Create a shipment in the API
        try:
            ShipmentService.create_shipment(transaction)
        except ShipmentCreationFailedException as creationFailed:
            raise HTTPException(status_code=400, detail="Failed to create shipment in Backend")
        # If suceessful
        transaction.transaction_state = 'A'
        transaction.accepted_by_receiver = True
    else:
        # Declined -> Notify the user
        transaction.transaction_state = 'D'
        transaction.accepted_by_receiver = False

    transaction.save()


@app.get("/responses/{user_id}", status_code=200 ,response_model=List[SendResponse])
def get_open_responses(user_id: uuid.UUID):
    pass

    # transactions_waiting_on_confirmation = HandoverTransaction.objects.filter(receiving_contact__exact=user_id).filter(accepted_by_receiver__isnull=True)

    # response_collection = []
    # for transaction in transactions_waiting_on_confirmation:
    #     pending = PendingConfirmations(id = transaction.transactionId, sender = transaction.sending_contact, dropoff_date = transaction.dropoff_date)
    #     response_collection.append(pending)

    # return response_collection


#TODO: Change to get
@app.post("/confirmations/{user_id}", response_model=List[ShipmentConfirmation])
async def get_open_confirmations(user_id: uuid.UUID):
    pass

@app.get("/shipment/{id}/delivery_code")
async def get_delivery_code(id: uuid.UUID):
    return "Hier dein Code"
