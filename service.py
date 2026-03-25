from sqlalchemy.orm import Session, aliased
from database import SessionLocal
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException, status
import models, schemas
import boto3
import jwt
from datetime import datetime
import requests
import math
import random
import asyncio
from pathlib import Path


def convert_to_datetime(date_string):
    if date_string is None:
        return datetime.now()
    if not date_string.strip():
        return datetime.now()
    if "T" in date_string:
        try:
            return datetime.fromisoformat(date_string.replace("Z", "+00:00"))
        except ValueError:
            date_part = date_string.split("T")[0]
            try:
                return datetime.strptime(date_part, "%Y-%m-%d")
            except ValueError:
                return datetime.now()
    else:
        # Try to determine format based on first segment
        parts = date_string.split("-")
        if len(parts[0]) == 4:
            # Likely YYYY-MM-DD format
            try:
                return datetime.strptime(date_string, "%Y-%m-%d")
            except ValueError:
                return datetime.now()

        # Try DD-MM-YYYY format
        try:
            return datetime.strptime(date_string, "%d-%m-%Y")
        except ValueError:
            return datetime.now()

        # Fallback: try YYYY-MM-DD if not already tried
        if len(parts[0]) != 4:
            try:
                return datetime.strptime(date_string, "%Y-%m-%d")
            except ValueError:
                return datetime.now()

        return datetime.now()


async def get_ground_stations(request: Request, db: Session):

    query = db.query(models.GroundStations)

    ground_stations_all = query.all()
    ground_stations_all = (
        [new_data.to_dict() for new_data in ground_stations_all]
        if ground_stations_all
        else ground_stations_all
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"ground_stations_all": ground_stations_all},
    }
    return res


async def get_ground_stations_id(request: Request, db: Session, id: Union[int, float]):

    query = db.query(models.GroundStations)
    query = query.filter(and_(models.GroundStations.id == id))

    ground_stations_one = query.first()

    ground_stations_one = (
        (
            ground_stations_one.to_dict()
            if hasattr(ground_stations_one, "to_dict")
            else vars(ground_stations_one)
        )
        if ground_stations_one
        else ground_stations_one
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"ground_stations_one": ground_stations_one},
    }
    return res


async def post_ground_stations(
    request: Request,
    db: Session,
    raw_data: schemas.PostGroundStations,
):
    user_id: Union[int, float] = raw_data.user_id
    name: str = raw_data.name
    latitude: float = raw_data.latitude
    longitude: float = raw_data.longitude
    created_at_dt: str = convert_to_datetime(raw_data.created_at_dt)

    record_to_be_added = {
        "name": name,
        "user_id": user_id,
        "latitude": latitude,
        "longitude": longitude,
        "created_at_dt": created_at_dt,
    }
    new_ground_stations = models.GroundStations(**record_to_be_added)
    db.add(new_ground_stations)
    db.commit()
    # db.refresh(new_ground_stations)
    ground_stations_inserted_record = new_ground_stations.to_dict()

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"ground_stations_inserted_record": ground_stations_inserted_record},
    }
    return res


async def put_ground_stations_id(
    request: Request,
    db: Session,
    raw_data: schemas.PutGroundStationsId,
):
    id: Union[int, float] = raw_data.id
    user_id: Union[int, float] = raw_data.user_id
    name: str = raw_data.name
    latitude: float = raw_data.latitude
    longitude: float = raw_data.longitude
    created_at_dt: str = convert_to_datetime(raw_data.created_at_dt)

    query = db.query(models.GroundStations)
    query = query.filter(and_(models.GroundStations.id == id))
    ground_stations_edited_record = query.first()

    if ground_stations_edited_record:
        for key, value in {
            "id": id,
            "name": name,
            "user_id": user_id,
            "latitude": latitude,
            "longitude": longitude,
            "created_at_dt": created_at_dt,
        }.items():
            setattr(ground_stations_edited_record, key, value)

        db.commit()

        # db.refresh(ground_stations_edited_record)

        ground_stations_edited_record = (
            ground_stations_edited_record.to_dict()
            if hasattr(ground_stations_edited_record, "to_dict")
            else vars(ground_stations_edited_record)
        )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"ground_stations_edited_record": ground_stations_edited_record},
    }
    return res


