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


class InlineResponse20090OriginalValue(object):
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
        'profile': 'InlineResponse20090OriginalValueProfile'
    }

    attribute_map = {
        'profile': 'profile'
    }

    def __init__(self, profile=None):  # noqa: E501
        """InlineResponse20090OriginalValue - a model defined in Swagger"""  # noqa: E501
        self._profile = None
        self.discriminator = None
        if profile is not None:
            self.profile = profile

    @property
    def profile(self):
        """Gets the profile of this InlineResponse20090OriginalValue.  # noqa: E501


        :return: The profile of this InlineResponse20090OriginalValue.  # noqa: E501
        :rtype: InlineResponse20090OriginalValueProfile
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this InlineResponse20090OriginalValue.


        :param profile: The profile of this InlineResponse20090OriginalValue.  # noqa: E501
        :type: InlineResponse20090OriginalValueProfile
        """

        self._profile = profile

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
        if issubclass(InlineResponse20090OriginalValue, dict):
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
        if not isinstance(other, InlineResponse20090OriginalValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other