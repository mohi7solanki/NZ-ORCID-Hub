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


class Contributor(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, contributor_orcid=None, credit_name=None, contributor_email=None, contributor_attributes=None):
        """
        Contributor - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'contributor_orcid': 'ContributorOrcid',
            'credit_name': 'CreditName',
            'contributor_email': 'ContributorEmail',
            'contributor_attributes': 'ContributorAttributes'
        }

        self.attribute_map = {
            'contributor_orcid': 'contributor-orcid',
            'credit_name': 'credit-name',
            'contributor_email': 'contributor-email',
            'contributor_attributes': 'contributor-attributes'
        }

        self._contributor_orcid = contributor_orcid
        self._credit_name = credit_name
        self._contributor_email = contributor_email
        self._contributor_attributes = contributor_attributes

    @property
    def contributor_orcid(self):
        """
        Gets the contributor_orcid of this Contributor.

        :return: The contributor_orcid of this Contributor.
        :rtype: ContributorOrcid
        """
        return self._contributor_orcid

    @contributor_orcid.setter
    def contributor_orcid(self, contributor_orcid):
        """
        Sets the contributor_orcid of this Contributor.

        :param contributor_orcid: The contributor_orcid of this Contributor.
        :type: ContributorOrcid
        """

        self._contributor_orcid = contributor_orcid

    @property
    def credit_name(self):
        """
        Gets the credit_name of this Contributor.

        :return: The credit_name of this Contributor.
        :rtype: CreditName
        """
        return self._credit_name

    @credit_name.setter
    def credit_name(self, credit_name):
        """
        Sets the credit_name of this Contributor.

        :param credit_name: The credit_name of this Contributor.
        :type: CreditName
        """

        self._credit_name = credit_name

    @property
    def contributor_email(self):
        """
        Gets the contributor_email of this Contributor.

        :return: The contributor_email of this Contributor.
        :rtype: ContributorEmail
        """
        return self._contributor_email

    @contributor_email.setter
    def contributor_email(self, contributor_email):
        """
        Sets the contributor_email of this Contributor.

        :param contributor_email: The contributor_email of this Contributor.
        :type: ContributorEmail
        """

        self._contributor_email = contributor_email

    @property
    def contributor_attributes(self):
        """
        Gets the contributor_attributes of this Contributor.

        :return: The contributor_attributes of this Contributor.
        :rtype: ContributorAttributes
        """
        return self._contributor_attributes

    @contributor_attributes.setter
    def contributor_attributes(self, contributor_attributes):
        """
        Sets the contributor_attributes of this Contributor.

        :param contributor_attributes: The contributor_attributes of this Contributor.
        :type: ContributorAttributes
        """

        self._contributor_attributes = contributor_attributes

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
        if not isinstance(other, Contributor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
