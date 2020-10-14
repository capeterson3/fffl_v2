import json


def get_manager_ids(year):
    filename = "./data/weekly_scoreboards/" + \
        str(year) + "/week_1_scoreboard.json"
    with open(filename) as json_file:
        data = json.load(json_file)

    with open("./data/owner_info/email_mapping.json") as f:
        email_mapping = json.load(f)

    league_key = data["fantasy_content"]["league"][0]["league_key"]

    team_mapping = {}

    for matchup in range(0, 6):
        matchup_num = "'" + str(matchup) + "'"

        for team in range(0, 2):
            team_num = "'" + str(team) + "'"
            manager_data = data["fantasy_content"]["league"][1]["scoreboard"]["0"]["matchups"][eval(
                matchup_num)]["matchup"]["0"]["teams"][eval(team_num)]["team"][0][19]["managers"][0]["manager"]

            nickname = manager_data["nickname"]
            # team_id = manager_data["manager_id"]
            team_id = data["fantasy_content"]["league"][1]["scoreboard"]["0"]["matchups"][eval(
                matchup_num)]["matchup"]["0"]["teams"][eval(team_num)]["team"][0][1]["team_id"]

            try:
                email = manager_data["email"]
            except:
                owner = input("Who is this?: " + nickname + " :")
                team_mapping[league_key + ".t." + team_id] = owner

            if "email" in manager_data:

                try:
                    team_mapping[league_key + ".t." +
                                 team_id] = email_mapping[email]
                except:
                    print("\n{}, team {}, {}".format(nickname, team_id, email))
                    existing_nickname = False
                    while existing_nickname == False:
                        owner = input("Who's email is " + email + "?: ")
                        existing_nickname = owner in email_mapping.values()
                        if not existing_nickname:
                            print('That owner does not exist, try again.\n')

                    email_mapping[email] = owner

                    team_mapping[league_key + ".t." +
                                 team_id] = email_mapping[email]

    with open("./data/owner_info/email_mapping.json", 'w') as f:
        json.dump(email_mapping, f, indent=4)
    # with open("./teams/team_numbers_" + str(year) + ".txt", "w+") as outfile:
    #     json.dump(team_mapping, outfile, sort_keys=True)
    return team_mapping


def update_team_mapping(year):

    ids = get_manager_ids(year)

    with open("./data/owner_info/team_mapping.json") as f:
        team_mapping = json.load(f)

    team_mapping[year] = ids
    print(f'Writing team ids for {year}')
    with open("./data/owner_info/team_mapping.json", 'w') as f:
        json.dump(team_mapping, f)


if __name__ == '__main__':

    # for year in range(2006, 2020):

    update_team_mapping(2020)
