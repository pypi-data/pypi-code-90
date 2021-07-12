# coding: utf-8

"""
    UltraCart Rest API V2

    UltraCart REST API Version 2  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: support@ultracart.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class OrderAffiliateLedger(object):
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
        'assigned_by_user': 'str',
        'item_id': 'str',
        'tier_number': 'int',
        'transaction_amount': 'float',
        'transaction_amount_paid': 'float',
        'transaction_dts': 'str',
        'transaction_memo': 'str',
        'transaction_percentage': 'float',
        'transaction_state': 'str'
    }

    attribute_map = {
        'assigned_by_user': 'assigned_by_user',
        'item_id': 'item_id',
        'tier_number': 'tier_number',
        'transaction_amount': 'transaction_amount',
        'transaction_amount_paid': 'transaction_amount_paid',
        'transaction_dts': 'transaction_dts',
        'transaction_memo': 'transaction_memo',
        'transaction_percentage': 'transaction_percentage',
        'transaction_state': 'transaction_state'
    }

    def __init__(self, assigned_by_user=None, item_id=None, tier_number=None, transaction_amount=None, transaction_amount_paid=None, transaction_dts=None, transaction_memo=None, transaction_percentage=None, transaction_state=None):  # noqa: E501
        """OrderAffiliateLedger - a model defined in Swagger"""  # noqa: E501

        self._assigned_by_user = None
        self._item_id = None
        self._tier_number = None
        self._transaction_amount = None
        self._transaction_amount_paid = None
        self._transaction_dts = None
        self._transaction_memo = None
        self._transaction_percentage = None
        self._transaction_state = None
        self.discriminator = None

        if assigned_by_user is not None:
            self.assigned_by_user = assigned_by_user
        if item_id is not None:
            self.item_id = item_id
        if tier_number is not None:
            self.tier_number = tier_number
        if transaction_amount is not None:
            self.transaction_amount = transaction_amount
        if transaction_amount_paid is not None:
            self.transaction_amount_paid = transaction_amount_paid
        if transaction_dts is not None:
            self.transaction_dts = transaction_dts
        if transaction_memo is not None:
            self.transaction_memo = transaction_memo
        if transaction_percentage is not None:
            self.transaction_percentage = transaction_percentage
        if transaction_state is not None:
            self.transaction_state = transaction_state

    @property
    def assigned_by_user(self):
        """Gets the assigned_by_user of this OrderAffiliateLedger.  # noqa: E501

        UltraCart user name that assigned this commission if manually assigned  # noqa: E501

        :return: The assigned_by_user of this OrderAffiliateLedger.  # noqa: E501
        :rtype: str
        """
        return self._assigned_by_user

    @assigned_by_user.setter
    def assigned_by_user(self, assigned_by_user):
        """Sets the assigned_by_user of this OrderAffiliateLedger.

        UltraCart user name that assigned this commission if manually assigned  # noqa: E501

        :param assigned_by_user: The assigned_by_user of this OrderAffiliateLedger.  # noqa: E501
        :type: str
        """

        self._assigned_by_user = assigned_by_user

    @property
    def item_id(self):
        """Gets the item_id of this OrderAffiliateLedger.  # noqa: E501

        Item ID that this ledger record is associated with  # noqa: E501

        :return: The item_id of this OrderAffiliateLedger.  # noqa: E501
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this OrderAffiliateLedger.

        Item ID that this ledger record is associated with  # noqa: E501

        :param item_id: The item_id of this OrderAffiliateLedger.  # noqa: E501
        :type: str
        """

        self._item_id = item_id

    @property
    def tier_number(self):
        """Gets the tier_number of this OrderAffiliateLedger.  # noqa: E501

        Tier number of this affiliate in the commission calculation  # noqa: E501

        :return: The tier_number of this OrderAffiliateLedger.  # noqa: E501
        :rtype: int
        """
        return self._tier_number

    @tier_number.setter
    def tier_number(self, tier_number):
        """Sets the tier_number of this OrderAffiliateLedger.

        Tier number of this affiliate in the commission calculation  # noqa: E501

        :param tier_number: The tier_number of this OrderAffiliateLedger.  # noqa: E501
        :type: int
        """

        self._tier_number = tier_number

    @property
    def transaction_amount(self):
        """Gets the transaction_amount of this OrderAffiliateLedger.  # noqa: E501

        Amount of the transaction  # noqa: E501

        :return: The transaction_amount of this OrderAffiliateLedger.  # noqa: E501
        :rtype: float
        """
        return self._transaction_amount

    @transaction_amount.setter
    def transaction_amount(self, transaction_amount):
        """Sets the transaction_amount of this OrderAffiliateLedger.

        Amount of the transaction  # noqa: E501

        :param transaction_amount: The transaction_amount of this OrderAffiliateLedger.  # noqa: E501
        :type: float
        """

        self._transaction_amount = transaction_amount

    @property
    def transaction_amount_paid(self):
        """Gets the transaction_amount_paid of this OrderAffiliateLedger.  # noqa: E501

        The amount that has been paid so far on the transaction  # noqa: E501

        :return: The transaction_amount_paid of this OrderAffiliateLedger.  # noqa: E501
        :rtype: float
        """
        return self._transaction_amount_paid

    @transaction_amount_paid.setter
    def transaction_amount_paid(self, transaction_amount_paid):
        """Sets the transaction_amount_paid of this OrderAffiliateLedger.

        The amount that has been paid so far on the transaction  # noqa: E501

        :param transaction_amount_paid: The transaction_amount_paid of this OrderAffiliateLedger.  # noqa: E501
        :type: float
        """

        self._transaction_amount_paid = transaction_amount_paid

    @property
    def transaction_dts(self):
        """Gets the transaction_dts of this OrderAffiliateLedger.  # noqa: E501

        The date/time that the affiliate ledger was generated for the transaction  # noqa: E501

        :return: The transaction_dts of this OrderAffiliateLedger.  # noqa: E501
        :rtype: str
        """
        return self._transaction_dts

    @transaction_dts.setter
    def transaction_dts(self, transaction_dts):
        """Sets the transaction_dts of this OrderAffiliateLedger.

        The date/time that the affiliate ledger was generated for the transaction  # noqa: E501

        :param transaction_dts: The transaction_dts of this OrderAffiliateLedger.  # noqa: E501
        :type: str
        """

        self._transaction_dts = transaction_dts

    @property
    def transaction_memo(self):
        """Gets the transaction_memo of this OrderAffiliateLedger.  # noqa: E501

        Details of the transaction suitable for display to the affiliate  # noqa: E501

        :return: The transaction_memo of this OrderAffiliateLedger.  # noqa: E501
        :rtype: str
        """
        return self._transaction_memo

    @transaction_memo.setter
    def transaction_memo(self, transaction_memo):
        """Sets the transaction_memo of this OrderAffiliateLedger.

        Details of the transaction suitable for display to the affiliate  # noqa: E501

        :param transaction_memo: The transaction_memo of this OrderAffiliateLedger.  # noqa: E501
        :type: str
        """

        self._transaction_memo = transaction_memo

    @property
    def transaction_percentage(self):
        """Gets the transaction_percentage of this OrderAffiliateLedger.  # noqa: E501

        The percentage earned on the transaction  # noqa: E501

        :return: The transaction_percentage of this OrderAffiliateLedger.  # noqa: E501
        :rtype: float
        """
        return self._transaction_percentage

    @transaction_percentage.setter
    def transaction_percentage(self, transaction_percentage):
        """Sets the transaction_percentage of this OrderAffiliateLedger.

        The percentage earned on the transaction  # noqa: E501

        :param transaction_percentage: The transaction_percentage of this OrderAffiliateLedger.  # noqa: E501
        :type: float
        """

        self._transaction_percentage = transaction_percentage

    @property
    def transaction_state(self):
        """Gets the transaction_state of this OrderAffiliateLedger.  # noqa: E501

        The state of the transaction  # noqa: E501

        :return: The transaction_state of this OrderAffiliateLedger.  # noqa: E501
        :rtype: str
        """
        return self._transaction_state

    @transaction_state.setter
    def transaction_state(self, transaction_state):
        """Sets the transaction_state of this OrderAffiliateLedger.

        The state of the transaction  # noqa: E501

        :param transaction_state: The transaction_state of this OrderAffiliateLedger.  # noqa: E501
        :type: str
        """
        allowed_values = ["Pending", "Posted", "Approved", "Paid", "Rejected", "Partially Paid"]  # noqa: E501
        if transaction_state not in allowed_values:
            raise ValueError(
                "Invalid value for `transaction_state` ({0}), must be one of {1}"  # noqa: E501
                .format(transaction_state, allowed_values)
            )

        self._transaction_state = transaction_state

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
        if issubclass(OrderAffiliateLedger, dict):
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
        if not isinstance(other, OrderAffiliateLedger):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
