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


class CertificateData(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, certificate_fields=None):
        """
        CertificateData - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'CertificateId',
            'certificate_fields': 'CertificateFields'
        }

        self.attribute_map = {
            'id': 'id',
            'certificate_fields': 'certificateFields'
        }

        self._id = id
        self._certificate_fields = certificate_fields

    @property
    def id(self):
        """
        Gets the id of this CertificateData.
        certificate id

        :return: The id of this CertificateData.
        :rtype: CertificateId
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CertificateData.
        certificate id

        :param id: The id of this CertificateData.
        :type: CertificateId
        """

        self._id = id

    @property
    def certificate_fields(self):
        """
        Gets the certificate_fields of this CertificateData.

        :return: The certificate_fields of this CertificateData.
        :rtype: CertificateFields
        """
        return self._certificate_fields

    @certificate_fields.setter
    def certificate_fields(self, certificate_fields):
        """
        Sets the certificate_fields of this CertificateData.

        :param certificate_fields: The certificate_fields of this CertificateData.
        :type: CertificateFields
        """

        self._certificate_fields = certificate_fields

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
        if not isinstance(other, CertificateData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
