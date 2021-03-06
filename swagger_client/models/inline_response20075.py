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


class InlineResponse20075(object):
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
        'results': 'list[InlineResponse20075Results]'
    }

    attribute_map = {
        'id': 'id',
        'results': 'results'
    }

    def __init__(self, id=None, results=None):  # noqa: E501
        """InlineResponse20075 - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._results = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if results is not None:
            self.results = results

    @property
    def id(self):
        """Gets the id of this InlineResponse20075.  # noqa: E501


        :return: The id of this InlineResponse20075.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20075.


        :param id: The id of this InlineResponse20075.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def results(self):
        """Gets the results of this InlineResponse20075.  # noqa: E501


        :return: The results of this InlineResponse20075.  # noqa: E501
        :rtype: list[InlineResponse20075Results]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this InlineResponse20075.


        :param results: The results of this InlineResponse20075.  # noqa: E501
        :type: list[InlineResponse20075Results]
        """

        self._results = results

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
        if issubclass(InlineResponse20075, dict):
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
        if not isinstance(other, InlineResponse20075):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
