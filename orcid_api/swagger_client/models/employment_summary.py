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


class EmploymentSummary(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, created_date=None, last_modified_date=None, source=None, department_name=None, role_title=None, start_date=None, end_date=None, organization=None, visibility=None, put_code=None, path=None):
        """
        EmploymentSummary - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'created_date': 'CreatedDate',
            'last_modified_date': 'LastModifiedDate',
            'source': 'Source',
            'department_name': 'str',
            'role_title': 'str',
            'start_date': 'FuzzyDate',
            'end_date': 'FuzzyDate',
            'organization': 'Organization',
            'visibility': 'str',
            'put_code': 'int',
            'path': 'str'
        }

        self.attribute_map = {
            'created_date': 'created-date',
            'last_modified_date': 'last-modified-date',
            'source': 'source',
            'department_name': 'department-name',
            'role_title': 'role-title',
            'start_date': 'start-date',
            'end_date': 'end-date',
            'organization': 'organization',
            'visibility': 'visibility',
            'put_code': 'put-code',
            'path': 'path'
        }

        self._created_date = created_date
        self._last_modified_date = last_modified_date
        self._source = source
        self._department_name = department_name
        self._role_title = role_title
        self._start_date = start_date
        self._end_date = end_date
        self._organization = organization
        self._visibility = visibility
        self._put_code = put_code
        self._path = path

    @property
    def created_date(self):
        """
        Gets the created_date of this EmploymentSummary.

        :return: The created_date of this EmploymentSummary.
        :rtype: CreatedDate
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """
        Sets the created_date of this EmploymentSummary.

        :param created_date: The created_date of this EmploymentSummary.
        :type: CreatedDate
        """

        self._created_date = created_date

    @property
    def last_modified_date(self):
        """
        Gets the last_modified_date of this EmploymentSummary.

        :return: The last_modified_date of this EmploymentSummary.
        :rtype: LastModifiedDate
        """
        return self._last_modified_date

    @last_modified_date.setter
    def last_modified_date(self, last_modified_date):
        """
        Sets the last_modified_date of this EmploymentSummary.

        :param last_modified_date: The last_modified_date of this EmploymentSummary.
        :type: LastModifiedDate
        """

        self._last_modified_date = last_modified_date

    @property
    def source(self):
        """
        Gets the source of this EmploymentSummary.

        :return: The source of this EmploymentSummary.
        :rtype: Source
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this EmploymentSummary.

        :param source: The source of this EmploymentSummary.
        :type: Source
        """

        self._source = source

    @property
    def department_name(self):
        """
        Gets the department_name of this EmploymentSummary.

        :return: The department_name of this EmploymentSummary.
        :rtype: str
        """
        return self._department_name

    @department_name.setter
    def department_name(self, department_name):
        """
        Sets the department_name of this EmploymentSummary.

        :param department_name: The department_name of this EmploymentSummary.
        :type: str
        """

        self._department_name = department_name

    @property
    def role_title(self):
        """
        Gets the role_title of this EmploymentSummary.

        :return: The role_title of this EmploymentSummary.
        :rtype: str
        """
        return self._role_title

    @role_title.setter
    def role_title(self, role_title):
        """
        Sets the role_title of this EmploymentSummary.

        :param role_title: The role_title of this EmploymentSummary.
        :type: str
        """

        self._role_title = role_title

    @property
    def start_date(self):
        """
        Gets the start_date of this EmploymentSummary.

        :return: The start_date of this EmploymentSummary.
        :rtype: FuzzyDate
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this EmploymentSummary.

        :param start_date: The start_date of this EmploymentSummary.
        :type: FuzzyDate
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """
        Gets the end_date of this EmploymentSummary.

        :return: The end_date of this EmploymentSummary.
        :rtype: FuzzyDate
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """
        Sets the end_date of this EmploymentSummary.

        :param end_date: The end_date of this EmploymentSummary.
        :type: FuzzyDate
        """

        self._end_date = end_date

    @property
    def organization(self):
        """
        Gets the organization of this EmploymentSummary.

        :return: The organization of this EmploymentSummary.
        :rtype: Organization
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """
        Sets the organization of this EmploymentSummary.

        :param organization: The organization of this EmploymentSummary.
        :type: Organization
        """

        self._organization = organization

    @property
    def visibility(self):
        """
        Gets the visibility of this EmploymentSummary.

        :return: The visibility of this EmploymentSummary.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """
        Sets the visibility of this EmploymentSummary.

        :param visibility: The visibility of this EmploymentSummary.
        :type: str
        """
        allowed_values = ["SYSTEM", "PRIVATE", "LIMITED", "REGISTERED_ONLY", "PUBLIC", "PRIVATE"]
        if visibility not in allowed_values:
            raise ValueError(
                "Invalid value for `visibility` ({0}), must be one of {1}"
                .format(visibility, allowed_values)
            )

        self._visibility = visibility

    @property
    def put_code(self):
        """
        Gets the put_code of this EmploymentSummary.

        :return: The put_code of this EmploymentSummary.
        :rtype: int
        """
        return self._put_code

    @put_code.setter
    def put_code(self, put_code):
        """
        Sets the put_code of this EmploymentSummary.

        :param put_code: The put_code of this EmploymentSummary.
        :type: int
        """

        self._put_code = put_code

    @property
    def path(self):
        """
        Gets the path of this EmploymentSummary.

        :return: The path of this EmploymentSummary.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this EmploymentSummary.

        :param path: The path of this EmploymentSummary.
        :type: str
        """

        self._path = path

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
        if not isinstance(other, EmploymentSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
