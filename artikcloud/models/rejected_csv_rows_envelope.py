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


class RejectedCSVRowsEnvelope(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, offset=None, count=None, total=None, data=None):
        """
        RejectedCSVRowsEnvelope - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'offset': 'int',
            'count': 'int',
            'total': 'int',
            'data': 'list[RejectedCSVRow]'
        }

        self.attribute_map = {
            'offset': 'offset',
            'count': 'count',
            'total': 'total',
            'data': 'data'
        }

        self._offset = offset
        self._count = count
        self._total = total
        self._data = data

    @property
    def offset(self):
        """
        Gets the offset of this RejectedCSVRowsEnvelope.
        Page starting position

        :return: The offset of this RejectedCSVRowsEnvelope.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """
        Sets the offset of this RejectedCSVRowsEnvelope.
        Page starting position

        :param offset: The offset of this RejectedCSVRowsEnvelope.
        :type: int
        """

        self._offset = offset

    @property
    def count(self):
        """
        Gets the count of this RejectedCSVRowsEnvelope.
        Page size

        :return: The count of this RejectedCSVRowsEnvelope.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this RejectedCSVRowsEnvelope.
        Page size

        :param count: The count of this RejectedCSVRowsEnvelope.
        :type: int
        """

        self._count = count

    @property
    def total(self):
        """
        Gets the total of this RejectedCSVRowsEnvelope.
        Total number or rejected rows

        :return: The total of this RejectedCSVRowsEnvelope.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """
        Sets the total of this RejectedCSVRowsEnvelope.
        Total number or rejected rows

        :param total: The total of this RejectedCSVRowsEnvelope.
        :type: int
        """

        self._total = total

    @property
    def data(self):
        """
        Gets the data of this RejectedCSVRowsEnvelope.
        Array of rejected rows

        :return: The data of this RejectedCSVRowsEnvelope.
        :rtype: list[RejectedCSVRow]
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this RejectedCSVRowsEnvelope.
        Array of rejected rows

        :param data: The data of this RejectedCSVRowsEnvelope.
        :type: list[RejectedCSVRow]
        """

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
        if not isinstance(other, RejectedCSVRowsEnvelope):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
