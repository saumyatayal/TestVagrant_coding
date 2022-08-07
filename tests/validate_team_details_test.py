import pytest
import os
import json

from TestVagrant_coding.services.helper_functions.validation_helper import Validation_Helper

class Test_Team_Details():

    @pytest.fixture(autouse=True)
    def initialise_object(self):
        self.validation_helper = Validation_Helper()

    def read_json_file(self,json_file):
        config_file = os.path.join("TestVagrant_coding", "tests", "test_data", json_file)
        with open(config_file) as data_file:
            self.team_json_file = json.load(data_file)

    def test_validate_number_of_foreign_players(self):
        self.read_json_file("team_rcb.json")
        resp, err_msg = self.validation_helper.validate_number_foreign_players(team_data=self.team_json_file,
                                                                      no_of_foreign_players=4,
                                                                      home_country="India")
        assert resp,err_msg

    def test_number_of_wicket_keepers(self):
        self.read_json_file("team_rcb.json")
        resp, err_msg = self.validation_helper.validate_number_wicket_keepers(team_data=self.team_json_file,
                                                                               no_of_wicket_keepers=1)
        assert resp, err_msg
