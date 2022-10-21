# cfw
# 2022.6.25

import json


class Config:
    def __init__(self, conf_filepath) -> None:
        self.conf_filepath = conf_filepath
        with open(self.conf_filepath, "r", encoding="utf-8") as f:
            self.confdata_dict: dict = json.load(f)

    def get_config_dict(self) -> dict:
        return self.confdata_dict

    def save_config(self, key_str: str, value):
        if key_str in self.confdata_dict:
            self.confdata_dict[key_str] = value
        with open(self.conf_filepath, "w", encoding="utf-8") as f:
            json.dump(self.confdata_dict, f, ensure_ascii=False)


class UserData:
    def __init__(self, data_filepath) -> None:
        self.data_filepath = data_filepath
        with open(self.data_filepath, "r", encoding="utf-8") as f:
            self._userdata_dict: dict = json.load(f)

    def get_gamename_list(self) -> list[str]:
        gamename_list = []
        for i in self._userdata_dict.keys():
            gamename_list.append(i)
        return gamename_list

    def get_savedata_sync_info(self, game_name: str) -> dict:
        """give arg "game name" return the game savedata sync info."""
        if game_name in self._userdata_dict:
            return self._userdata_dict[game_name]

    def get_game_name_sort_dict(self) -> dict:
        pass

    def save_sync_info(self, game_name: str, key: str, value: str):
        if game_name in self._userdata_dict:
            game_data = self._userdata_dict[game_name]
            game_data[key] = value
            with open(self.data_filepath, "w", encoding="utf-8") as f:
                json.dump(self._userdata_dict, f, ensure_ascii=False)

    def check_game_name(self, game_name: str):
        """check game name can use"""
        if game_name in self._userdata_dict:
            return False
        else:
            return True

    def create_sync_info(self, game_name: str, sync_info_dict: dict):
        """when create new game savedata sync then use tihs func"""
        self._userdata_dict[game_name] = sync_info_dict
        with open(self.data_filepath, "w", encoding="utf-8") as f:
            json.dump(self._userdata_dict, f, ensure_ascii=False)

    def del_game(self, game_name: str):
        self._userdata_dict.pop(game_name)
        with open(self.data_filepath, "w", encoding="utf-8") as f:
            json.dump(self._userdata_dict, f, ensure_ascii=False)

    def sort_game(self):
        a1 = sorted(self._userdata_dict.items(), key=lambda x: x[0])
        self._userdata_dict = dict(a1)
        with open(self.data_filepath, "w", encoding="utf-8") as f:
            json.dump(self._userdata_dict, f, ensure_ascii=False)
