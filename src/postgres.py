import psycopg2
import pandas as pd
from psycopg2 import Error
import postgres_tables as tables
import postgres_insert_queries as queries
import fffl

user = "postgres"
password = "Rodgers12"
host = "localhost"
port = 5432
database = "postgres"

owners = [
    "Sarge",
    "Lude",
    "Gresh",
    "Ceej",
    "Ost",
    "Schingen",
    "Winks",
    "Faber",
    "Frank",
    "Benny",
    "Strand",
    "Rades",
]


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


def bulkInsert(records, table, insert_query):
    try:
        connection = psycopg2.connect(
            user=user, password=password, host=host, port=port, database=database,
        )
        cursor = connection.cursor()

        # executemany() to insert multiple rows rows
        result = cursor.executemany(insert_query, records)
        connection.commit()
        print(cursor.rowcount,
              f"Records inserted successfully into table: {table}")

    except (Exception, psycopg2.Error) as error:
        print("Failed inserting record into table {}".format(error))

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


if __name__ == "__main__":
    create_table(tables.standings)
    # drop_table('standings')

    # bulkInsert(fffl.updateStandings(2019), "standings", queries.standings)
    # drop_table("player_scores")

    # for year in range(2009, 2009):
    #     print(f"inserting records for {year}")
    #     bulkInsert(fffl.get_scoring_settings(year), "scoring_settings")

    # for year in range(2020, 2021):
    #     print(f'inserting records for {year}')
    #     for week in range(1, 17):
    #         bulkInsert(fffl.parse_scores(year, week),
    #                    'weekly_scores', queries.weekly_scores)

    # Fill player_scores tables

    # for owner in owners:
    #     # for owner in ['Rades']:

    #     for year in range(2020, 2021):
    #         records = []
    #         for week in range(1, 7):
    #             stats = fffl.get_roster(owner, year, week)
    #             stats = stats.set_index("id").reset_index()
    #             stats = list(stats.itertuples(index=False, name=None))

    #             records.extend(stats)

    #         table = "player_scores"
    #         bulkInsert(records, 'player_scores', queries.player_scores)