async def delete_ground_stations_id(
    request: Request, db: Session, id: Union[int, float]
):

    query = db.query(models.GroundStations)
    query = query.filter(and_(models.GroundStations.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        ground_stations_deleted = record_to_delete.to_dict()
    else:
        ground_stations_deleted = record_to_delete

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"ground_stations_deleted": ground_stations_deleted},
    }
    return res


async def get_satellites(request: Request, db: Session):

    query = db.query(models.Satellites)

    satellites_all = query.all()
    satellites_all = (
        [new_data.to_dict() for new_data in satellites_all]
        if satellites_all
        else satellites_all
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"satellites_all": satellites_all},
    }
    return res


async def get_satellites_id(request: Request, db: Session, id: Union[int, float]):

    query = db.query(models.Satellites)
    query = query.filter(and_(models.Satellites.id == id))

    satellites_one = query.first()

    satellites_one = (
        (
            satellites_one.to_dict()
            if hasattr(satellites_one, "to_dict")
            else vars(satellites_one)
        )
        if satellites_one
        else satellites_one
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"satellites_one": satellites_one},
    }
    return res


async def post_satellites(
    request: Request,
    db: Session,
    raw_data: schemas.PostSatellites,
):
    norad_id: Union[int, float] = raw_data.norad_id
    name: str = raw_data.name
    tle_line1: str = raw_data.tle_line1
    tle_line2: str = raw_data.tle_line2
    created_at_dt: str = convert_to_datetime(raw_data.created_at_dt)

    record_to_be_added = {
        "name": name,
        "norad_id": norad_id,
        "tle_line1": tle_line1,
        "tle_line2": tle_line2,
        "created_at_dt": created_at_dt,
    }
    new_satellites = models.Satellites(**record_to_be_added)
    db.add(new_satellites)
    db.commit()
    # db.refresh(new_satellites)
    satellites_inserted_record = new_satellites.to_dict()

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"satellites_inserted_record": satellites_inserted_record},
    }
    return res


async def put_satellites_id(
    request: Request,
    db: Session,
    raw_data: schemas.PutSatellitesId,
):
    id: Union[int, float] = raw_data.id
    norad_id: Union[int, float] = raw_data.norad_id
    name: str = raw_data.name
    tle_line1: str = raw_data.tle_line1
    tle_line2: str = raw_data.tle_line2
    created_at_dt: str = convert_to_datetime(raw_data.created_at_dt)

    query = db.query(models.Satellites)
    query = query.filter(and_(models.Satellites.id == id))
    satellites_edited_record = query.first()

    if satellites_edited_record:
        for key, value in {
            "id": id,
            "name": name,
            "norad_id": norad_id,
            "tle_line1": tle_line1,
            "tle_line2": tle_line2,
            "created_at_dt": created_at_dt,
        }.items():
            setattr(satellites_edited_record, key, value)

        db.commit()

        # db.refresh(satellites_edited_record)

        satellites_edited_record = (
            satellites_edited_record.to_dict()
            if hasattr(satellites_edited_record, "to_dict")
            else vars(satellites_edited_record)
        )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"satellites_edited_record": satellites_edited_record},
    }
    return res


async def delete_satellites_id(request: Request, db: Session, id: Union[int, float]):

    query = db.query(models.Satellites)
    query = query.filter(and_(models.Satellites.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        satellites_deleted = record_to_delete.to_dict()
    else:
        satellites_deleted = record_to_delete

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"satellites_deleted": satellites_deleted},
    }
    return res


async def get_conjunction_alerts(request: Request, db: Session):

    query = db.query(models.ConjunctionAlerts)

    conjunction_alerts_all = query.all()
    conjunction_alerts_all = (
        [new_data.to_dict() for new_data in conjunction_alerts_all]
        if conjunction_alerts_all
        else conjunction_alerts_all
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"conjunction_alerts_all": conjunction_alerts_all},
    }
    return res


async def get_conjunction_alerts_id(
    request: Request, db: Session, id: Union[int, float]
):

    query = db.query(models.ConjunctionAlerts)
    query = query.filter(and_(models.ConjunctionAlerts.id == id))

    conjunction_alerts_one = query.first()

    conjunction_alerts_one = (
        (
            conjunction_alerts_one.to_dict()
            if hasattr(conjunction_alerts_one, "to_dict")
            else vars(conjunction_alerts_one)
        )
        if conjunction_alerts_one
        else conjunction_alerts_one
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"conjunction_alerts_one": conjunction_alerts_one},
    }
    return res


