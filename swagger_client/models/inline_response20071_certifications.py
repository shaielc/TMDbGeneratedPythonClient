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


class InlineResponse20071Certifications(object):
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
        'us': 'list[InlineResponse20071CertificationsUS]',
        'ca': 'list[InlineResponse20071CertificationsUS]',
        'de': 'list[InlineResponse20071CertificationsUS]',
        'gb': 'list[InlineResponse20071CertificationsUS]',
        'au': 'list[InlineResponse20071CertificationsUS]',
        'br': 'list[InlineResponse20071CertificationsUS]',
        'fr': 'list[InlineResponse20071CertificationsUS]',
        'nz': 'list[InlineResponse20071CertificationsUS]',
        '_in': 'list[InlineResponse20071CertificationsUS]'
    }

    attribute_map = {
        'us': 'US',
        'ca': 'CA',
        'de': 'DE',
        'gb': 'GB',
        'au': 'AU',
        'br': 'BR',
        'fr': 'FR',
        'nz': 'NZ',
        '_in': 'IN'
    }

    def __init__(self, us=None, ca=None, de=None, gb=None, au=None, br=None, fr=None, nz=None, _in=None):  # noqa: E501
        """InlineResponse20071Certifications - a model defined in Swagger"""  # noqa: E501
        self._us = None
        self._ca = None
        self._de = None
        self._gb = None
        self._au = None
        self._br = None
        self._fr = None
        self._nz = None
        self.__in = None
        self.discriminator = None
        if us is not None:
            self.us = us
        if ca is not None:
            self.ca = ca
        if de is not None:
            self.de = de
        if gb is not None:
            self.gb = gb
        if au is not None:
            self.au = au
        if br is not None:
            self.br = br
        if fr is not None:
            self.fr = fr
        if nz is not None:
            self.nz = nz
        if _in is not None:
            self._in = _in

    @property
    def us(self):
        """Gets the us of this InlineResponse20071Certifications.  # noqa: E501


        :return: The us of this InlineResponse20071Certifications.  # noqa: E501
        :rtype: list[InlineResponse20071CertificationsUS]
        """
        return self._us

    @us.setter
    def us(self, us):
        """Sets the us of this InlineResponse20071Certifications.


        :param us: The us of this InlineResponse20071Certifications.  # noqa: E501
        :type: list[InlineResponse20071CertificationsUS]
        """

        self._us = us

    @property
    def ca(self):
        """Gets the ca of this InlineResponse20071Certifications.  # noqa: E501


        :return: The ca of this InlineResponse20071Certifications.  # noqa: E501
        :rtype: list[InlineResponse20071CertificationsUS]
        """
        return self._ca

    @ca.setter
    def ca(self, ca):
        """Sets the ca of this InlineResponse20071Certifications.


        :param ca: The ca of this InlineResponse20071Certifications.  # noqa: E501
        :type: list[InlineResponse20071CertificationsUS]
        """

        self._ca = ca

    @property
    def de(self):
        """Gets the de of this InlineResponse20071Certifications.  # noqa: E501


        :return: The de of this InlineResponse20071Certifications.  # noqa: E501
        :rtype: list[InlineResponse20071CertificationsUS]
        """
        return self._de

    @de.setter
    def de(self, de):
        """Sets the de of this InlineResponse20071Certifications.


        :param de: The de of this InlineResponse20071Certifications.  # noqa: E501
        :type: list[InlineResponse20071CertificationsUS]
        """

        self._de = de

    @property
    def gb(self):
        """Gets the gb of this InlineResponse20071Certifications.  # noqa: E501


        :return: The gb of this InlineResponse20071Certifications.  # noqa: E501
        :rtype: list[InlineResponse20071CertificationsUS]
        """
        return self._gb

    @gb.setter
    def gb(self, gb):
        """Sets the gb of this InlineResponse20071Certifications.


        :param gb: The gb of this InlineResponse20071Certifications.  # noqa: E501
        :type: list[InlineResponse20071CertificationsUS]
        """

        self._gb = gb

    @property
    def au(self):
        """Gets the au of this InlineResponse20071Certifications.  # noqa: E501


        :return: The au of this InlineResponse20071Certifications.  # noqa: E501
        :rtype: list[InlineResponse20071CertificationsUS]
        """
        return self._au

    @au.setter
    def au(self, au):
        """Sets the au of this InlineResponse20071Certifications.


        :param au: The au of this InlineResponse20071Certifications.  # noqa: E501
        :type: list[InlineResponse20071CertificationsUS]
        """

        self._au = au

    @property
    def br(self):
        """Gets the br of this InlineResponse20071Certifications.  # noqa: E501


        :return: The br of this InlineResponse20071Certifications.  # noqa: E501
        :rtype: list[InlineResponse20071CertificationsUS]
        """
        return self._br

    @br.setter
    def br(self, br):
        """Sets the br of this InlineResponse20071Certifications.


        :param br: The br of this InlineResponse20071Certifications.  # noqa: E501
        :type: list[InlineResponse20071CertificationsUS]
        """

        self._br = br

    @property
    def fr(self):
        """Gets the fr of this InlineResponse20071Certifications.  # noqa: E501


        :return: The fr of this InlineResponse20071Certifications.  # noqa: E501
        :rtype: list[InlineResponse20071CertificationsUS]
        """
        return self._fr

    @fr.setter
    def fr(self, fr):
        """Sets the fr of this InlineResponse20071Certifications.


        :param fr: The fr of this InlineResponse20071Certifications.  # noqa: E501
        :type: list[InlineResponse20071CertificationsUS]
        """

        self._fr = fr

    @property
    def nz(self):
        """Gets the nz of this InlineResponse20071Certifications.  # noqa: E501


        :return: The nz of this InlineResponse20071Certifications.  # noqa: E501
        :rtype: list[InlineResponse20071CertificationsUS]
        """
        return self._nz

    @nz.setter
    def nz(self, nz):
        """Sets the nz of this InlineResponse20071Certifications.


        :param nz: The nz of this InlineResponse20071Certifications.  # noqa: E501
        :type: list[InlineResponse20071CertificationsUS]
        """

        self._nz = nz

    @property
    def _in(self):
        """Gets the _in of this InlineResponse20071Certifications.  # noqa: E501


        :return: The _in of this InlineResponse20071Certifications.  # noqa: E501
        :rtype: list[InlineResponse20071CertificationsUS]
        """
        return self.__in

    @_in.setter
    def _in(self, _in):
        """Sets the _in of this InlineResponse20071Certifications.


        :param _in: The _in of this InlineResponse20071Certifications.  # noqa: E501
        :type: list[InlineResponse20071CertificationsUS]
        """

        self.__in = _in

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
        if issubclass(InlineResponse20071Certifications, dict):
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
        if not isinstance(other, InlineResponse20071Certifications):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
