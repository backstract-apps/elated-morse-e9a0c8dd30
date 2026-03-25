from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile,Query, Form
from sqlalchemy.orm import Session
from typing import List,Annotated
import service, models, schemas
from fastapi import Query
from database import SessionLocal
from middleware.application_middleware import default_dependency


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/ground_stations/')
async def get_ground_stations(request: Request, db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.get_ground_stations(request, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/ground_stations/id/')
async def get_ground_stations_id(request: Request, query: schemas.GetGroundStationsIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.get_ground_stations_id(request, db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/ground_stations/')
async def post_ground_stations(request: Request, raw_data: schemas.PostGroundStations, db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.post_ground_stations(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/ground_stations/id/')
async def put_ground_stations_id(request: Request, raw_data: schemas.PutGroundStationsId, db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.put_ground_stations_id(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/ground_stations/id/')
async def delete_ground_stations_id(request: Request, query: schemas.DeleteGroundStationsIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.delete_ground_stations_id(request, db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/satellites/')
async def get_satellites(request: Request, db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.get_satellites(request, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/satellites/id/')
async def get_satellites_id(request: Request, query: schemas.GetSatellitesIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.get_satellites_id(request, db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/satellites/')
async def post_satellites(request: Request, raw_data: schemas.PostSatellites, db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.post_satellites(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/satellites/id/')
async def put_satellites_id(request: Request, raw_data: schemas.PutSatellitesId, db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.put_satellites_id(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/satellites/id/')
async def delete_satellites_id(request: Request, query: schemas.DeleteSatellitesIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.delete_satellites_id(request, db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/conjunction_alerts/')
async def get_conjunction_alerts(request: Request, db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.get_conjunction_alerts(request, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/conjunction_alerts/id/')
async def get_conjunction_alerts_id(request: Request, query: schemas.GetConjunctionAlertsIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.get_conjunction_alerts_id(request, db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/conjunction_alerts/')
async def post_conjunction_alerts(request: Request, raw_data: schemas.PostConjunctionAlerts, db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.post_conjunction_alerts(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/conjunction_alerts/id/')
async def put_conjunction_alerts_id(request: Request, raw_data: schemas.PutConjunctionAlertsId, db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.put_conjunction_alerts_id(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/conjunction_alerts/id/')
async def delete_conjunction_alerts_id(request: Request, query: schemas.DeleteConjunctionAlertsIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.delete_conjunction_alerts_id(request, db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/user_watchlist/')
async def get_user_watchlist(request: Request, db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.get_user_watchlist(request, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/user_watchlist/user_id/')
async def get_user_watchlist_user_id(request: Request, query: schemas.GetUserWatchlistUserIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.get_user_watchlist_user_id(request, db, query.user_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/user_watchlist/')
async def post_user_watchlist(request: Request, raw_data: schemas.PostUserWatchlist, db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.post_user_watchlist(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/user_watchlist/user_id/')
async def put_user_watchlist_user_id(request: Request, raw_data: schemas.PutUserWatchlistUserId, db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.put_user_watchlist_user_id(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/users/')
async def get_users(request: Request, db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.get_users(request, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/users/id/')
async def get_users_id(request: Request, query: schemas.GetUsersIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.get_users_id(request, db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/users/')
async def post_users(request: Request, raw_data: schemas.PostUsers, db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.post_users(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/users/id/')
async def put_users_id(request: Request, raw_data: schemas.PutUsersId, db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.put_users_id(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/users/id/')
async def delete_users_id(request: Request, query: schemas.DeleteUsersIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.delete_users_id(request, db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/user_watchlist/user_id/')
async def delete_user_watchlist_user_id(request: Request, query: schemas.DeleteUserWatchlistUserIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.delete_user_watchlist_user_id(request, db, query.user_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

