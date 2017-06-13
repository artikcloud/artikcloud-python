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


class Token(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, access_token=None, expires_in=None, scope=None, token_type=None):
        """
        Token - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'access_token': 'str',
            'expires_in': 'int',
            'scope': 'str',
            'token_type': 'str'
        }

        self.attribute_map = {
            'access_token': 'access_token',
            'expires_in': 'expires_in',
            'scope': 'scope',
            'token_type': 'token_type'
        }

        self._access_token = access_token
        self._expires_in = expires_in
        self._scope = scope
        self._token_type = token_type

    @property
    def access_token(self):
        """
        Gets the access_token of this Token.

        :return: The access_token of this Token.
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """
        Sets the access_token of this Token.

        :param access_token: The access_token of this Token.
        :type: str
        """

        self._access_token = access_token

    @property
    def expires_in(self):
        """
        Gets the expires_in of this Token.

        :return: The expires_in of this Token.
        :rtype: int
        """
        return self._expires_in

    @expires_in.setter
    def expires_in(self, expires_in):
        """
        Sets the expires_in of this Token.

        :param expires_in: The expires_in of this Token.
        :type: int
        """

        self._expires_in = expires_in

    @property
    def scope(self):
        """
        Gets the scope of this Token.

        :return: The scope of this Token.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """
        Sets the scope of this Token.

        :param scope: The scope of this Token.
        :type: str
        """

        self._scope = scope

    @property
    def token_type(self):
        """
        Gets the token_type of this Token.

        :return: The token_type of this Token.
        :rtype: str
        """
        return self._token_type

    @token_type.setter
    def token_type(self, token_type):
        """
        Sets the token_type of this Token.

        :param token_type: The token_type of this Token.
        :type: str
        """

        self._token_type = token_type

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
        if not isinstance(other, Token):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
