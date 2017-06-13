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


class UnregisterDeviceResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, certificate_info=None, certificate_signature=None, created_on=None, dtid=None, eid=None, id=None, manifest_version=None, manifest_version_policy=None, name=None, need_provider_auth=None, uid=None):
        """
        UnregisterDeviceResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'certificate_info': 'str',
            'certificate_signature': 'str',
            'created_on': 'int',
            'dtid': 'str',
            'eid': 'str',
            'id': 'str',
            'manifest_version': 'int',
            'manifest_version_policy': 'str',
            'name': 'str',
            'need_provider_auth': 'bool',
            'uid': 'str'
        }

        self.attribute_map = {
            'certificate_info': 'certificateInfo',
            'certificate_signature': 'certificateSignature',
            'created_on': 'createdOn',
            'dtid': 'dtid',
            'eid': 'eid',
            'id': 'id',
            'manifest_version': 'manifestVersion',
            'manifest_version_policy': 'manifestVersionPolicy',
            'name': 'name',
            'need_provider_auth': 'needProviderAuth',
            'uid': 'uid'
        }

        self._certificate_info = certificate_info
        self._certificate_signature = certificate_signature
        self._created_on = created_on
        self._dtid = dtid
        self._eid = eid
        self._id = id
        self._manifest_version = manifest_version
        self._manifest_version_policy = manifest_version_policy
        self._name = name
        self._need_provider_auth = need_provider_auth
        self._uid = uid

    @property
    def certificate_info(self):
        """
        Gets the certificate_info of this UnregisterDeviceResponse.
        Device certificate information.

        :return: The certificate_info of this UnregisterDeviceResponse.
        :rtype: str
        """
        return self._certificate_info

    @certificate_info.setter
    def certificate_info(self, certificate_info):
        """
        Sets the certificate_info of this UnregisterDeviceResponse.
        Device certificate information.

        :param certificate_info: The certificate_info of this UnregisterDeviceResponse.
        :type: str
        """

        self._certificate_info = certificate_info

    @property
    def certificate_signature(self):
        """
        Gets the certificate_signature of this UnregisterDeviceResponse.
        Certificate's signature.

        :return: The certificate_signature of this UnregisterDeviceResponse.
        :rtype: str
        """
        return self._certificate_signature

    @certificate_signature.setter
    def certificate_signature(self, certificate_signature):
        """
        Sets the certificate_signature of this UnregisterDeviceResponse.
        Certificate's signature.

        :param certificate_signature: The certificate_signature of this UnregisterDeviceResponse.
        :type: str
        """

        self._certificate_signature = certificate_signature

    @property
    def created_on(self):
        """
        Gets the created_on of this UnregisterDeviceResponse.
        Device created on date.

        :return: The created_on of this UnregisterDeviceResponse.
        :rtype: int
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """
        Sets the created_on of this UnregisterDeviceResponse.
        Device created on date.

        :param created_on: The created_on of this UnregisterDeviceResponse.
        :type: int
        """

        self._created_on = created_on

    @property
    def dtid(self):
        """
        Gets the dtid of this UnregisterDeviceResponse.
        Device type id.

        :return: The dtid of this UnregisterDeviceResponse.
        :rtype: str
        """
        return self._dtid

    @dtid.setter
    def dtid(self, dtid):
        """
        Sets the dtid of this UnregisterDeviceResponse.
        Device type id.

        :param dtid: The dtid of this UnregisterDeviceResponse.
        :type: str
        """

        self._dtid = dtid

    @property
    def eid(self):
        """
        Gets the eid of this UnregisterDeviceResponse.
        External ID of the device.

        :return: The eid of this UnregisterDeviceResponse.
        :rtype: str
        """
        return self._eid

    @eid.setter
    def eid(self, eid):
        """
        Sets the eid of this UnregisterDeviceResponse.
        External ID of the device.

        :param eid: The eid of this UnregisterDeviceResponse.
        :type: str
        """

        self._eid = eid

    @property
    def id(self):
        """
        Gets the id of this UnregisterDeviceResponse.
        Device id.

        :return: The id of this UnregisterDeviceResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UnregisterDeviceResponse.
        Device id.

        :param id: The id of this UnregisterDeviceResponse.
        :type: str
        """

        self._id = id

    @property
    def manifest_version(self):
        """
        Gets the manifest_version of this UnregisterDeviceResponse.
        Device manifest version.

        :return: The manifest_version of this UnregisterDeviceResponse.
        :rtype: int
        """
        return self._manifest_version

    @manifest_version.setter
    def manifest_version(self, manifest_version):
        """
        Sets the manifest_version of this UnregisterDeviceResponse.
        Device manifest version.

        :param manifest_version: The manifest_version of this UnregisterDeviceResponse.
        :type: int
        """

        self._manifest_version = manifest_version

    @property
    def manifest_version_policy(self):
        """
        Gets the manifest_version_policy of this UnregisterDeviceResponse.
        Device manifest version policy.

        :return: The manifest_version_policy of this UnregisterDeviceResponse.
        :rtype: str
        """
        return self._manifest_version_policy

    @manifest_version_policy.setter
    def manifest_version_policy(self, manifest_version_policy):
        """
        Sets the manifest_version_policy of this UnregisterDeviceResponse.
        Device manifest version policy.

        :param manifest_version_policy: The manifest_version_policy of this UnregisterDeviceResponse.
        :type: str
        """

        self._manifest_version_policy = manifest_version_policy

    @property
    def name(self):
        """
        Gets the name of this UnregisterDeviceResponse.
        Device name.

        :return: The name of this UnregisterDeviceResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UnregisterDeviceResponse.
        Device name.

        :param name: The name of this UnregisterDeviceResponse.
        :type: str
        """

        self._name = name

    @property
    def need_provider_auth(self):
        """
        Gets the need_provider_auth of this UnregisterDeviceResponse.
        Device need provider auth.

        :return: The need_provider_auth of this UnregisterDeviceResponse.
        :rtype: bool
        """
        return self._need_provider_auth

    @need_provider_auth.setter
    def need_provider_auth(self, need_provider_auth):
        """
        Sets the need_provider_auth of this UnregisterDeviceResponse.
        Device need provider auth.

        :param need_provider_auth: The need_provider_auth of this UnregisterDeviceResponse.
        :type: bool
        """

        self._need_provider_auth = need_provider_auth

    @property
    def uid(self):
        """
        Gets the uid of this UnregisterDeviceResponse.
        User id.

        :return: The uid of this UnregisterDeviceResponse.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """
        Sets the uid of this UnregisterDeviceResponse.
        User id.

        :param uid: The uid of this UnregisterDeviceResponse.
        :type: str
        """

        self._uid = uid

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
        if not isinstance(other, UnregisterDeviceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
