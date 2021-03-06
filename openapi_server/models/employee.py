# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Employee(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, employee_name=None, employee_title=None):  # noqa: E501
        """Employee - a model defined in OpenAPI

        :param id: The id of this Employee.  # noqa: E501
        :type id: int
        :param employee_name: The employee_name of this Employee.  # noqa: E501
        :type employee_name: str
        :param employee_title: The employee_title of this Employee.  # noqa: E501
        :type employee_title: str
        """
        self.openapi_types = {
            'id': int,
            'employee_name': str,
            'employee_title': str
        }

        self.attribute_map = {
            'id': 'id',
            'employee_name': 'employee name',
            'employee_title': 'employee title'
        }

        self._id = id
        self._employee_name = employee_name
        self._employee_title = employee_title

    @classmethod
    def from_dict(cls, dikt) -> 'Employee':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Employee of this Employee.  # noqa: E501
        :rtype: Employee
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this Employee.


        :return: The id of this Employee.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Employee.


        :param id: The id of this Employee.
        :type id: int
        """

        self._id = id

    @property
    def employee_name(self):
        """Gets the employee_name of this Employee.


        :return: The employee_name of this Employee.
        :rtype: str
        """
        return self._employee_name

    @employee_name.setter
    def employee_name(self, employee_name):
        """Sets the employee_name of this Employee.


        :param employee_name: The employee_name of this Employee.
        :type employee_name: str
        """

        self._employee_name = employee_name

    @property
    def employee_title(self):
        """Gets the employee_title of this Employee.


        :return: The employee_title of this Employee.
        :rtype: str
        """
        return self._employee_title

    @employee_title.setter
    def employee_title(self, employee_title):
        """Sets the employee_title of this Employee.


        :param employee_title: The employee_title of this Employee.
        :type employee_title: str
        """

        self._employee_title = employee_title
