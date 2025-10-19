#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Handles Json data."""

import json
from pathlib import Path


class JSONFileHandler:
    """Handles writing user data to JSON file."""

    def __init__(self, file_path, dir_path="./pig_game/GameData"):
        """Initialize the object.

        :param file_path: File name, eg. '/file.json'.
        :type file_path: :py:obj:`str`
        :param dir_path: Directory path, eg. './pig_game/GameData'.
        :type dir_path: :py:obj:`str`
        """
        self.__file_path = Path(file_path)
        self.__dir_path = Path(dir_path)
        self.__dir_path.mkdir(parents=True, exist_ok=True)

    def is_missing_or_empty(self):
        """Check for missing file or invalid content.

        :return: If json file exists.
        :rtype: :py:obj:`bool`
        """
        missing_file = not self.__file_path.exists()
        if not missing_file:
            empty_file = self.__file_path.stat().st_size == 0
        else:
            empty_file = True
        if missing_file or empty_file:
            self.write({})
            return True
        return False

    def write(self, data):
        """Write user data to file.

        :param data: JSON data to be written.
        :type data: :py:obj:`dict`
        """
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def read(self):
        """Read user data file and returns.

        :return: Parsed JSON data.
        :rtype: :py:obj:`dict`
        :raises OSError: If the file is missing or unreadable.
        :raises json.JSONDecodeError: If the file contains invalid JSON.
        """
        self.is_missing_or_empty()
        with open(self.__file_path, "r", encoding="utf-8") as f:
            return json.load(f)
