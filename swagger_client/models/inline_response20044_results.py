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


class InlineResponse20044Results(object):
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
        'description': 'str',
        'episode_count': 'int',
        'group_count': 'int',
        'id': 'str',
        'name': 'str',
        'network': 'InlineResponse20044Network',
        'type': 'int'
    }

    attribute_map = {
        'description': 'description',
        'episode_count': 'episode_count',
        'group_count': 'group_count',
        'id': 'id',
        'name': 'name',
        'network': 'network',
        'type': 'type'
    }

    def __init__(self, description=None, episode_count=None, group_count=None, id=None, name=None, network=None, type=None):  # noqa: E501
        """InlineResponse20044Results - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._episode_count = None
        self._group_count = None
        self._id = None
        self._name = None
        self._network = None
        self._type = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if episode_count is not None:
            self.episode_count = episode_count
        if group_count is not None:
            self.group_count = group_count
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if network is not None:
            self.network = network
        if type is not None:
            self.type = type

    @property
    def description(self):
        """Gets the description of this InlineResponse20044Results.  # noqa: E501


        :return: The description of this InlineResponse20044Results.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InlineResponse20044Results.


        :param description: The description of this InlineResponse20044Results.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def episode_count(self):
        """Gets the episode_count of this InlineResponse20044Results.  # noqa: E501


        :return: The episode_count of this InlineResponse20044Results.  # noqa: E501
        :rtype: int
        """
        return self._episode_count

    @episode_count.setter
    def episode_count(self, episode_count):
        """Sets the episode_count of this InlineResponse20044Results.


        :param episode_count: The episode_count of this InlineResponse20044Results.  # noqa: E501
        :type: int
        """

        self._episode_count = episode_count

    @property
    def group_count(self):
        """Gets the group_count of this InlineResponse20044Results.  # noqa: E501


        :return: The group_count of this InlineResponse20044Results.  # noqa: E501
        :rtype: int
        """
        return self._group_count

    @group_count.setter
    def group_count(self, group_count):
        """Sets the group_count of this InlineResponse20044Results.


        :param group_count: The group_count of this InlineResponse20044Results.  # noqa: E501
        :type: int
        """

        self._group_count = group_count

    @property
    def id(self):
        """Gets the id of this InlineResponse20044Results.  # noqa: E501


        :return: The id of this InlineResponse20044Results.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20044Results.


        :param id: The id of this InlineResponse20044Results.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this InlineResponse20044Results.  # noqa: E501


        :return: The name of this InlineResponse20044Results.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse20044Results.


        :param name: The name of this InlineResponse20044Results.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def network(self):
        """Gets the network of this InlineResponse20044Results.  # noqa: E501


        :return: The network of this InlineResponse20044Results.  # noqa: E501
        :rtype: InlineResponse20044Network
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this InlineResponse20044Results.


        :param network: The network of this InlineResponse20044Results.  # noqa: E501
        :type: InlineResponse20044Network
        """

        self._network = network

    @property
    def type(self):
        """Gets the type of this InlineResponse20044Results.  # noqa: E501


        :return: The type of this InlineResponse20044Results.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineResponse20044Results.


        :param type: The type of this InlineResponse20044Results.  # noqa: E501
        :type: int
        """

        self._type = type

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
        if issubclass(InlineResponse20044Results, dict):
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
        if not isinstance(other, InlineResponse20044Results):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other