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


class InlineResponse20019Translations(object):
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
        'iso_3166_1': 'str',
        'iso_639_1': 'str',
        'name': 'str',
        'english_name': 'str',
        'data': 'InlineResponse20019Data'
    }

    attribute_map = {
        'iso_3166_1': 'iso_3166_1',
        'iso_639_1': 'iso_639_1',
        'name': 'name',
        'english_name': 'english_name',
        'data': 'data'
    }

    def __init__(self, iso_3166_1=None, iso_639_1=None, name=None, english_name=None, data=None):  # noqa: E501
        """InlineResponse20019Translations - a model defined in Swagger"""  # noqa: E501
        self._iso_3166_1 = None
        self._iso_639_1 = None
        self._name = None
        self._english_name = None
        self._data = None
        self.discriminator = None
        if iso_3166_1 is not None:
            self.iso_3166_1 = iso_3166_1
        if iso_639_1 is not None:
            self.iso_639_1 = iso_639_1
        if name is not None:
            self.name = name
        if english_name is not None:
            self.english_name = english_name
        if data is not None:
            self.data = data

    @property
    def iso_3166_1(self):
        """Gets the iso_3166_1 of this InlineResponse20019Translations.  # noqa: E501


        :return: The iso_3166_1 of this InlineResponse20019Translations.  # noqa: E501
        :rtype: str
        """
        return self._iso_3166_1

    @iso_3166_1.setter
    def iso_3166_1(self, iso_3166_1):
        """Sets the iso_3166_1 of this InlineResponse20019Translations.


        :param iso_3166_1: The iso_3166_1 of this InlineResponse20019Translations.  # noqa: E501
        :type: str
        """

        self._iso_3166_1 = iso_3166_1

    @property
    def iso_639_1(self):
        """Gets the iso_639_1 of this InlineResponse20019Translations.  # noqa: E501


        :return: The iso_639_1 of this InlineResponse20019Translations.  # noqa: E501
        :rtype: str
        """
        return self._iso_639_1

    @iso_639_1.setter
    def iso_639_1(self, iso_639_1):
        """Sets the iso_639_1 of this InlineResponse20019Translations.


        :param iso_639_1: The iso_639_1 of this InlineResponse20019Translations.  # noqa: E501
        :type: str
        """

        self._iso_639_1 = iso_639_1

    @property
    def name(self):
        """Gets the name of this InlineResponse20019Translations.  # noqa: E501


        :return: The name of this InlineResponse20019Translations.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse20019Translations.


        :param name: The name of this InlineResponse20019Translations.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def english_name(self):
        """Gets the english_name of this InlineResponse20019Translations.  # noqa: E501


        :return: The english_name of this InlineResponse20019Translations.  # noqa: E501
        :rtype: str
        """
        return self._english_name

    @english_name.setter
    def english_name(self, english_name):
        """Sets the english_name of this InlineResponse20019Translations.


        :param english_name: The english_name of this InlineResponse20019Translations.  # noqa: E501
        :type: str
        """

        self._english_name = english_name

    @property
    def data(self):
        """Gets the data of this InlineResponse20019Translations.  # noqa: E501


        :return: The data of this InlineResponse20019Translations.  # noqa: E501
        :rtype: InlineResponse20019Data
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this InlineResponse20019Translations.


        :param data: The data of this InlineResponse20019Translations.  # noqa: E501
        :type: InlineResponse20019Data
        """

        self._data = data

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
        if issubclass(InlineResponse20019Translations, dict):
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
        if not isinstance(other, InlineResponse20019Translations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
