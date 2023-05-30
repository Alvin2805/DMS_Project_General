from sqlalchemy.orm import Session
from sqlalchemy import select, column
from src.entities import RegionEntity 
from src.schemas import RegionSchema
import math
from src.utils.BoolConvert import strtobool

#get all data
def get_region_all(db:Session,skip:int,limit:int,query:list[str],query_by:list[str]):    
    query_check = select(RegionEntity.MtrRegion)

    page = skip
    page_limit = limit
    total_rows = db.query(RegionEntity.MtrRegion).count()
    total_pages = int(math.ceil(total_rows/page_limit))

    if (query != None):
        for idx,x in enumerate(query):
            if query_by[idx] != "is_active":
                query_check = query_check.where(column(query_by[idx]).contains(query[idx]))
            query_check = query_check.where(column(query_by[idx]).contains(strtobool(query[idx])))

    query_final = query_check.order_by(RegionEntity.MtrRegion.region_id).offset(page*page_limit).limit(page_limit)

    final_res = db.execute(query_final).all()
    
    return page,page_limit,total_rows,total_pages,final_res

#get data by filtering the primary_key(ID)
def get_region_by_id(db:Session,get_id:int):
    return db.query(RegionEntity.MtrRegion).filter(RegionEntity.MtrRegion.region_id==get_id).first()

#get data by filtering the param(s)
def get_region_by_params(db:Session,code):
    return db.query(RegionEntity.MtrRegion).filter(RegionEntity.MtrRegion.region_code==code).all()


#post / create new data
def post_new_region(db:Session,region:RegionSchema.MtrRegionSchema):
    _region = RegionEntity.MtrRegion()
    _region.region_code = region.region_code
    _region.region_name = region.region_name
    _region.user_id = region.user_id
    db.add(_region)
    db.commit()
    db.refresh(_region)
    print(_region)
    return _region

#delete data by primary_key(ID)
def del_region(db:Session,del_id:int):
    _region = get_region_by_id(db=db,get_id=del_id)
    db.delete(_region)
    db.commit()
    return {
        "status_code":200,
        "msg_status":"deleted"
    }

#update data by primary_key(ID)
def update_region(db:Session,update_id:int,region:RegionSchema.MtrRegionSchema):
    _region = get_region_by_id(db,update_id)
    _region.region_code = region.region_code
    _region.region_name = region.region_name
    _region.user_id = region.user_id
    db.commit()
    db.refresh(_region)
    return _region