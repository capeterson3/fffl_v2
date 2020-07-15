scores = """CREATE TABLE scores
          (ID INT PRIMARY KEY NOT NULL,
          YEAR INT      NOT NULL,
          WEEK INT    NOT NULL,
          TEAM TEXT   NOT NULL,
          PTS_FOR FLOAT8 NOT NULL,
          OPPONENT TEXT   NOT NULL,
          PTS_AGAINST FLOAT8 NOT NULL); """


manager_ids = """CREATE TABLE manager_ids
          (ID INT PRIMARY KEY NOT NULL,
          YEAR INT      NOT NULL,
          MANAGER TEXT   NOT NULL); """

scoring_settings = """CREATE TABLE scoring_settings
          (ID INT PRIMARY KEY NOT NULL,
          YEAR INT      NOT NULL,
          STAT_ID INT   NOT NULL,
          NAME TEXT     NOT NULL,
          VALUE FLOAT8 NOT NULL); """
