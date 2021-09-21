# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.  # noqa: E501

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from docusign_esign.client.configuration import Configuration


class FeatureAvailableMetadata(object):
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
        'availabilty': 'str',
        'feature_name': 'str'
    }

    attribute_map = {
        'availabilty': 'availabilty',
        'feature_name': 'featureName'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """FeatureAvailableMetadata - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._availabilty = None
        self._feature_name = None
        self.discriminator = None

        setattr(self, "_{}".format('availabilty'), kwargs.get('availabilty', None))
        setattr(self, "_{}".format('feature_name'), kwargs.get('feature_name', None))

    @property
    def availabilty(self):
        """Gets the availabilty of this FeatureAvailableMetadata.  # noqa: E501

          # noqa: E501

        :return: The availabilty of this FeatureAvailableMetadata.  # noqa: E501
        :rtype: str
        """
        return self._availabilty

    @availabilty.setter
    def availabilty(self, availabilty):
        """Sets the availabilty of this FeatureAvailableMetadata.

          # noqa: E501

        :param availabilty: The availabilty of this FeatureAvailableMetadata.  # noqa: E501
        :type: str
        """

        self._availabilty = availabilty

    @property
    def feature_name(self):
        """Gets the feature_name of this FeatureAvailableMetadata.  # noqa: E501

          # noqa: E501

        :return: The feature_name of this FeatureAvailableMetadata.  # noqa: E501
        :rtype: str
        """
        return self._feature_name

    @feature_name.setter
    def feature_name(self, feature_name):
        """Sets the feature_name of this FeatureAvailableMetadata.

          # noqa: E501

        :param feature_name: The feature_name of this FeatureAvailableMetadata.  # noqa: E501
        :type: str
        """

        self._feature_name = feature_name

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
        if issubclass(FeatureAvailableMetadata, dict):
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
        if not isinstance(other, FeatureAvailableMetadata):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FeatureAvailableMetadata):
            return True

        return self.to_dict() != other.to_dict()