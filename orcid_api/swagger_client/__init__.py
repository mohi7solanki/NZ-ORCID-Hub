# coding: utf-8

"""
    ORCID Member

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: Latest
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into sdk package
from .models.activities_summary import ActivitiesSummary
from .models.address import Address
from .models.amount import Amount
from .models.authorization_url import AuthorizationUrl
from .models.bulk_element import BulkElement
from .models.citation import Citation
from .models.contributor import Contributor
from .models.contributor_attributes import ContributorAttributes
from .models.contributor_email import ContributorEmail
from .models.contributor_orcid import ContributorOrcid
from .models.country import Country
from .models.created_date import CreatedDate
from .models.credit_name import CreditName
from .models.day import Day
from .models.disambiguated_organization import DisambiguatedOrganization
from .models.education import Education
from .models.education_summary import EducationSummary
from .models.educations import Educations
from .models.employment import Employment
from .models.employment_summary import EmploymentSummary
from .models.employments import Employments
from .models.external_id import ExternalID
from .models.external_i_ds import ExternalIDs
from .models.funding import Funding
from .models.funding_contributor import FundingContributor
from .models.funding_contributor_attributes import FundingContributorAttributes
from .models.funding_contributors import FundingContributors
from .models.funding_group import FundingGroup
from .models.funding_summary import FundingSummary
from .models.funding_title import FundingTitle
from .models.fundings import Fundings
from .models.fuzzy_date import FuzzyDate
from .models.group_id_record import GroupIdRecord
from .models.group_id_records import GroupIdRecords
from .models.item import Item
from .models.items import Items
from .models.keyword import Keyword
from .models.last_modified_date import LastModifiedDate
from .models.month import Month
from .models.notification import Notification
from .models.notification_permission import NotificationPermission
from .models.organization import Organization
from .models.organization_address import OrganizationAddress
from .models.organization_defined_funding_sub_type import OrganizationDefinedFundingSubType
from .models.other_name import OtherName
from .models.peer_review import PeerReview
from .models.peer_review_group import PeerReviewGroup
from .models.peer_review_summary import PeerReviewSummary
from .models.peer_reviews import PeerReviews
from .models.person_external_identifier import PersonExternalIdentifier
from .models.publication_date import PublicationDate
from .models.researcher_url import ResearcherUrl
from .models.source import Source
from .models.source_client_id import SourceClientId
from .models.source_name import SourceName
from .models.source_orcid import SourceOrcid
from .models.subtitle import Subtitle
from .models.title import Title
from .models.transient_non_empty_string import TransientNonEmptyString
from .models.translated_title import TranslatedTitle
from .models.url import Url
from .models.work import Work
from .models.work_bulk import WorkBulk
from .models.work_contributors import WorkContributors
from .models.work_group import WorkGroup
from .models.work_summary import WorkSummary
from .models.work_title import WorkTitle
from .models.works import Works
from .models.year import Year

# import apis into sdk package
from .apis.development_member_apiv30_dev1_api import DevelopmentMemberAPIV30Dev1Api
from .apis.member_apiv20_api import MemberAPIV20Api
from .apis.member_apiv21_api import MemberAPIV21Api

# import ApiClient
from .api_client import ApiClient

from .configuration import Configuration

configuration = Configuration()
