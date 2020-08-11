.. code:: robotframework
    *** Settings ***
    Library    DateTime

    *** Test Cases ***
    show me time
        ${date}=       Get Current Date
        Log    ${date}

    show me N
        Log    1111111





    *** Settings ***
    Resource    resource.robot

    *** Test Cases ***
    use key word test
        open browser and access baidu
        ${the value returned}    input username    osc_user
        log    ${the value returned}
        shopping    10