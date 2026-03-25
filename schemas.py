from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple,Union

import re

class Users(BaseModel):
    email: Optional[str]=None
    password: Optional[str]=None
    created_at_dt: Optional[Any]=None


class ReadUsers(BaseModel):
    email: Optional[str]=None
    password: Optional[str]=None
    created_at_dt: Optional[Any]=None
    class Config:
        from_attributes = True


class Satellites(BaseModel):
    norad_id: Optional[Union[int, float]]=None
    name: Optional[str]=None
    tle_line1: Optional[str]=None
    tle_line2: Optional[str]=None
    created_at_dt: Optional[Any]=None


class ReadSatellites(BaseModel):
    norad_id: Optional[Union[int, float]]=None
    name: Optional[str]=None
    tle_line1: Optional[str]=None
    tle_line2: Optional[str]=None
    created_at_dt: Optional[Any]=None
    class Config:
        from_attributes = True


class GroundStations(BaseModel):
    user_id: Optional[Union[int, float]]=None
    name: Optional[str]=None
    latitude: Optional[float]=None
    longitude: Optional[float]=None
    created_at_dt: Optional[Any]=None


class ReadGroundStations(BaseModel):
    user_id: Optional[Union[int, float]]=None
    name: Optional[str]=None
    latitude: Optional[float]=None
    longitude: Optional[float]=None
    created_at_dt: Optional[Any]=None
    class Config:
        from_attributes = True


class ConjunctionAlerts(BaseModel):
    satellite_a_id: Optional[Union[int, float]]=None
    satellite_b_id: Optional[Union[int, float]]=None
    miss_km: Optional[float]=None
    approach_dt: Optional[Any]=None
    created_at_dt: Optional[Any]=None


class ReadConjunctionAlerts(BaseModel):
    satellite_a_id: Optional[Union[int, float]]=None
    satellite_b_id: Optional[Union[int, float]]=None
    miss_km: Optional[float]=None
    approach_dt: Optional[Any]=None
    created_at_dt: Optional[Any]=None
    class Config:
        from_attributes = True


class UserWatchlist(BaseModel):
    user_id: int
    satellite_id: int
    created_at_dt: Optional[Any]=None


class ReadUserWatchlist(BaseModel):
    user_id: int
    satellite_id: int
    created_at_dt: Optional[Any]=None
    class Config:
        from_attributes = True




class PostGroundStations(BaseModel):
    user_id: Optional[Union[int, float]]=None
    name: Optional[str]=None
    latitude: Optional[Any]=None
    longitude: Optional[Any]=None
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PutGroundStationsId(BaseModel):
    id: Union[int, float] = Field(...)
    user_id: Optional[Union[int, float]]=None
    name: Optional[str]=None
    latitude: Optional[Any]=None
    longitude: Optional[Any]=None
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PostSatellites(BaseModel):
    norad_id: Optional[Union[int, float]]=None
    name: Optional[str]=None
    tle_line1: Optional[str]=None
    tle_line2: Optional[str]=None
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PutSatellitesId(BaseModel):
    id: Union[int, float] = Field(...)
    norad_id: Optional[Union[int, float]]=None
    name: Optional[str]=None
    tle_line1: Optional[str]=None
    tle_line2: Optional[str]=None
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PostConjunctionAlerts(BaseModel):
    satellite_a_id: Optional[Union[int, float]]=None
    satellite_b_id: Optional[Union[int, float]]=None
    miss_km: Optional[Any]=None
    approach_dt: Optional[str]=None
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PutConjunctionAlertsId(BaseModel):
    id: Union[int, float] = Field(...)
    satellite_a_id: Optional[Union[int, float]]=None
    satellite_b_id: Optional[Union[int, float]]=None
    miss_km: Optional[Any]=None
    approach_dt: Optional[str]=None
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PostUserWatchlist(BaseModel):
    user_id: Union[int, float] = Field(...)
    satellite_id: Union[int, float] = Field(...)
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PutUserWatchlistUserId(BaseModel):
    user_id: Union[int, float] = Field(...)
    satellite_id: Union[int, float] = Field(...)
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PostUsers(BaseModel):
    email: Optional[str]=None
    password: Optional[str]=None
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PutUsersId(BaseModel):
    id: Union[int, float] = Field(...)
    email: Optional[str]=None
    password: Optional[str]=None
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



# Query Parameter Validation Schemas

class GetGroundStationsIdQueryParams(BaseModel):
    """Query parameter validation for get_ground_stations_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class DeleteGroundStationsIdQueryParams(BaseModel):
    """Query parameter validation for delete_ground_stations_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class GetSatellitesIdQueryParams(BaseModel):
    """Query parameter validation for get_satellites_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class DeleteSatellitesIdQueryParams(BaseModel):
    """Query parameter validation for delete_satellites_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class GetConjunctionAlertsIdQueryParams(BaseModel):
    """Query parameter validation for get_conjunction_alerts_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class DeleteConjunctionAlertsIdQueryParams(BaseModel):
    """Query parameter validation for delete_conjunction_alerts_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class GetUserWatchlistUserIdQueryParams(BaseModel):
    """Query parameter validation for get_user_watchlist_user_id"""
    user_id: int = Field(..., ge=1, description="User Id")

    class Config:
        populate_by_name = True


class GetUsersIdQueryParams(BaseModel):
    """Query parameter validation for get_users_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class DeleteUsersIdQueryParams(BaseModel):
    """Query parameter validation for delete_users_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class DeleteUserWatchlistUserIdQueryParams(BaseModel):
    """Query parameter validation for delete_user_watchlist_user_id"""
    user_id: int = Field(..., ge=1, description="User Id")

    class Config:
        populate_by_name = True
