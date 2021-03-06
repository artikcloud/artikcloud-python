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


class Message(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, data=None, sdid=None, ts=None, type='message'):
        """
        Message - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'data': 'dict(str, object)',
            'sdid': 'str',
            'ts': 'int',
            'type': 'str'
        }

        self.attribute_map = {
            'data': 'data',
            'sdid': 'sdid',
            'ts': 'ts',
            'type': 'type'
        }

        self._data = data
        self._sdid = sdid
        self._ts = ts
        self._type = type

    @property
    def data(self):
        """
        Gets the data of this Message.

        :return: The data of this Message.
        :rtype: dict(str, object)
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this Message.

        :param data: The data of this Message.
        :type: dict(str, object)
        """

        self._data = data

    @property
    def sdid(self):
        """
        Gets the sdid of this Message.
        Source Device ID.

        :return: The sdid of this Message.
        :rtype: str
        """
        return self._sdid

    @sdid.setter
    def sdid(self, sdid):
        """
        Sets the sdid of this Message.
        Source Device ID.

        :param sdid: The sdid of this Message.
        :type: str
        """

        self._sdid = sdid

    @property
    def ts(self):
        """
        Gets the ts of this Message.
        Timestamp (past, present or future). Defaults to current time if not provided.

        :return: The ts of this Message.
        :rtype: int
        """
        return self._ts

    @ts.setter
    def ts(self, ts):
        """
        Sets the ts of this Message.
        Timestamp (past, present or future). Defaults to current time if not provided.

        :param ts: The ts of this Message.
        :type: int
        """

        self._ts = ts

    @property
    def type(self):
        """
        Gets the type of this Message.
        Type - message.

        :return: The type of this Message.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Message.
        Type - message.

        :param type: The type of this Message.
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
        if not isinstance(other, Message):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
