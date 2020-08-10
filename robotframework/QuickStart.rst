*** Test Cases ***
User can create an account and log in
    Create Valid User   fred    P4ssw0rd
    Attempt to Login with Credentials    fred    P4ssw0rd
    Status Should Be    Logged In

User cannot log in with bad password
    Create Valid User    betty    P4ssw0rd
    Attempt to Login with Credentials    betty    wrong
    Status Should Be    Access Denied

*** Keywords ***
Clear login database
    Remove file     ${DATABASE FILE}
Create valid user
    [Arguments]     ${username}     {password}
    Create user     {$username}     {password}

*** Variables ***
${DATABASE FILE} ${TEMPDIR}${/}robotframework-quickstart-db.txt

*** Settings ***
Library OperatingSystem
Library lib/LoginLibrary.py

*** Settings ***
Suite Setup       Clear Login Database
Test Teardown     Clear Login Database