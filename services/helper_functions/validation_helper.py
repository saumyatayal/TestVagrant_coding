
class Validation_Helper(object):

    def validate_number_foreign_players(self,team_data,no_of_foreign_players,home_country):
        if "player" in team_data.keys():
            no_of_players = self.number_players_other_than_country_given(team_data['player'],home_country)
            if no_of_players == no_of_foreign_players:
                return True, "team has exact " +str(no_of_foreign_players) + " foreign players"
            else:
                return False, "no of foreign players in team is: " +str(no_of_players)

        else:
            return False,"Player list not found in the given json"

    def number_players_other_than_country_given(self,players_data,home_country):
        no_of_players = 0
        for player_entry in players_data:
            if 'country' in player_entry:
                if player_entry['country'].lower() != home_country.lower():
                    no_of_players+=1

        return no_of_players
