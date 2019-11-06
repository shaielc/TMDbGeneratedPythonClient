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


class InlineResponse20045Changes(object):
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
        'key': 'str',
        'items': 'list[InlineResponse20045Items]'
    }

    attribute_map = {
        'key': 'key',
        'items': 'items'
    }

    def __init__(self, key=None, items=None):  # noqa: E501
        """InlineResponse20045Changes - a model defined in Swagger"""  # noqa: E501
        self._key = None
        self._items = None
        self.discriminator = None
        if key is not None:
            self.key = key
        if items is not None:
            self.items = items

    @property
    def key(self):
        """Gets the key of this InlineResponse20045Changes.  # noqa: E501


        :return: The key of this InlineResponse20045Changes.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this InlineResponse20045Changes.


        :param key: The key of this InlineResponse20045Changes.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def items(self):
        """Gets the items of this InlineResponse20045Changes.  # noqa: E501


        :return: The items of this InlineResponse20045Changes.  # noqa: E501
        :rtype: list[InlineResponse20045Items]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this InlineResponse20045Changes.


        :param items: The items of this InlineResponse20045Changes.  # noqa: E501
        :type: list[InlineResponse20045Items]
        """

        self._items = items

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
        if issubclass(InlineResponse20045Changes, dict):
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
        if not isinstance(other, InlineResponse20045Changes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
