# coding: utf-8

"""
    ORCID Member

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: Latest
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Citation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, citation_type=None, citation_value=None):
        """
        Citation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'citation_type': 'str',
            'citation_value': 'str'
        }

        self.attribute_map = {
            'citation_type': 'citation-type',
            'citation_value': 'citation-value'
        }

        self._citation_type = citation_type
        self._citation_value = citation_value

    @property
    def citation_type(self):
        """
        Gets the citation_type of this Citation.

        :return: The citation_type of this Citation.
        :rtype: str
        """
        return self._citation_type

    @citation_type.setter
    def citation_type(self, citation_type):
        """
        Sets the citation_type of this Citation.

        :param citation_type: The citation_type of this Citation.
        :type: str
        """
        allowed_values = ["FORMATTED_UNSPECIFIED", "BIBTEX", "FORMATTED_APA", "FORMATTED_HARVARD", "FORMATTED_IEEE", "FORMATTED_MLA", "FORMATTED_VANCOUVER", "FORMATTED_CHICAGO", "RIS"]
        if citation_type not in allowed_values:
            raise ValueError(
                "Invalid value for `citation_type` ({0}), must be one of {1}"
                .format(citation_type, allowed_values)
            )

        self._citation_type = citation_type

    @property
    def citation_value(self):
        """
        Gets the citation_value of this Citation.

        :return: The citation_value of this Citation.
        :rtype: str
        """
        return self._citation_value

    @citation_value.setter
    def citation_value(self, citation_value):
        """
        Sets the citation_value of this Citation.

        :param citation_value: The citation_value of this Citation.
        :type: str
        """
        if citation_value is None:
            raise ValueError("Invalid value for `citation_value`, must not be `None`")

        self._citation_value = citation_value

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
        if not isinstance(other, Citation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
