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


class Actions(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, data=None, ddid=None, sdid=None, ts=None, type='action'):
        """
        Actions - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'data': 'ActionArray',
            'ddid': 'str',
            'sdid': 'str',
            'ts': 'int',
            'type': 'str'
        }

        self.attribute_map = {
            'data': 'data',
            'ddid': 'ddid',
            'sdid': 'sdid',
            'ts': 'ts',
            'type': 'type'
        }

        self._data = data
        self._ddid = ddid
        self._sdid = sdid
        self._ts = ts
        self._type = type

    @property
    def data(self):
        """
        Gets the data of this Actions.

        :return: The data of this Actions.
        :rtype: ActionArray
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this Actions.

        :param data: The data of this Actions.
        :type: ActionArray
        """

        self._data = data

    @property
    def ddid(self):
        """
        Gets the ddid of this Actions.
        Destination Device ID.

        :return: The ddid of this Actions.
        :rtype: str
        """
        return self._ddid

    @ddid.setter
    def ddid(self, ddid):
        """
        Sets the ddid of this Actions.
        Destination Device ID.

        :param ddid: The ddid of this Actions.
        :type: str
        """

        self._ddid = ddid

    @property
    def sdid(self):
        """
        Gets the sdid of this Actions.
        Destination Device ID.

        :return: The sdid of this Actions.
        :rtype: str
        """
        return self._sdid

    @sdid.setter
    def sdid(self, sdid):
        """
        Sets the sdid of this Actions.
        Destination Device ID.

        :param sdid: The sdid of this Actions.
        :type: str
        """

        self._sdid = sdid

    @property
    def ts(self):
        """
        Gets the ts of this Actions.
        Timestamp (past, present or future). Defaults to current time if not provided.

        :return: The ts of this Actions.
        :rtype: int
        """
        return self._ts

    @ts.setter
    def ts(self, ts):
        """
        Sets the ts of this Actions.
        Timestamp (past, present or future). Defaults to current time if not provided.

        :param ts: The ts of this Actions.
        :type: int
        """

        self._ts = ts

    @property
    def type(self):
        """
        Gets the type of this Actions.
        Type - action.

        :return: The type of this Actions.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Actions.
        Type - action.

        :param type: The type of this Actions.
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
        if not isinstance(other, Actions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
