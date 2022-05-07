# Flight Booking APIs Document

## Overview

The API documents of Flight Booking web application. This documentation will provide API of our flight booking service.

## Booking APIs

### Get all bookings

Get all the bookings

#### HTTP Request

`GET /bookings/`

##### Request headers

| Parameters   | Value            |
| :----------- | :--------------- |
| Content-Type | application/json |

##### URL parameters

|          | Parameters | Value | Description                                                   |
| :------- | :--------- | :---- | :------------------------------------------------------------ |
| Optional | sorted     | str   | If'true', The API will return all the booking sorted by date. |

Example request:

```
curl -v -X GET {prefix}/api/bookings/?sorted=true \
-H 'Content-Type: application/json' \
```

#### Response

Status code `200` and a list of booking objects.

```json
{
  "body": [
    {
      "id": 1,
      "flight_class": "Economy",
      "seat": "E-123",
      "user": {
        "id": 1,
        "first": "Thomas",
        "lastname": "Merchant",
        "age": 20
      },
      "current": "Bangkok",
      "destination": "Chiang mai",
      "boarding_date": "06/05/2022 09:00:00"
    },
    {
      "id": 2,
      "flight_class": "Economy",
      "seat": "E-124",
      "user": {
        "id": 2,
        "first": "Janis",
        "lastname": "Merchant",
        "age": 20
      },
      "current": "Bangkok",
      "destination": "Chiang mai",
      "boarding_date": "06/05/2022 09:00:00"
    }
  ]
}
```

### Get booking by booking ID

Get a booking with the specified ID.

#### HTTP request

`GET /bookings/{booking_id}`

##### Request headers

| Parameters   | Value            |
| :----------- | :--------------- |
| Content-Type | application/json |

##### Path parameters

| Parameters | Description       |
| :--------- | :---------------- |
| booking_id | The ID of booking |

Example request:

```bash
curl -v -X GET {prefix}/api/bookings/{booking_id}/ \
-H 'Content-Type: application/json' \
```

#### Response

Status code `200` and a booking objects.

```json
{
  "id": 1,
  "flight_class": "Economy",
  "seat": "E-123",
  "user": {
    "id": 1,
    "first": "Thomas",
    "lastname": "Merchant",
    "age": 20
  },
  "current": "Bangkok",
  "destination": "Chiang mai",
  "boarding_date": "06/05/2022 09:00:00"
}
```

#### Error

Returns a `40x` HTTP status code and an error response.

Example error response:

```json
{
  "message": "Booking ID not found"
}
```

### Create Booking

#### Permission

- Anyone that have the account in our system.

#### HTTP request

`POST /api/bookings/`

##### Request headers

| Parameters    | Value             |
| :------------ | :---------------- |
| Content-Type  | application/json  |
| Authorization | Bearer {ID Token} |

##### Request body

| Parameters    | Type     | Description                                              |
| :------------ | :------- | :------------------------------------------------------- |
| flight-class  | str      | Class of the flight (eg. First-class, Economy, Business) |
| seat          | str      | Seat number                                              |
| current       | str      | source city/country                                      |
| destination   | str      | Destination city/country                                 |
| boarding_date | datetime | On boarding date and time                                |

Example request:

```bash
  curl -v -X POST {prefix}/api/bookings/ \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer {ID Token}' \
  -d '{
      "flight-class": "First-class",
      "seat": "F-100",
      "current": "Bangkok",
      "destination": "Chiang mai",
      "boarding_date": "07/05/2022 09:00:00"
  }'
```

### Update Booking

#### Permission

- Must be an admin.

#### HTTP request

`PATCH /api/bookings/{booking_id}`

##### Request headers

| Parameters    | Value             |
| :------------ | :---------------- |
| Content-Type  | application/json  |
| Authorization | Bearer {ID Token} |

##### Path parameters

| Parameters | Description       |
| :--------- | :---------------- |
| booking_id | The ID of booking |

##### Request body

|          | Parameters    | Type     | Description                                              |
| :------- | :------------ | :------- | :------------------------------------------------------- |
| Optional | flight-class  | str      | Class of the flight (eg. First-class, Economy, Business) |
| Optional | seat          | str      | Seat number                                              |
| Optional | current       | str      | source city/country                                      |
| Optional | destination   | str      | Destination city/country                                 |
| Optional | boarding_date | datetime | On boarding date and time                                |

Example request:

```bash
  curl -v -X POST {prefix}/api/bookings/1/ \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer {ID Token}' \
  -d '{
      "boarding_date": "07/05/2022 15:00:00"
  }'
```

#### Error

Returns a `40x` HTTP status code and an error response.

Example error response:

```json
{
  "message": "Booking ID not found"
}
```
