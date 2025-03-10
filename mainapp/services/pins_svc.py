from mainapp import db
from sqlalchemy import text
from flask import current_app
import json

def add_new_pin( title, address, latitude, longitude, rating1, rating2, description, favorited):
    # SQL query to insert new pin
    sql_string = """
        INSERT INTO Pin (title, address, latitude, longitude, rating1, rating2, description, favorited)
        VALUES (:title, :address, :latitude, :longitude, :rating1, :rating2, :description, :favorited)
    """

    # Bind parameters to the SQL query
    sql = db.text( sql_string )
    sql_with_params = sql.bindparams(
        title=title,
        address=address,
        latitude=latitude,
        longitude=longitude,
        rating1=rating1,
        rating2=rating2,
        description=description,
        favorited=favorited
    )

    # Execute the SQL query and commit the changes
    inserted_id = -1
    with db.engine.connect() as conn:
        rs = conn.execute( sql_with_params )
        inserted_id = rs.lastrowid
        conn.commit()
    return inserted_id

def edit_pin( pkid, title, address, latitude, longitude, rating1, rating2, description):
    # SQL query to insert new pin
    sql_string = """
        UPDATE Pin SET title = :title, address = :address, latitude = :latitude,
        longitude = :longitude, rating1 = :rating1, rating2 = :rating2, description = :description
        WHERE pkid = :pkid 
    """

    # Bind parameters to the SQL query
    sql = db.text( sql_string )
    sql_with_params = sql.bindparams(
        pkid=pkid,
        title=title,
        address=address,
        latitude=latitude,
        longitude=longitude,
        rating1=rating1,
        rating2=rating2,
        description=description
    )

    # Execute the SQL query and commit the changes
    inserted_id = -1
    with db.engine.connect() as conn:
        rs = conn.execute( sql_with_params )
        inserted_id = rs.lastrowid
        conn.commit()
    return inserted_id

def pins_list() -> list:
    select_statement = f"""
    SELECT * FROM Pin;
    """

    sql = text(select_statement)
    sql_with_params = sql.bindparams()

    pins_list = []
    

    with db.engine.connect() as conn:
        rs = conn.execute(sql_with_params)

        for row in rs.mappings():
            pins_list.append(row)
    return pins_list

def pins_list_favorite() -> list:
    select_statement = f"""
    SELECT * FROM Pin WHERE favorited='true';
    """

    sql = text(select_statement)
    sql_with_params = sql.bindparams()

    pins_list = []
    

    with db.engine.connect() as conn:
        rs = conn.execute(sql_with_params)

        for row in rs.mappings():
            pins_list.append(row)
    return pins_list

def get_pin( pkid ) -> list:
    select_statement = f"""
    SELECT * FROM Pin
    WHERE pkid = :pkid;
    """

    sql = text(select_statement)
    sql_with_params = sql.bindparams(pkid=pkid)

    pins_list = []
    

    with db.engine.connect() as conn:
        rs = conn.execute(sql_with_params)

        for row in rs.mappings():
            pins_list.append(row)
    return pins_list

def get_last_pkid():
    select_statement= f"""
    SELECT pkid FROM Pin
    ORDER BY pkid DESC
    LIMIT 1;
    """

    sql = text(select_statement)
    sql_with_params = sql.bindparams()

    pkid = []

    with db.engine.connect() as conn:
        rs = conn.execute(sql_with_params)

        for row in rs.mappings():
            pkid.append(row)
    return pkid