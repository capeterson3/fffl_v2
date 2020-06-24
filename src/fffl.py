import pandas as pd

# from yahoo_oauth import OAuth2
import json
from auth import yahoo_auth
import os

with open("./auth/oauth2yahoo.json") as json_yahoo_file:
    auths = json.load(json_yahoo_file)
yahoo_consumer_key = auths["consumer_key"]
yahoo_consumer_secret = auths["consumer_secret"]
yahoo_access_key = auths["access_token"]
json_yahoo_file.close()

yahoo_api = yahoo_auth.Yahoo_Api(
    yahoo_consumer_key, yahoo_consumer_secret, yahoo_access_key
)
yahoo_api._login()


def findGameID(year):

    with open("./data/league_info/league_id_mapping.json", "r") as m:
        league_id_mapping = eval(m.read())

    league_id = league_id_mapping[str(year)]["league_id"]

    for id in range(350, 500):
        url = (
            "https://fantasysports.yahooapis.com/fantasy/v2/league/"
            + str(id)
            + ".l."
            + str(league_id)
            + "/"
        )

        response = yahoo_auth.oauth.session.get(url, params={"format": "json"})

        if response.status_code == 200:
            r = response.json()
            if (
                r["fantasy_content"]["league"][0]["name"] == "FFFL"
                and r["fantasy_content"]["league"][0]["league_type"] == "private"
            ):
                return id
                break


def updateScoreboards(year):

    if not os.path.exists("./data/weekly_scoreboards/" + str(year)):
        os.makedirs("./data/weekly_scoreboards/" + str(year))

    with open("./data/league_info/league_id_mapping.json", "r") as m:
        league_id_mapping = eval(m.read())

    league_id = league_id_mapping[str(year)]["league_id"]
    game_id = league_id_mapping[str(year)]["game_id"]
    week = 1

    while week < 17:  # assumes 16 week-schedule
        print("Updating scoreboards for " + str(year) + ", week " + str(week))
        url = (
            "https://fantasysports.yahooapis.com/fantasy/v2/league/"
            + str(game_id)
            + ".l."
            + str(league_id)
            + "/scoreboard;week="
            + str(week)
        )
        response = yahoo_auth.oauth.session.get(url, params={"format": "json"})
        r = response.json()
        file_name = "week_" + str(week) + "_scoreboard.json"

        with open(
            "./data/weekly_scoreboards/" + str(year) + "/" + file_name, "w+"
        ) as outfile:
            json.dump(r, outfile)

        week += 1

    return


def parse_scores(year, week):
    # load team number and names references as a dictionary
    team_numbers = {}
    with open("./data/owner_info/team_mapping.json", "r") as f:
        team_numbers = json.load(f)

    scores = []

    filename = (
        "./data/weekly_scoreboards/"
        + str(year)
        + "/week_"
        + str(week)
        + "_scoreboard.json"
    )
    with open(filename) as json_file:
        data = json.load(json_file)

    data = data["fantasy_content"]["league"][1]["scoreboard"]["0"]["matchups"]

    # Pad week number with leading 0 if less than 10
    week = str(week).zfill(2)

    # Loop through 6 matchups each week
    for i in range(0, 6):
        matchup_num = "'" + str(i) + "'"

        for j in range(1, 3):
            matchup_switch = "'" + str(j % 2) + "'"

            try:
                team = data[eval(matchup_num)]["matchup"]["0"]["teams"][
                    eval("'" + str(j - 1) + "'")
                ]["team"][0][0]["team_key"]
                team = team_numbers[str(year)][team]

                pts_for = data[eval(matchup_num)]["matchup"]["0"]["teams"][
                    eval("'" + str(j - 1) + "'")
                ]["team"][1]["team_points"]["total"]

                opponent = data[eval(matchup_num)]["matchup"]["0"]["teams"][
                    eval(matchup_switch)
                ]["team"][0][0]["team_key"]
                opponent = team_numbers[str(year)][opponent]

                pts_against = data[eval(matchup_num)]["matchup"]["0"]["teams"][
                    eval(matchup_switch)
                ]["team"][1]["team_points"]["total"]

                matchup = (
                    int(str(year) + str(week) + str(i) + str(j)),
                    year,
                    week,
                    team,
                    pts_for,
                    opponent,
                    pts_against,
                )
                scores.append(matchup)

            except:
                pass

    print(scores)
    return scores


if __name__ == "__main__":
    # for year in range(2005, 2020):
    #     updateScoreboards(year)

    # updateScoreboards(2019)

    print(parse_scores(2019, 10))