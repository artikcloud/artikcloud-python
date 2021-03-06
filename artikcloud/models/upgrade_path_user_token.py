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


class UpgradePathUserToken(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, uid=None, access_token=None, did=None):
        """
        UpgradePathUserToken - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'uid': 'str',
            'access_token': 'str',
            'did': 'str'
        }

        self.attribute_map = {
            'uid': 'uid',
            'access_token': 'accessToken',
            'did': 'did'
        }

        self._uid = uid
        self._access_token = access_token
        self._did = did

    @property
    def uid(self):
        """
        Gets the uid of this UpgradePathUserToken.
        User ID

        :return: The uid of this UpgradePathUserToken.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """
        Sets the uid of this UpgradePathUserToken.
        User ID

        :param uid: The uid of this UpgradePathUserToken.
        :type: str
        """

        self._uid = uid

    @property
    def access_token(self):
        """
        Gets the access_token of this UpgradePathUserToken.
        User token from initial upgrade path request

        :return: The access_token of this UpgradePathUserToken.
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """
        Sets the access_token of this UpgradePathUserToken.
        User token from initial upgrade path request

        :param access_token: The access_token of this UpgradePathUserToken.
        :type: str
        """

        self._access_token = access_token

    @property
    def did(self):
        """
        Gets the did of this UpgradePathUserToken.
        Device ID

        :return: The did of this UpgradePathUserToken.
        :rtype: str
        """
        return self._did

    @did.setter
    def did(self, did):
        """
        Sets the did of this UpgradePathUserToken.
        Device ID

        :param did: The did of this UpgradePathUserToken.
        :type: str
        """

        self._did = did

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
        if not isinstance(other, UpgradePathUserToken):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
