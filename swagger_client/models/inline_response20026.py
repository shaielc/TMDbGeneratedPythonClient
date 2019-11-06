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


class InlineResponse20026(object):
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
        'cast': 'list[InlineResponse20026Cast]',
        'crew': 'list[InlineResponse20026Crew]',
        'guest_stars': 'list[InlineResponse20026GuestStars]',
        'id': 'int'
    }

    attribute_map = {
        'cast': 'cast',
        'crew': 'crew',
        'guest_stars': 'guest_stars',
        'id': 'id'
    }

    def __init__(self, cast=None, crew=None, guest_stars=None, id=None):  # noqa: E501
        """InlineResponse20026 - a model defined in Swagger"""  # noqa: E501
        self._cast = None
        self._crew = None
        self._guest_stars = None
        self._id = None
        self.discriminator = None
        if cast is not None:
            self.cast = cast
        if crew is not None:
            self.crew = crew
        if guest_stars is not None:
            self.guest_stars = guest_stars
        if id is not None:
            self.id = id

    @property
    def cast(self):
        """Gets the cast of this InlineResponse20026.  # noqa: E501


        :return: The cast of this InlineResponse20026.  # noqa: E501
        :rtype: list[InlineResponse20026Cast]
        """
        return self._cast

    @cast.setter
    def cast(self, cast):
        """Sets the cast of this InlineResponse20026.


        :param cast: The cast of this InlineResponse20026.  # noqa: E501
        :type: list[InlineResponse20026Cast]
        """

        self._cast = cast

    @property
    def crew(self):
        """Gets the crew of this InlineResponse20026.  # noqa: E501


        :return: The crew of this InlineResponse20026.  # noqa: E501
        :rtype: list[InlineResponse20026Crew]
        """
        return self._crew

    @crew.setter
    def crew(self, crew):
        """Sets the crew of this InlineResponse20026.


        :param crew: The crew of this InlineResponse20026.  # noqa: E501
        :type: list[InlineResponse20026Crew]
        """

        self._crew = crew

    @property
    def guest_stars(self):
        """Gets the guest_stars of this InlineResponse20026.  # noqa: E501


        :return: The guest_stars of this InlineResponse20026.  # noqa: E501
        :rtype: list[InlineResponse20026GuestStars]
        """
        return self._guest_stars

    @guest_stars.setter
    def guest_stars(self, guest_stars):
        """Sets the guest_stars of this InlineResponse20026.


        :param guest_stars: The guest_stars of this InlineResponse20026.  # noqa: E501
        :type: list[InlineResponse20026GuestStars]
        """

        self._guest_stars = guest_stars

    @property
    def id(self):
        """Gets the id of this InlineResponse20026.  # noqa: E501


        :return: The id of this InlineResponse20026.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20026.


        :param id: The id of this InlineResponse20026.  # noqa: E501
        :type: int
        """

        self._id = id

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
        if issubclass(InlineResponse20026, dict):
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
        if not isinstance(other, InlineResponse20026):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
