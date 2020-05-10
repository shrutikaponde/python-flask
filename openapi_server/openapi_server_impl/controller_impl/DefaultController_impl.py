import connexion
import six

from openapi_server.models.employee import Employee  # noqa: E501
from openapi_server import util
from openapi_server.openapi_server_impl.controllers_impl import DefaultController_impl

def employees_get(body_limit=None, page_limit=None):  # noqa: E501
    """employees_get

    Obtain information about employees from the HR database # noqa: E501

    :param body_limit: The amount of employees returned
    :type body_limit: int
    :param page_limit: The pages to return employees info
    :type page_limit: int

    :rtype: List[Employee]
    """
    return DefaultController_impl.employees_get(body_limit, page_limit)

def employees_id_get(id):  # noqa: E501
    """employees_id_get

    Obtain information about specific employee # noqa: E501

    :param id: The ID of the employee
    :type id: int

    :rtype: Employee
    """
    return DefaultController_impl.employees_id_get(id)

def employees_post(employee):  # noqa: E501
    """employees_post

    Creates a new employee in the database # noqa: E501

    :param employee: 
    :type employee: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        employee = Employee.from_dict(connexion.request.get_json())  # noqa: E501
    return DefaultController_impl.employees_post(employee)
