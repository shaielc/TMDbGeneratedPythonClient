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


class InlineResponse20071CertificationsUS(object):
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
        'certification': 'str',
        'meaning': 'str',
        'order': 'int'
    }

    attribute_map = {
        'certification': 'certification',
        'meaning': 'meaning',
        'order': 'order'
    }

    def __init__(self, certification=None, meaning=None, order=None):  # noqa: E501
        """InlineResponse20071CertificationsUS - a model defined in Swagger"""  # noqa: E501
        self._certification = None
        self._meaning = None
        self._order = None
        self.discriminator = None
        if certification is not None:
            self.certification = certification
        if meaning is not None:
            self.meaning = meaning
        if order is not None:
            self.order = order

    @property
    def certification(self):
        """Gets the certification of this InlineResponse20071CertificationsUS.  # noqa: E501


        :return: The certification of this InlineResponse20071CertificationsUS.  # noqa: E501
        :rtype: str
        """
        return self._certification

    @certification.setter
    def certification(self, certification):
        """Sets the certification of this InlineResponse20071CertificationsUS.


        :param certification: The certification of this InlineResponse20071CertificationsUS.  # noqa: E501
        :type: str
        """

        self._certification = certification

    @property
    def meaning(self):
        """Gets the meaning of this InlineResponse20071CertificationsUS.  # noqa: E501


        :return: The meaning of this InlineResponse20071CertificationsUS.  # noqa: E501
        :rtype: str
        """
        return self._meaning

    @meaning.setter
    def meaning(self, meaning):
        """Sets the meaning of this InlineResponse20071CertificationsUS.


        :param meaning: The meaning of this InlineResponse20071CertificationsUS.  # noqa: E501
        :type: str
        """

        self._meaning = meaning

    @property
    def order(self):
        """Gets the order of this InlineResponse20071CertificationsUS.  # noqa: E501


        :return: The order of this InlineResponse20071CertificationsUS.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this InlineResponse20071CertificationsUS.


        :param order: The order of this InlineResponse20071CertificationsUS.  # noqa: E501
        :type: int
        """

        self._order = order

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
        if issubclass(InlineResponse20071CertificationsUS, dict):
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
        if not isinstance(other, InlineResponse20071CertificationsUS):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
