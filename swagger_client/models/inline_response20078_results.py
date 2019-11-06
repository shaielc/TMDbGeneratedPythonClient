# coding: utf-8

"""
    API

    ## Welcome  This is a place to put general notes and extra information, for internal use.  To get started designing/documenting this API, select a version on the left. # Title No Description  # noqa: E501

    OpenAPI spec version: 3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class InlineResponse20078Results(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'air_date': 'str',
        'episode_number': 'int',
        'id': 'int',
        'name': 'str',
        'overview': 'str',
        'production_code': 'str',
        'season_number': 'int',
        'show_id': 'int',
        'still_path': 'ImagePath',
        'vote_average': 'Object',
        'vote_count': 'int',
        'rating': 'Object'
    }

    attribute_map = {
        'air_date': 'air_date',
        'episode_number': 'episode_number',
        'id': 'id',
        'name': 'name',
        'overview': 'overview',
        'production_code': 'production_code',
        'season_number': 'season_number',
        'show_id': 'show_id',
        'still_path': 'still_path',
        'vote_average': 'vote_average',
        'vote_count': 'vote_count',
        'rating': 'rating'
    }

    def __init__(self, air_date=None, episode_number=None, id=None, name=None, overview=None, production_code=None, season_number=None, show_id=None, still_path=None, vote_average=None, vote_count=None, rating=None):  # noqa: E501
        """InlineResponse20078Results - a model defined in Swagger"""  # noqa: E501
        self._air_date = None
        self._episode_number = None
        self._id = None
        self._name = None
        self._overview = None
        self._production_code = None
        self._season_number = None
        self._show_id = None
        self._still_path = None
        self._vote_average = None
        self._vote_count = None
        self._rating = None
        self.discriminator = None
        if air_date is not None:
            self.air_date = air_date
        if episode_number is not None:
            self.episode_number = episode_number
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if overview is not None:
            self.overview = overview
        if production_code is not None:
            self.production_code = production_code
        if season_number is not None:
            self.season_number = season_number
        if show_id is not None:
            self.show_id = show_id
        if still_path is not None:
            self.still_path = still_path
        if vote_average is not None:
            self.vote_average = vote_average
        if vote_count is not None:
            self.vote_count = vote_count
        if rating is not None:
            self.rating = rating

    @property
    def air_date(self):
        """Gets the air_date of this InlineResponse20078Results.  # noqa: E501


        :return: The air_date of this InlineResponse20078Results.  # noqa: E501
        :rtype: str
        """
        return self._air_date

    @air_date.setter
    def air_date(self, air_date):
        """Sets the air_date of this InlineResponse20078Results.


        :param air_date: The air_date of this InlineResponse20078Results.  # noqa: E501
        :type: str
        """

        self._air_date = air_date

    @property
    def episode_number(self):
        """Gets the episode_number of this InlineResponse20078Results.  # noqa: E501


        :return: The episode_number of this InlineResponse20078Results.  # noqa: E501
        :rtype: int
        """
        return self._episode_number

    @episode_number.setter
    def episode_number(self, episode_number):
        """Sets the episode_number of this InlineResponse20078Results.


        :param episode_number: The episode_number of this InlineResponse20078Results.  # noqa: E501
        :type: int
        """

        self._episode_number = episode_number

    @property
    def id(self):
        """Gets the id of this InlineResponse20078Results.  # noqa: E501


        :return: The id of this InlineResponse20078Results.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20078Results.


        :param id: The id of this InlineResponse20078Results.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this InlineResponse20078Results.  # noqa: E501


        :return: The name of this InlineResponse20078Results.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse20078Results.


        :param name: The name of this InlineResponse20078Results.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def overview(self):
        """Gets the overview of this InlineResponse20078Results.  # noqa: E501


        :return: The overview of this InlineResponse20078Results.  # noqa: E501
        :rtype: str
        """
        return self._overview

    @overview.setter
    def overview(self, overview):
        """Sets the overview of this InlineResponse20078Results.


        :param overview: The overview of this InlineResponse20078Results.  # noqa: E501
        :type: str
        """

        self._overview = overview

    @property
    def production_code(self):
        """Gets the production_code of this InlineResponse20078Results.  # noqa: E501


        :return: The production_code of this InlineResponse20078Results.  # noqa: E501
        :rtype: str
        """
        return self._production_code

    @production_code.setter
    def production_code(self, production_code):
        """Sets the production_code of this InlineResponse20078Results.


        :param production_code: The production_code of this InlineResponse20078Results.  # noqa: E501
        :type: str
        """

        self._production_code = production_code

    @property
    def season_number(self):
        """Gets the season_number of this InlineResponse20078Results.  # noqa: E501


        :return: The season_number of this InlineResponse20078Results.  # noqa: E501
        :rtype: int
        """
        return self._season_number

    @season_number.setter
    def season_number(self, season_number):
        """Sets the season_number of this InlineResponse20078Results.


        :param season_number: The season_number of this InlineResponse20078Results.  # noqa: E501
        :type: int
        """

        self._season_number = season_number

    @property
    def show_id(self):
        """Gets the show_id of this InlineResponse20078Results.  # noqa: E501


        :return: The show_id of this InlineResponse20078Results.  # noqa: E501
        :rtype: int
        """
        return self._show_id

    @show_id.setter
    def show_id(self, show_id):
        """Sets the show_id of this InlineResponse20078Results.


        :param show_id: The show_id of this InlineResponse20078Results.  # noqa: E501
        :type: int
        """

        self._show_id = show_id

    @property
    def still_path(self):
        """Gets the still_path of this InlineResponse20078Results.  # noqa: E501


        :return: The still_path of this InlineResponse20078Results.  # noqa: E501
        :rtype: ImagePath
        """
        return self._still_path

    @still_path.setter
    def still_path(self, still_path):
        """Sets the still_path of this InlineResponse20078Results.


        :param still_path: The still_path of this InlineResponse20078Results.  # noqa: E501
        :type: ImagePath
        """

        self._still_path = still_path

    @property
    def vote_average(self):
        """Gets the vote_average of this InlineResponse20078Results.  # noqa: E501


        :return: The vote_average of this InlineResponse20078Results.  # noqa: E501
        :rtype: Object
        """
        return self._vote_average

    @vote_average.setter
    def vote_average(self, vote_average):
        """Sets the vote_average of this InlineResponse20078Results.


        :param vote_average: The vote_average of this InlineResponse20078Results.  # noqa: E501
        :type: Object
        """

        self._vote_average = vote_average

    @property
    def vote_count(self):
        """Gets the vote_count of this InlineResponse20078Results.  # noqa: E501


        :return: The vote_count of this InlineResponse20078Results.  # noqa: E501
        :rtype: int
        """
        return self._vote_count

    @vote_count.setter
    def vote_count(self, vote_count):
        """Sets the vote_count of this InlineResponse20078Results.


        :param vote_count: The vote_count of this InlineResponse20078Results.  # noqa: E501
        :type: int
        """

        self._vote_count = vote_count

    @property
    def rating(self):
        """Gets the rating of this InlineResponse20078Results.  # noqa: E501


        :return: The rating of this InlineResponse20078Results.  # noqa: E501
        :rtype: Object
        """
        return self._rating

    @rating.setter
    def rating(self, rating):
        """Sets the rating of this InlineResponse20078Results.


        :param rating: The rating of this InlineResponse20078Results.  # noqa: E501
        :type: Object
        """

        self._rating = rating

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(InlineResponse20078Results, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse20078Results):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