async def post_conjunction_alerts(
    request: Request,
    db: Session,
    raw_data: schemas.PostConjunctionAlerts,
):
    satellite_a_id: Union[int, float] = raw_data.satellite_a_id
    satellite_b_id: Union[int, float] = raw_data.satellite_b_id
    miss_km: float = raw_data.miss_km
    approach_dt: str = convert_to_datetime(raw_data.approach_dt)
    created_at_dt: str = convert_to_datetime(raw_data.created_at_dt)

    record_to_be_added = {
        "miss_km": miss_km,
        "approach_dt": approach_dt,
        "created_at_dt": created_at_dt,
        "satellite_a_id": satellite_a_id,
        "satellite_b_id": satellite_b_id,
    }
    new_conjunction_alerts = models.ConjunctionAlerts(**record_to_be_added)
    db.add(new_conjunction_alerts)
    db.commit()
    # db.refresh(new_conjunction_alerts)
    conjunction_alerts_inserted_record = new_conjunction_alerts.to_dict()

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {
            "conjunction_alerts_inserted_record": conjunction_alerts_inserted_record
        },
    }
    return res


async def put_conjunction_alerts_id(
    request: Request,
    db: Session,
    raw_data: schemas.PutConjunctionAlertsId,
):
    id: Union[int, float] = raw_data.id
    satellite_a_id: Union[int, float] = raw_data.satellite_a_id
    satellite_b_id: Union[int, float] = raw_data.satellite_b_id
    miss_km: float = raw_data.miss_km
    approach_dt: str = convert_to_datetime(raw_data.approach_dt)
    created_at_dt: str = convert_to_datetime(raw_data.created_at_dt)

    query = db.query(models.ConjunctionAlerts)
    query = query.filter(and_(models.ConjunctionAlerts.id == id))
    conjunction_alerts_edited_record = query.first()

    if conjunction_alerts_edited_record:
        for key, value in {
            "id": id,
            "miss_km": miss_km,
            "approach_dt": approach_dt,
            "created_at_dt": created_at_dt,
            "satellite_a_id": satellite_a_id,
            "satellite_b_id": satellite_b_id,
        }.items():
            setattr(conjunction_alerts_edited_record, key, value)

        db.commit()

        # db.refresh(conjunction_alerts_edited_record)

        conjunction_alerts_edited_record = (
            conjunction_alerts_edited_record.to_dict()
            if hasattr(conjunction_alerts_edited_record, "to_dict")
            else vars(conjunction_alerts_edited_record)
        )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"conjunction_alerts_edited_record": conjunction_alerts_edited_record},
    }
    return res


async def delete_conjunction_alerts_id(
    request: Request, db: Session, id: Union[int, float]
):

    query = db.query(models.ConjunctionAlerts)
    query = query.filter(and_(models.ConjunctionAlerts.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        conjunction_alerts_deleted = record_to_delete.to_dict()
    else:
        conjunction_alerts_deleted = record_to_delete

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"conjunction_alerts_deleted": conjunction_alerts_deleted},
    }
    return res


async def get_user_watchlist(request: Request, db: Session):

    query = db.query(models.UserWatchlist)

    user_watchlist_all = query.all()
    user_watchlist_all = (
        [new_data.to_dict() for new_data in user_watchlist_all]
        if user_watchlist_all
        else user_watchlist_all
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"user_watchlist_all": user_watchlist_all},
    }
    return res


async def get_user_watchlist_user_id(
    request: Request, db: Session, user_id: Union[int, float]
):

    query = db.query(models.UserWatchlist)
    query = query.filter(and_(models.UserWatchlist.user_id == user_id))

    user_watchlist_one = query.first()

    user_watchlist_one = (
        (
            user_watchlist_one.to_dict()
            if hasattr(user_watchlist_one, "to_dict")
            else vars(user_watchlist_one)
        )
        if user_watchlist_one
        else user_watchlist_one
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"user_watchlist_one": user_watchlist_one},
    }
    return res


