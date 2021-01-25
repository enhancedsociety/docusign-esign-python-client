# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.  # noqa: E501

    OpenAPI spec version: v2
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DocumentUpdateInfo(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'data': 'str',
        'document_id': 'str',
        'document_security_store': 'DocumentSecurityStore',
        'name': 'str',
        'return_format': 'str',
        'signature_data_infos': 'list[SignatureDataInfo]',
        'time_stamp_field': 'TimeStampField'
    }

    attribute_map = {
        'data': 'data',
        'document_id': 'documentId',
        'document_security_store': 'documentSecurityStore',
        'name': 'name',
        'return_format': 'returnFormat',
        'signature_data_infos': 'signatureDataInfos',
        'time_stamp_field': 'timeStampField'
    }

    def __init__(self, data=None, document_id=None, document_security_store=None, name=None, return_format=None, signature_data_infos=None, time_stamp_field=None):  # noqa: E501
        """DocumentUpdateInfo - a model defined in Swagger"""  # noqa: E501

        self._data = None
        self._document_id = None
        self._document_security_store = None
        self._name = None
        self._return_format = None
        self._signature_data_infos = None
        self._time_stamp_field = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if document_id is not None:
            self.document_id = document_id
        if document_security_store is not None:
            self.document_security_store = document_security_store
        if name is not None:
            self.name = name
        if return_format is not None:
            self.return_format = return_format
        if signature_data_infos is not None:
            self.signature_data_infos = signature_data_infos
        if time_stamp_field is not None:
            self.time_stamp_field = time_stamp_field

    @property
    def data(self):
        """Gets the data of this DocumentUpdateInfo.  # noqa: E501

          # noqa: E501

        :return: The data of this DocumentUpdateInfo.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this DocumentUpdateInfo.

          # noqa: E501

        :param data: The data of this DocumentUpdateInfo.  # noqa: E501
        :type: str
        """

        self._data = data

    @property
    def document_id(self):
        """Gets the document_id of this DocumentUpdateInfo.  # noqa: E501

        Specifies the document ID number that the tab is placed on. This must refer to an existing Document's ID attribute.  # noqa: E501

        :return: The document_id of this DocumentUpdateInfo.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this DocumentUpdateInfo.

        Specifies the document ID number that the tab is placed on. This must refer to an existing Document's ID attribute.  # noqa: E501

        :param document_id: The document_id of this DocumentUpdateInfo.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def document_security_store(self):
        """Gets the document_security_store of this DocumentUpdateInfo.  # noqa: E501


        :return: The document_security_store of this DocumentUpdateInfo.  # noqa: E501
        :rtype: DocumentSecurityStore
        """
        return self._document_security_store

    @document_security_store.setter
    def document_security_store(self, document_security_store):
        """Sets the document_security_store of this DocumentUpdateInfo.


        :param document_security_store: The document_security_store of this DocumentUpdateInfo.  # noqa: E501
        :type: DocumentSecurityStore
        """

        self._document_security_store = document_security_store

    @property
    def name(self):
        """Gets the name of this DocumentUpdateInfo.  # noqa: E501

          # noqa: E501

        :return: The name of this DocumentUpdateInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DocumentUpdateInfo.

          # noqa: E501

        :param name: The name of this DocumentUpdateInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def return_format(self):
        """Gets the return_format of this DocumentUpdateInfo.  # noqa: E501

          # noqa: E501

        :return: The return_format of this DocumentUpdateInfo.  # noqa: E501
        :rtype: str
        """
        return self._return_format

    @return_format.setter
    def return_format(self, return_format):
        """Sets the return_format of this DocumentUpdateInfo.

          # noqa: E501

        :param return_format: The return_format of this DocumentUpdateInfo.  # noqa: E501
        :type: str
        """

        self._return_format = return_format

    @property
    def signature_data_infos(self):
        """Gets the signature_data_infos of this DocumentUpdateInfo.  # noqa: E501

          # noqa: E501

        :return: The signature_data_infos of this DocumentUpdateInfo.  # noqa: E501
        :rtype: list[SignatureDataInfo]
        """
        return self._signature_data_infos

    @signature_data_infos.setter
    def signature_data_infos(self, signature_data_infos):
        """Sets the signature_data_infos of this DocumentUpdateInfo.

          # noqa: E501

        :param signature_data_infos: The signature_data_infos of this DocumentUpdateInfo.  # noqa: E501
        :type: list[SignatureDataInfo]
        """

        self._signature_data_infos = signature_data_infos

    @property
    def time_stamp_field(self):
        """Gets the time_stamp_field of this DocumentUpdateInfo.  # noqa: E501


        :return: The time_stamp_field of this DocumentUpdateInfo.  # noqa: E501
        :rtype: TimeStampField
        """
        return self._time_stamp_field

    @time_stamp_field.setter
    def time_stamp_field(self, time_stamp_field):
        """Sets the time_stamp_field of this DocumentUpdateInfo.


        :param time_stamp_field: The time_stamp_field of this DocumentUpdateInfo.  # noqa: E501
        :type: TimeStampField
        """

        self._time_stamp_field = time_stamp_field

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(DocumentUpdateInfo, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DocumentUpdateInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
