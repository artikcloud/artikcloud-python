# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class ExportStatusResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ExportStatusResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'expiration_date': 'int',
            'export_id': 'str',
            'md5': 'str',
            'status': 'str',
            'ttl': 'str'
        }

        self.attribute_map = {
            'expiration_date': 'expirationDate',
            'export_id': 'exportId',
            'md5': 'md5',
            'status': 'status',
            'ttl': 'ttl'
        }

        self._expiration_date = None
        self._export_id = None
        self._md5 = None
        self._status = None
        self._ttl = None

    @property
    def expiration_date(self):
        """
        Gets the expiration_date of this ExportStatusResponse.


        :return: The expiration_date of this ExportStatusResponse.
        :rtype: int
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """
        Sets the expiration_date of this ExportStatusResponse.


        :param expiration_date: The expiration_date of this ExportStatusResponse.
        :type: int
        """
        self._expiration_date = expiration_date

    @property
    def export_id(self):
        """
        Gets the export_id of this ExportStatusResponse.


        :return: The export_id of this ExportStatusResponse.
        :rtype: str
        """
        return self._export_id

    @export_id.setter
    def export_id(self, export_id):
        """
        Sets the export_id of this ExportStatusResponse.


        :param export_id: The export_id of this ExportStatusResponse.
        :type: str
        """
        self._export_id = export_id

    @property
    def md5(self):
        """
        Gets the md5 of this ExportStatusResponse.


        :return: The md5 of this ExportStatusResponse.
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        """
        Sets the md5 of this ExportStatusResponse.


        :param md5: The md5 of this ExportStatusResponse.
        :type: str
        """
        self._md5 = md5

    @property
    def status(self):
        """
        Gets the status of this ExportStatusResponse.
        Export status

        :return: The status of this ExportStatusResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ExportStatusResponse.
        Export status

        :param status: The status of this ExportStatusResponse.
        :type: str
        """
        self._status = status

    @property
    def ttl(self):
        """
        Gets the ttl of this ExportStatusResponse.


        :return: The ttl of this ExportStatusResponse.
        :rtype: str
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """
        Sets the ttl of this ExportStatusResponse.


        :param ttl: The ttl of this ExportStatusResponse.
        :type: str
        """
        self._ttl = ttl

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
