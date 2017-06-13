# coding: utf-8

"""
    ARTIK Cloud API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class RegisterMessage(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, cid=None, authorization=None, sdid=None, ts=None, type='register'):
        """
        RegisterMessage - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'cid': 'str',
            'authorization': 'str',
            'sdid': 'str',
            'ts': 'int',
            'type': 'str'
        }

        self.attribute_map = {
            'cid': 'cid',
            'authorization': 'authorization',
            'sdid': 'sdid',
            'ts': 'ts',
            'type': 'type'
        }

        self._cid = cid
        self._authorization = authorization
        self._sdid = sdid
        self._ts = ts
        self._type = type

    @property
    def cid(self):
        """
        Gets the cid of this RegisterMessage.
        Confirmation ID.

        :return: The cid of this RegisterMessage.
        :rtype: str
        """
        return self._cid

    @cid.setter
    def cid(self, cid):
        """
        Sets the cid of this RegisterMessage.
        Confirmation ID.

        :param cid: The cid of this RegisterMessage.
        :type: str
        """

        self._cid = cid

    @property
    def authorization(self):
        """
        Gets the authorization of this RegisterMessage.
        Authorization header containing access token (Bearer <access_token>).

        :return: The authorization of this RegisterMessage.
        :rtype: str
        """
        return self._authorization

    @authorization.setter
    def authorization(self, authorization):
        """
        Sets the authorization of this RegisterMessage.
        Authorization header containing access token (Bearer <access_token>).

        :param authorization: The authorization of this RegisterMessage.
        :type: str
        """

        self._authorization = authorization

    @property
    def sdid(self):
        """
        Gets the sdid of this RegisterMessage.
        Source Device ID.

        :return: The sdid of this RegisterMessage.
        :rtype: str
        """
        return self._sdid

    @sdid.setter
    def sdid(self, sdid):
        """
        Sets the sdid of this RegisterMessage.
        Source Device ID.

        :param sdid: The sdid of this RegisterMessage.
        :type: str
        """

        self._sdid = sdid

    @property
    def ts(self):
        """
        Gets the ts of this RegisterMessage.
        Timestamp (past, present or future). Defaults to current time if not provided.

        :return: The ts of this RegisterMessage.
        :rtype: int
        """
        return self._ts

    @ts.setter
    def ts(self, ts):
        """
        Sets the ts of this RegisterMessage.
        Timestamp (past, present or future). Defaults to current time if not provided.

        :param ts: The ts of this RegisterMessage.
        :type: int
        """

        self._ts = ts

    @property
    def type(self):
        """
        Gets the type of this RegisterMessage.
        Type.

        :return: The type of this RegisterMessage.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this RegisterMessage.
        Type.

        :param type: The type of this RegisterMessage.
        :type: str
        """

        self._type = type

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, RegisterMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
