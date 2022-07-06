import jsonschema.exceptions

try:
    from robot.libraries.BuiltIn import BuiltIn
    from robot.libraries.BuiltIn import keyword
    import robot.api.logger as logger
    import requests
    import json
    import re
    import jsonpath_ng
    from jsonschema import validate
    ROBOT = False


except Exception:
    ROBOT = False

@keyword("Verify response has pagination")
def pagination_validation(response):

    validate_pagination = response.headers
    if "X-Pagination-Pages" in validate_pagination.keys():
        return True
    else:
        return False

@keyword("Verify response jsonData")
def jsondata_validation(response):
    """
    :param response:
    :return:
    """
    response_data = response.json()

    try:
        with open("schema.json",'r') as f:
            schema_set = json.load(f)
            for i in range(len(response_data)):
                try:
                    validate(instance=response_data[i],schema=schema_set)
                except jsonschema.exceptions.ValidationError as e:
                    print(e)
                    raise Exception
                    return False
        return True
    except Exception:
        raise Exception
        return False

@keyword("Verify json attributes")
def json_attributes_velidation(response):
    """
    :param response:
    :return:
    """
    response_data = response.json()
    keys_to_be_validated = ("id","name","email","gender","status")
    email_regex = '^([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+$'
    id_pattren = '^[0-9]{1}$'
    name_pattr = '^[A-Za-z].+$'

    for i in range(len(response_data)):

        if sorted(response_data[i].keys()) == sorted(keys_to_be_validated):
            id = (re.match(id_pattren,str(response_data[i]["id"])))
            name = (re.search(name_pattr,response_data[i]["name"]))
            email = (re.search(email_regex,response_data[i]["email"]))

            if id is None or name is None and email is None:
                raise Exception(f"Error in content, pattern mismatch! at doc index {i}:")
            else:
                pass







