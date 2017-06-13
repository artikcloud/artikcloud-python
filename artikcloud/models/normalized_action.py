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


class NormalizedAction(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, cts=None, ts=None, mid=None, sdid=None, ddid=None, ddtid=None, uid=None, mv=None, data=None):
        """
        NormalizedAction - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'cts': 'int',
            'ts': 'int',
            'mid': 'str',
            'sdid': 'str',
            'ddid': 'str',
            'ddtid': 'str',
            'uid': 'str',
            'mv': 'int',
            'data': 'ActionArray'
        }

        self.attribute_map = {
            'cts': 'cts',
            'ts': 'ts',
            'mid': 'mid',
            'sdid': 'sdid',
            'ddid': 'ddid',
            'ddtid': 'ddtid',
            'uid': 'uid',
            'mv': 'mv',
            'data': 'data'
        }

        self._cts = cts
        self._ts = ts
        self._mid = mid
        self._sdid = sdid
        self._ddid = ddid
        self._ddtid = ddtid
        self._uid = uid
        self._mv = mv
        self._data = data

    @property
    def cts(self):
        """
        Gets the cts of this NormalizedAction.

        :return: The cts of this NormalizedAction.
        :rtype: int
        """
        return self._cts

    @cts.setter
    def cts(self, cts):
        """
        Sets the cts of this NormalizedAction.

        :param cts: The cts of this NormalizedAction.
        :type: int
        """
        if cts is None:
            raise ValueError("Invalid value for `cts`, must not be `None`")

        self._cts = cts

    @property
    def ts(self):
        """
        Gets the ts of this NormalizedAction.

        :return: The ts of this NormalizedAction.
        :rtype: int
        """
        return self._ts

    @ts.setter
    def ts(self, ts):
        """
        Sets the ts of this NormalizedAction.

        :param ts: The ts of this NormalizedAction.
        :type: int
        """
        if ts is None:
            raise ValueError("Invalid value for `ts`, must not be `None`")

        self._ts = ts

    @property
    def mid(self):
        """
        Gets the mid of this NormalizedAction.

        :return: The mid of this NormalizedAction.
        :rtype: str
        """
        return self._mid

    @mid.setter
    def mid(self, mid):
        """
        Sets the mid of this NormalizedAction.

        :param mid: The mid of this NormalizedAction.
        :type: str
        """
        if mid is None:
            raise ValueError("Invalid value for `mid`, must not be `None`")

        self._mid = mid

    @property
    def sdid(self):
        """
        Gets the sdid of this NormalizedAction.

        :return: The sdid of this NormalizedAction.
        :rtype: str
        """
        return self._sdid

    @sdid.setter
    def sdid(self, sdid):
        """
        Sets the sdid of this NormalizedAction.

        :param sdid: The sdid of this NormalizedAction.
        :type: str
        """

        self._sdid = sdid

    @property
    def ddid(self):
        """
        Gets the ddid of this NormalizedAction.

        :return: The ddid of this NormalizedAction.
        :rtype: str
        """
        return self._ddid

    @ddid.setter
    def ddid(self, ddid):
        """
        Sets the ddid of this NormalizedAction.

        :param ddid: The ddid of this NormalizedAction.
        :type: str
        """
        if ddid is None:
            raise ValueError("Invalid value for `ddid`, must not be `None`")

        self._ddid = ddid

    @property
    def ddtid(self):
        """
        Gets the ddtid of this NormalizedAction.

        :return: The ddtid of this NormalizedAction.
        :rtype: str
        """
        return self._ddtid

    @ddtid.setter
    def ddtid(self, ddtid):
        """
        Sets the ddtid of this NormalizedAction.

        :param ddtid: The ddtid of this NormalizedAction.
        :type: str
        """
        if ddtid is None:
            raise ValueError("Invalid value for `ddtid`, must not be `None`")

        self._ddtid = ddtid

    @property
    def uid(self):
        """
        Gets the uid of this NormalizedAction.

        :return: The uid of this NormalizedAction.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """
        Sets the uid of this NormalizedAction.

        :param uid: The uid of this NormalizedAction.
        :type: str
        """
        if uid is None:
            raise ValueError("Invalid value for `uid`, must not be `None`")

        self._uid = uid

    @property
    def mv(self):
        """
        Gets the mv of this NormalizedAction.

        :return: The mv of this NormalizedAction.
        :rtype: int
        """
        return self._mv

    @mv.setter
    def mv(self, mv):
        """
        Sets the mv of this NormalizedAction.

        :param mv: The mv of this NormalizedAction.
        :type: int
        """
        if mv is None:
            raise ValueError("Invalid value for `mv`, must not be `None`")

        self._mv = mv

    @property
    def data(self):
        """
        Gets the data of this NormalizedAction.

        :return: The data of this NormalizedAction.
        :rtype: ActionArray
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this NormalizedAction.

        :param data: The data of this NormalizedAction.
        :type: ActionArray
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")

        self._data = data

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
        if not isinstance(other, NormalizedAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
