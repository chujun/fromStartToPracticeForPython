*** Test Cases ***
创建用户并登录
    创建用户   fred    P4ssw0rd
    Attempt to Login with Credentials    fred    P4ssw0rd
    Status Should Be    Logged In

错误密码登录
    创建用户    betty    P4ssw0rd
    Attempt to Login with Credentials    betty    wrong
    Status Should Be    Access Denied

#Higher-level tests
*** Test Cases ***
改变密码完整流程
    Given a user has a valid account
    When she changes her password
    Then she can log in with the new password
    And she cannot use the old password anymore

#Data-driven tests

*** Test Cases ***
非法密码登录
    [Template]      创建用户并用非法密码登录
    abCD5            ${PWD INVALID LENGTH}
    abCD567890123    ${PWD INVALID LENGTH}
    123DEFG          ${PWD INVALID CONTENT}
    abcd56789        ${PWD INVALID CONTENT}
    AbCdEfGh         ${PWD INVALID CONTENT}
    abCD56+          ${PWD INVALID CONTENT}

*** Keywords ***
清除登录数据库
    Remove file     ${DATABASE FILE}
创建用户
    [Arguments]     ${username}     ${password}
    Create user     ${username}     ${password}
创建用户并用非法密码登录
    [Arguments]    ${password}    ${error}
    Create user    example    ${password}
    Status should be    Creating user failed: ${error}
成功登录
    [Arguments]    ${username}    ${password}
    Attempt to login with credentials    ${username}    ${password}
    Status should be    Logged In
# Keywords below used by higher level tests. Notice how given/when/then/and
# prefixes can be dropped. And this is a comment.
A user has a valid account
    创建用户   ${USERNAME}     ${PASSWORD}
she changes her password
    Change password     ${USERNAME}     ${PASSWORD}     ${NEW PASSWORD}
    Status should be    SUCCESS
She can log in with the new password
    成功登录    ${USERNAME}    ${NEW PASSWORD}
She cannot use the old password anymore
    Attempt to login with credentials    ${USERNAME}    ${PASSWORD}
    Status should be    Access Denied
*** Variables ***
${DATABASE FILE}    ${TEMPDIR}${/}robotframework-quickstart-db.txt
${USERNAME}               janedoe
${PASSWORD}               J4n3D0e
${NEW PASSWORD}           e0D3n4J
${PWD INVALID LENGTH}     Password must be 7-12 characters long
${PWD INVALID CONTENT}    Password must be a combination of lowercase and uppercase letters and numbers

*** Settings ***
Library     OperatingSystem
Library     pylib/LoginLibrary.py

*** Settings ***
Documentation   中文版test case,keywords可支持中文
Suite Setup       清除登录数据库
Test Teardown     清除登录数据库