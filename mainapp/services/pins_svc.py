from mainapp import db
from sqlalchemy import text
from flask import current_app
import json

def add_new_pin( title, address, latitude, longitude, rating1, rating2, description):
    # SQL query to insert new pin
    sql_string = """
        INSERT INTO Pin (title, address, latitude, longitude, rating1, rating2, description)
        VALUES (:title, :address, :latitude, :longitude, :rating1, :rating2, :description)
    """

    # Bind parameters to the SQL query
    sql = db.text( sql_string )
    sql_with_parms = sql.bindparams(
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
        rs = conn.execute( sql_with_parms )
        inserted_id = rs.lastrowid
        conn.commit()
    return inserted_id

def pins_list() -> list:
    select_statement = f"""
    SELECT * FROM Pin;
    """

    sql = text(select_statement)
    sql_with_parms = sql.bindparams()

    pins_list = []
    

    with db.engine.connect() as conn:
        rs = conn.execute(sql_with_parms)

        for row in rs.mappings():
            pins_list.append(row)
    return pins_list