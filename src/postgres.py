import psycopg2
import pandas as pd
from psycopg2 import Error
import postgres_tables
import fffl

user = "postgres"
password = "rodgers12"
host = "127.0.0.1"
port = "5432"
database = "fffl"


def create_table(create_table_query):
    try:
        connection = psycopg2.connect(
            user=user, password=password, host=host, port=port, database=database,
        )

        cursor = connection.cursor()
        cursor.execute(create_table_query)
        connection.commit()
        print("Table created successfully in PostgreSQL ")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while creating PostgreSQL table", error)
    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def drop_table(table_name):
    try:
        connection = psycopg2.connect(
            user=user, password=password, host=host, port=port, database=database,
        )

        cursor = connection.cursor()
        create_table_query = " DROP TABLE IF EXISTS %s" % (table_name)

        cursor.execute(create_table_query)
        connection.commit()
        print(f"{table_name} dropped successfully in PostgreSQL ")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while creating PostgreSQL table", error)
    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def bulkInsert(records, table):
    try:
        connection = psycopg2.connect(
            user=user, password=password, host=host, port=port, database=database,
        )
        cursor = connection.cursor()

        # sql_insert_query = """ INSERT INTO scores (id, year, week, team, pts_for, opponent, pts_against)
        #                    VALUES (%s,%s,%s,%s,%s,%s,%s)
        #                    ON CONFLICT (id)
        #                    DO UPDATE SET (id, year, week, team, pts_for, opponent, pts_against) =
        #                    (EXCLUDED.id, EXCLUDED.year, EXCLUDED.week, EXCLUDED.team, EXCLUDED.pts_for, EXCLUDED.opponent, EXCLUDED.pts_against)"""

        sql_insert_query = """ INSERT INTO scoring_settings (id, year, stat_id, name, value)
                           VALUES (%s,%s,%s,%s,%s)
                           ON CONFLICT (id) 
                           DO UPDATE SET (id, year, stat_id, name, value) = 
                           (EXCLUDED.id, EXCLUDED.year, EXCLUDED.stat_id, EXCLUDED.name, EXCLUDED.value)"""

        # executemany() to insert multiple rows rows
        result = cursor.executemany(sql_insert_query, records)
        connection.commit()
        print(cursor.rowcount, f"Records inserted successfully into table: {table}")

    except (Exception, psycopg2.Error) as error:
        print("Failed inserting record into table {}".format(error))

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


if __name__ == "__main__":
    # create_table(postgres_tables.scoring_settings)
    # drop_table("scoring_settings")
    for year in range(2005, 2020):
        print(f"inserting records for {year}")
        bulkInsert(fffl.get_scoring_settings(year), "scoring_settings")
