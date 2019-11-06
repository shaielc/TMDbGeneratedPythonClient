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


class InlineResponse201(object):
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
        'status_message': 'str',
        'success': 'bool',
        'status_code': 'int',
        'list_id': 'int'
    }

    attribute_map = {
        'status_message': 'status_message',
        'success': 'success',
        'status_code': 'status_code',
        'list_id': 'list_id'
    }

    def __init__(self, status_message=None, success=None, status_code=None, list_id=None):  # noqa: E501
        """InlineResponse201 - a model defined in Swagger"""  # noqa: E501
        self._status_message = None
        self._success = None
        self._status_code = None
        self._list_id = None
        self.discriminator = None
        if status_message is not None:
            self.status_message = status_message
        if success is not None:
            self.success = success
        if status_code is not None:
            self.status_code = status_code
        if list_id is not None:
            self.list_id = list_id

    @property
    def status_message(self):
        """Gets the status_message of this InlineResponse201.  # noqa: E501


        :return: The status_message of this InlineResponse201.  # noqa: E501
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """Sets the status_message of this InlineResponse201.


        :param status_message: The status_message of this InlineResponse201.  # noqa: E501
        :type: str
        """

        self._status_message = status_message

    @property
    def success(self):
        """Gets the success of this InlineResponse201.  # noqa: E501


        :return: The success of this InlineResponse201.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this InlineResponse201.


        :param success: The success of this InlineResponse201.  # noqa: E501
        :type: bool
        """

        self._success = success

    @property
    def status_code(self):
        """Gets the status_code of this InlineResponse201.  # noqa: E501


        :return: The status_code of this InlineResponse201.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this InlineResponse201.


        :param status_code: The status_code of this InlineResponse201.  # noqa: E501
        :type: int
        """

        self._status_code = status_code

    @property
    def list_id(self):
        """Gets the list_id of this InlineResponse201.  # noqa: E501


        :return: The list_id of this InlineResponse201.  # noqa: E501
        :rtype: int
        """
        return self._list_id

    @list_id.setter
    def list_id(self, list_id):
        """Sets the list_id of this InlineResponse201.


        :param list_id: The list_id of this InlineResponse201.  # noqa: E501
        :type: int
        """

        self._list_id = list_id

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
        if issubclass(InlineResponse201, dict):
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
        if not isinstance(other, InlineResponse201):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
