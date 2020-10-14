weekly_scores = """ INSERT INTO weekly_scores (id, year, week, team, pts_for, opponent, pts_against)
                           VALUES (%s,%s,%s,%s,%s,%s,%s)
                           ON CONFLICT (id)
                           DO UPDATE SET (id, year, week, team, pts_for, opponent, pts_against) =
                           (EXCLUDED.id, EXCLUDED.year, EXCLUDED.week, EXCLUDED.team, EXCLUDED.pts_for, EXCLUDED.opponent, EXCLUDED.pts_against)"""

# manager_ids = """CREATE TABLE manager_ids
#           (ID INT PRIMARY KEY NOT NULL,
#           YEAR INT      NOT NULL,
#           MANAGER TEXT   NOT NULL); """

scoring_settings = """ INSERT INTO scoring_settings (id, year, stat_id, name, value)
                           VALUES (%s,%s,%s,%s,%s)
                           ON CONFLICT (id)
                           DO UPDATE SET (id, year, stat_id, name, value) =
                           (EXCLUDED.id, EXCLUDED.year, EXCLUDED.stat_id, EXCLUDED.name, EXCLUDED.value)"""


player_scores = """ INSERT INTO player_scores (id, owner, week, year, name, selected_position, player_position, player_key, player_id, points)
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    ON CONFLICT (id)
                    DO UPDATE SET (id, owner, week, year, name, selected_position, player_position, player_key, player_id, points) =
                    (EXCLUDED.id, EXCLUDED.owner, EXCLUDED.week, EXCLUDED.year, EXCLUDED.name, EXCLUDED.selected_position, EXCLUDED.player_position, EXCLUDED.player_key, EXCLUDED.player_id, EXCLUDED.points)"""

standings = """ INSERT INTO standings (year, owner, number_of_moves, number_of_trades, clinched_playoffs, finish, playoff_seed, wins, losses, ties, pts_for, pts_against)                           
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                ON CONFLICT (year, owner)
                DO UPDATE SET (year, owner, number_of_moves, number_of_trades, clinched_playoffs, finish, playoff_seed, wins, losses, ties, pts_for, pts_against) =
                (EXCLUDED.year, EXCLUDED.owner, EXCLUDED.number_of_moves, EXCLUDED.number_of_trades, EXCLUDED.clinched_playoffs, EXCLUDED.finish, EXCLUDED.playoff_seed, EXCLUDED.wins, EXCLUDED.losses, EXCLUDED.ties, EXCLUDED.pts_for, EXCLUDED.pts_against)"""
