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

player_scores = """CREATE TABLE player_scores
          (ID BIGINT PRIMARY KEY NOT NULL,
          OWNER TEXT    NOT NULL,
          WEEK INT      NOT NULL,
          YEAR INT      NOT NULL,
          NAME TEXT     NOT NULL,
          SELECTED_POSITION TEXT NOT NULL,
          PLAYER_POSITION TEXT   NOT NULL,
          PLAYER_KEY TEXT   NOT NULL,
          PLAYER_ID INT NOT NULL,
          POINTS FLOAT8 NOT NULL); """
