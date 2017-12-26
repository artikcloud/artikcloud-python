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


class CertificateFields(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, version=None, serial_number=None, signature_algorithm=None, subject=None, issuer=None, validity=None):
        """
        CertificateFields - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'version': 'int',
            'serial_number': 'str',
            'signature_algorithm': 'str',
            'subject': 'str',
            'issuer': 'str',
            'validity': 'ValidityPeriod'
        }

        self.attribute_map = {
            'version': 'version',
            'serial_number': 'serialNumber',
            'signature_algorithm': 'signatureAlgorithm',
            'subject': 'subject',
            'issuer': 'issuer',
            'validity': 'validity'
        }

        self._version = version
        self._serial_number = serial_number
        self._signature_algorithm = signature_algorithm
        self._subject = subject
        self._issuer = issuer
        self._validity = validity

    @property
    def version(self):
        """
        Gets the version of this CertificateFields.
        version

        :return: The version of this CertificateFields.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this CertificateFields.
        version

        :param version: The version of this CertificateFields.
        :type: int
        """

        self._version = version

    @property
    def serial_number(self):
        """
        Gets the serial_number of this CertificateFields.
        serialNumber

        :return: The serial_number of this CertificateFields.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """
        Sets the serial_number of this CertificateFields.
        serialNumber

        :param serial_number: The serial_number of this CertificateFields.
        :type: str
        """

        self._serial_number = serial_number

    @property
    def signature_algorithm(self):
        """
        Gets the signature_algorithm of this CertificateFields.
        signatureAlgorithm

        :return: The signature_algorithm of this CertificateFields.
        :rtype: str
        """
        return self._signature_algorithm

    @signature_algorithm.setter
    def signature_algorithm(self, signature_algorithm):
        """
        Sets the signature_algorithm of this CertificateFields.
        signatureAlgorithm

        :param signature_algorithm: The signature_algorithm of this CertificateFields.
        :type: str
        """

        self._signature_algorithm = signature_algorithm

    @property
    def subject(self):
        """
        Gets the subject of this CertificateFields.
        subject

        :return: The subject of this CertificateFields.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """
        Sets the subject of this CertificateFields.
        subject

        :param subject: The subject of this CertificateFields.
        :type: str
        """

        self._subject = subject

    @property
    def issuer(self):
        """
        Gets the issuer of this CertificateFields.
        issuer

        :return: The issuer of this CertificateFields.
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """
        Sets the issuer of this CertificateFields.
        issuer

        :param issuer: The issuer of this CertificateFields.
        :type: str
        """

        self._issuer = issuer

    @property
    def validity(self):
        """
        Gets the validity of this CertificateFields.

        :return: The validity of this CertificateFields.
        :rtype: ValidityPeriod
        """
        return self._validity

    @validity.setter
    def validity(self, validity):
        """
        Sets the validity of this CertificateFields.

        :param validity: The validity of this CertificateFields.
        :type: ValidityPeriod
        """

        self._validity = validity

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
        if not isinstance(other, CertificateFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other