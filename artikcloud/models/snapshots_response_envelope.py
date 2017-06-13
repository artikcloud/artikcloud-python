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


class SnapshotsResponseEnvelope(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, data=None, sdid=None):
        """
        SnapshotsResponseEnvelope - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'data': 'SnapshotResponses',
            'sdid': 'str'
        }

        self.attribute_map = {
            'data': 'data',
            'sdid': 'sdid'
        }

        self._data = data
        self._sdid = sdid

    @property
    def data(self):
        """
        Gets the data of this SnapshotsResponseEnvelope.

        :return: The data of this SnapshotsResponseEnvelope.
        :rtype: SnapshotResponses
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this SnapshotsResponseEnvelope.

        :param data: The data of this SnapshotsResponseEnvelope.
        :type: SnapshotResponses
        """

        self._data = data

    @property
    def sdid(self):
        """
        Gets the sdid of this SnapshotsResponseEnvelope.

        :return: The sdid of this SnapshotsResponseEnvelope.
        :rtype: str
        """
        return self._sdid

    @sdid.setter
    def sdid(self, sdid):
        """
        Sets the sdid of this SnapshotsResponseEnvelope.

        :param sdid: The sdid of this SnapshotsResponseEnvelope.
        :type: str
        """

        self._sdid = sdid

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
        if not isinstance(other, SnapshotsResponseEnvelope):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
