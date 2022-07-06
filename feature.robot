*** Settings ***
Library    RequestsLibrary
Library    base_functions.py
Library    Collections

#Suite Setup    SuiteSetup
#Suite Teardown    SuiteTeardown
*** Variables ***
${BaseUrl}    https://gorest.co.in

*** Test Cases ***

##################  Functional ###############
TestCase001: Verify response has pagination
    [Tags]    Sanity
    ${response}=    GET    ${BaseUrl}/public/v2/users/
    ${response_code}=    convert to string    ${response.status_code}
    should be equal    ${response_code}    200
    ${get_response}=    base_functions.Verify response has pagination    ${response}
    log many    ${get_response}
    IF  ${get_response} == True
        log many    pagination found

    ELSE
        log many    pagination not found
    END

TestCase002: Validate Json Data
    [Documentation]    "JSON Schema Validation"
    [Tags]    Sanity
    ${response}=    GET    ${BaseUrl}/public/v2/users/
    ${get_response}=    base_functions.Verify response jsonData    ${response}
    IF  ${get_response} == True
        log many    Valid Json Data
    ELSE
        log many    InValid Json Data
    END

TestCase003: Verify Response Data has email address
    [Documentation]    Test to Verify Response Data has email address
    [Tags]    SRG
    ${response}=    GET    ${BaseUrl}/public/v2/users/
    ${json_object} =    to json    ${response.content}
    log to console    ${json_object}[0]
    ${keys}=  set variable    ${json_object[0].keys()}
    should contain    ${keys}       email
    ${get_anymail}=    set variable    ${json_object[0]}[email]
    log to console   ${get_anymail}

#
TestCase004: Verify all entries on list data have similar attributes
    [Documentation]    field type and regular expression
    [Tags]    SRG
    ${response}=    GET    ${BaseUrl}/public/v2/users/
    ${attributesdata}=    base_functions.Verify json attributes     ${response}


################## NON Functional ################
TestCase005: Verify HTTP response codes
    ${response}=    GET    ${BaseUrl}/public/v2/users/
    ${response_code}=    convert to string    ${response.status_code}
    should be equal    ${response_code}    200




*** Keywords ***
SuiteSetup
    log many    Suite Setup Done
SuiteTeardown
    log many    Suite Teardown Done