async def post_user_watchlist(
    request: Request,
    db: Session,
    raw_data: schemas.PostUserWatchlist,
):
    user_id: Union[int, float] = raw_data.user_id
    satellite_id: Union[int, float] = raw_data.satellite_id
    created_at_dt: str = convert_to_datetime(raw_data.created_at_dt)

    record_to_be_added = {
        "user_id": user_id,
        "satellite_id": satellite_id,
        "created_at_dt": created_at_dt,
    }
    new_user_watchlist = models.UserWatchlist(**record_to_be_added)
    db.add(new_user_watchlist)
    db.commit()
    # db.refresh(new_user_watchlist)
    user_watchlist_inserted_record = new_user_watchlist.to_dict()

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"user_watchlist_inserted_record": user_watchlist_inserted_record},
    }
    return res


async def put_user_watchlist_user_id(
    request: Request,
    db: Session,
    raw_data: schemas.PutUserWatchlistUserId,
):
    user_id: Union[int, float] = raw_data.user_id
    satellite_id: Union[int, float] = raw_data.satellite_id
    created_at_dt: str = convert_to_datetime(raw_data.created_at_dt)

    query = db.query(models.UserWatchlist)
    query = query.filter(and_(models.UserWatchlist.user_id == user_id))
    user_watchlist_edited_record = query.first()

    if user_watchlist_edited_record:
        for key, value in {
            "user_id": user_id,
            "satellite_id": satellite_id,
            "created_at_dt": created_at_dt,
        }.items():
            setattr(user_watchlist_edited_record, key, value)

        db.commit()

        # db.refresh(user_watchlist_edited_record)

        user_watchlist_edited_record = (
            user_watchlist_edited_record.to_dict()
            if hasattr(user_watchlist_edited_record, "to_dict")
            else vars(user_watchlist_edited_record)
        )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"user_watchlist_edited_record": user_watchlist_edited_record},
    }
    return res


async def get_users(request: Request, db: Session):

    query = db.query(models.Users)

    users_all = query.all()
    users_all = (
        [new_data.to_dict() for new_data in users_all] if users_all else users_all
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"users_all": users_all},
    }
    return res


async def get_users_id(request: Request, db: Session, id: Union[int, float]):

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.id == id))

    users_one = query.first()

    users_one = (
        (users_one.to_dict() if hasattr(users_one, "to_dict") else vars(users_one))
        if users_one
        else users_one
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"users_one": users_one},
    }
    return res


async def post_users(
    request: Request,
    db: Session,
    raw_data: schemas.PostUsers,
):
    email: str = raw_data.email
    password: str = raw_data.password
    created_at_dt: str = convert_to_datetime(raw_data.created_at_dt)

    record_to_be_added = {
        "email": email,
        "password": password,
        "created_at_dt": created_at_dt,
    }
    new_users = models.Users(**record_to_be_added)
    db.add(new_users)
    db.commit()
    # db.refresh(new_users)
    users_inserted_record = new_users.to_dict()

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"users_inserted_record": users_inserted_record},
    }
    return res


async def put_users_id(
    request: Request,
    db: Session,
    raw_data: schemas.PutUsersId,
):
    id: Union[int, float] = raw_data.id
    email: str = raw_data.email
    password: str = raw_data.password
    created_at_dt: str = convert_to_datetime(raw_data.created_at_dt)

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.id == id))
    users_edited_record = query.first()

    if users_edited_record:
        for key, value in {
            "id": id,
            "email": email,
            "password": password,
            "created_at_dt": created_at_dt,
        }.items():
            setattr(users_edited_record, key, value)

        db.commit()

        # db.refresh(users_edited_record)

        users_edited_record = (
            users_edited_record.to_dict()
            if hasattr(users_edited_record, "to_dict")
            else vars(users_edited_record)
        )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"users_edited_record": users_edited_record},
    }
    return res


async def delete_users_id(request: Request, db: Session, id: Union[int, float]):

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        users_deleted = record_to_delete.to_dict()
    else:
        users_deleted = record_to_delete

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"users_deleted": users_deleted},
    }
    return res


async def delete_user_watchlist_user_id(
    request: Request, db: Session, user_id: Union[int, float]
):

    query = db.query(models.UserWatchlist)
    query = query.filter(and_(models.UserWatchlist.user_id == user_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        user_watchlist_deleted = record_to_delete.to_dict()
    else:
        user_watchlist_deleted = record_to_delete

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"user_watchlist_deleted": user_watchlist_deleted},
    }
    return res
