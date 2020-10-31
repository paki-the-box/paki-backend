# paki-backend
Backend for paki the amazing box

# Remarks

## Modelling

### Locker
* Supported couriers ignored for the moment
* Maximum weight of whole locker ignored at the moment

### Order
* Supported couries ignored - assuming 'DEMO' for Hackathon
* timer ignored - optional properties for priority and returning durations

### Database
* created a database model - Notice: sqlite has to be created using 'python3 manage.py migrate' 

### API
* api/locker/find/lat/_xxx.yyy_/long/_xxx.yyy_/:
find all lockers around latitude (first _xxx.yyy_) and longitude latitude (second _xxx.yyy_)
* api/shipment/_string_/ _string_ is id of shipment
* api/shipment
* api/user/add application/json using [POST]  with firstname,lastname, email, latitude, longitude as parameter
* api/user/get/_email_ gets user information by email [GET]