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


class InlineResponse20074Network(object):
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
        'id': 'int',
        'logo_path': 'ImagePath',
        'name': 'str',
        'origin_country': 'str'
    }

    attribute_map = {
        'id': 'id',
        'logo_path': 'logo_path',
        'name': 'name',
        'origin_country': 'origin_country'
    }

    def __init__(self, id=None, logo_path=None, name=None, origin_country=None):  # noqa: E501
        """InlineResponse20074Network - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._logo_path = None
        self._name = None
        self._origin_country = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if logo_path is not None:
            self.logo_path = logo_path
        if name is not None:
            self.name = name
        if origin_country is not None:
            self.origin_country = origin_country

    @property
    def id(self):
        """Gets the id of this InlineResponse20074Network.  # noqa: E501


        :return: The id of this InlineResponse20074Network.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20074Network.


        :param id: The id of this InlineResponse20074Network.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def logo_path(self):
        """Gets the logo_path of this InlineResponse20074Network.  # noqa: E501


        :return: The logo_path of this InlineResponse20074Network.  # noqa: E501
        :rtype: ImagePath
        """
        return self._logo_path

    @logo_path.setter
    def logo_path(self, logo_path):
        """Sets the logo_path of this InlineResponse20074Network.


        :param logo_path: The logo_path of this InlineResponse20074Network.  # noqa: E501
        :type: ImagePath
        """

        self._logo_path = logo_path

    @property
    def name(self):
        """Gets the name of this InlineResponse20074Network.  # noqa: E501


        :return: The name of this InlineResponse20074Network.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse20074Network.


        :param name: The name of this InlineResponse20074Network.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def origin_country(self):
        """Gets the origin_country of this InlineResponse20074Network.  # noqa: E501


        :return: The origin_country of this InlineResponse20074Network.  # noqa: E501
        :rtype: str
        """
        return self._origin_country

    @origin_country.setter
    def origin_country(self, origin_country):
        """Sets the origin_country of this InlineResponse20074Network.


        :param origin_country: The origin_country of this InlineResponse20074Network.  # noqa: E501
        :type: str
        """

        self._origin_country = origin_country

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
        if issubclass(InlineResponse20074Network, dict):
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
        if not isinstance(other, InlineResponse20074Network):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
