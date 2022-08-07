
class Validation_Helper(object):

    def validate_number_foreign_players(self,team_data,no_of_foreign_players,home_country):
        '''
        function to verify number of foreign players in data
        :param team_data: team data in json format
        :param no_of_foreign_players: no of foreign players to check in the given team json
        :param home_country: home country which decides player is foreign or not
        :return: True if exact no of foreign players exist, False otherwise
        '''
        if "player" in team_data.keys():
            no_of_players = self.number_players_other_than_country_given(team_data['player'],home_country)
            if no_of_players == no_of_foreign_players:
                return True, "team has exact " +str(no_of_foreign_players) + " foreign players"
            else:
                return False, "no of foreign players in team is: " +str(no_of_players)

        else:
            return False,"Player list not found in the given json"

    def number_players_other_than_country_given(self,players_data,home_country):
        '''
        helper function to count no of players which are not from home country
        :param players_data: list of player data
        :param home_country: home country which decides player is foreign or not
        :return: no of players which do not belong to home country
        '''
        no_of_players = 0
        for player_entry in players_data:
            if 'country' in player_entry:
                if player_entry['country'].lower() != home_country.lower():
                    no_of_players+=1

        return no_of_players

    def validate_number_wicket_keepers(self,team_data,no_of_wicket_keepers):
        '''
        function to verify number of wicket keepers in data
        :param team_data: team data in json format
        :param no_of_wicket_keepers: no of wicket keepers to check in the given team json
        :return: True if atleast given no of wicket keepers exist, False otherwise
        '''
        if "player" in team_data.keys():
            no_of_players = self.number_of_players_with_given_role(team_data['player'],"Wicket-keeper")
            if no_of_players >= no_of_wicket_keepers:
                return True, "team has atleast " +str(no_of_wicket_keepers) + " wicket keepers"
            else:
                return False, "no of wicket keepers in team is: " +str(no_of_players)
        else:
            return False, "Player list not found in the given json"

    def number_of_players_with_given_role(self,players_data,player_role):
        '''
        helper function to count no of players with a given role
        :param players_data: list of player data
        :param player_role: role for which counting players
        :return: no of players with a given role
        '''
        no_of_players = 0
        for player_entry in players_data:
            if 'role' in player_entry:
                if player_entry['role'].lower() == player_role.lower():
                    no_of_players+=1

        return no_of_players