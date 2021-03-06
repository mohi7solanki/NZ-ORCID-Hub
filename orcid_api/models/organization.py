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


class Organization(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, address=None, disambiguated_organization=None):
        """
        Organization - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'address': 'OrganizationAddress',
            'disambiguated_organization': 'DisambiguatedOrganization'
        }

        self.attribute_map = {
            'name': 'name',
            'address': 'address',
            'disambiguated_organization': 'disambiguated-organization'
        }

        self._name = name
        self._address = address
        self._disambiguated_organization = disambiguated_organization

    @property
    def name(self):
        """
        Gets the name of this Organization.

        :return: The name of this Organization.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Organization.

        :param name: The name of this Organization.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def address(self):
        """
        Gets the address of this Organization.

        :return: The address of this Organization.
        :rtype: OrganizationAddress
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this Organization.

        :param address: The address of this Organization.
        :type: OrganizationAddress
        """
        if address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")

        self._address = address

    @property
    def disambiguated_organization(self):
        """
        Gets the disambiguated_organization of this Organization.

        :return: The disambiguated_organization of this Organization.
        :rtype: DisambiguatedOrganization
        """
        return self._disambiguated_organization

    @disambiguated_organization.setter
    def disambiguated_organization(self, disambiguated_organization):
        """
        Sets the disambiguated_organization of this Organization.

        :param disambiguated_organization: The disambiguated_organization of this Organization.
        :type: DisambiguatedOrganization
        """

        self._disambiguated_organization = disambiguated_organization

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
        if not isinstance(other, Organization):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
