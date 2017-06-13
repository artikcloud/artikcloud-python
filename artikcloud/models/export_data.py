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


class ExportData(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, expiration_date=None, export_id=None, file_size=None, md5=None, request=None, status=None, total_messages=None):
        """
        ExportData - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'expiration_date': 'int',
            'export_id': 'str',
            'file_size': 'int',
            'md5': 'str',
            'request': 'ExportRequest',
            'status': 'str',
            'total_messages': 'int'
        }

        self.attribute_map = {
            'expiration_date': 'expirationDate',
            'export_id': 'exportId',
            'file_size': 'fileSize',
            'md5': 'md5',
            'request': 'request',
            'status': 'status',
            'total_messages': 'totalMessages'
        }

        self._expiration_date = expiration_date
        self._export_id = export_id
        self._file_size = file_size
        self._md5 = md5
        self._request = request
        self._status = status
        self._total_messages = total_messages

    @property
    def expiration_date(self):
        """
        Gets the expiration_date of this ExportData.

        :return: The expiration_date of this ExportData.
        :rtype: int
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """
        Sets the expiration_date of this ExportData.

        :param expiration_date: The expiration_date of this ExportData.
        :type: int
        """

        self._expiration_date = expiration_date

    @property
    def export_id(self):
        """
        Gets the export_id of this ExportData.

        :return: The export_id of this ExportData.
        :rtype: str
        """
        return self._export_id

    @export_id.setter
    def export_id(self, export_id):
        """
        Sets the export_id of this ExportData.

        :param export_id: The export_id of this ExportData.
        :type: str
        """

        self._export_id = export_id

    @property
    def file_size(self):
        """
        Gets the file_size of this ExportData.

        :return: The file_size of this ExportData.
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """
        Sets the file_size of this ExportData.

        :param file_size: The file_size of this ExportData.
        :type: int
        """

        self._file_size = file_size

    @property
    def md5(self):
        """
        Gets the md5 of this ExportData.

        :return: The md5 of this ExportData.
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        """
        Sets the md5 of this ExportData.

        :param md5: The md5 of this ExportData.
        :type: str
        """

        self._md5 = md5

    @property
    def request(self):
        """
        Gets the request of this ExportData.

        :return: The request of this ExportData.
        :rtype: ExportRequest
        """
        return self._request

    @request.setter
    def request(self, request):
        """
        Sets the request of this ExportData.

        :param request: The request of this ExportData.
        :type: ExportRequest
        """

        self._request = request

    @property
    def status(self):
        """
        Gets the status of this ExportData.
        Export status

        :return: The status of this ExportData.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ExportData.
        Export status

        :param status: The status of this ExportData.
        :type: str
        """

        self._status = status

    @property
    def total_messages(self):
        """
        Gets the total_messages of this ExportData.

        :return: The total_messages of this ExportData.
        :rtype: int
        """
        return self._total_messages

    @total_messages.setter
    def total_messages(self, total_messages):
        """
        Sets the total_messages of this ExportData.

        :param total_messages: The total_messages of this ExportData.
        :type: int
        """

        self._total_messages = total_messages

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
        if not isinstance(other, ExportData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
