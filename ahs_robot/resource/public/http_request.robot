*** Settings ***
Documentation    Suite description
Library     OperatingSystem
Library     RequestsLibrary
Library     String
Library     Collections

*** Test Cases ***
Calss_01_测试条件语句
    ${a}  set variable  1
    Run Keyword If  ${a}==1     log     ${a}
    ...  ELSE    log ${a}
Class_01_测试get请求
    create session  example_robotframework  http://192.168.103.194:8098  timeout=30
    ${resp}  get_request     example_robotframework  trade-in-center/v2/base-trade-in-orders/detail/20200728210218871717
    should be true  200==${resp.status_code}
    log     ${resp.content}
Class_01_测试get请求带param
    create session  example_robotframework  http://192.168.103.194:8098  timeout=30
    ${params}   set variable   isDesc=true
    ${resp}  get_request     example_robotframework  trade-in-center/erp/orders/20200728210218871717/traces     params=${params}
    should be true  200==${resp.status_code}
    log     ${resp.content}
Class_01_自定义get请求
    ${resp}  my_get_request    http://192.168.103.194:8098    trade-in-center/erp/orders/20200728210218871717/traces
    ...  ${None}   isDesc=true
    should be true  200==${resp.status_code}
    log     ${resp.content}
Class_02_测试post请求
    create session  example_robotframework  http://192.168.103.194:8098  timeout=30
    ${json}  create dictionary
    ${resp}  post_request     example_robotframework  trade-in-center/v2/base-trade-in-orders/search    json=${json}
    should be true  200==${resp.status_code}
    log     ${resp.content}

*** Keywords ***
my_get_request
    [Arguments]  ${host}    ${path}     ${datas}    ${params}   ${headers}=None   ${timeout}=30
    # 设置编码
    #EVALUATE   reload(sys)  sys
    #evaluate   sys.setdefaultencoding('utf-8')  sys
    #处理请求header
    ${header_dict}  create dictionary   Content-Type=application/json
    run keyword if  ${headers}==${None}    log   没有添加自定义header
    # 'Else' is a reserved keyword. It must be in uppercase (ELSE) when used as a marker with 'Run Keyword If'.
    ...     ELSE       run keyword     add_header     ${headers}      ${header_dict}
    #处理Cookie
#    ${cookie_dict}  create dictionary
#    run keyword if  ${cookie}==${None}  Log     没有添加cookie信息
#    ...  else   run keyword  add_cookies
    #创建session
    create session  example_robotframework  ${host}     timeout=${timeout}
    #发起GET请求
    ${resp}     RequestsLibrary.Get_Request     example_robotframework  ${path}     headers=${header_dict}  params=${params}
    [Return]  ${resp}
my_Post_Request
    [Arguments]     ${host}     ${path}     ${datas}        ${params}=${EMPTY}      ${headers}=None     ${cookies}=None     ${timeout}=30
    #   设置编码
    evaluate        reload(sys)     sys
    evaluate        sys.setdefaultencoding('utf-8')     sys
    #   处理请求header
    ${header_dict}  create dictionary   Content-Type=application/json
    run keyword if  ${headers}==${None}     Log 没有添加自定义header
    ...     ELSE    run keyword     add_header      ${headers}      ${header_dict}
    # 处理cookies
    ${cookie_dict}  create dictionary
    run keyword if  ${cookies}==${None}     Log 没有添加cookie信息
    ...     ELSE    run keyword     add_cookies     ${cookies}      ${cookie_dict}
    # 创建session
    create session  example_robotframework  ${host}  timeout=${timeout}  cookies=${cookie_dict}
    #发起post请求
    ${resp}  RequestsLibrary.Post_Request  example_robotframework   ${path}  data=${datas}  headers=${header_dict}  params=${params}
    [Return]   ${resp}

add_header
    [Arguments]   ${dict1}      ${dict2}
    [Documentation]  *遍历字典变量dic1，将dict1中的值添加到dict2中*
    log  在请求中添加自定义header
#    ${items}    get dictionary items        ${dict1}
#    :FOR    ${index}    ${key}      ${value}   In enumerate    @{items}
#    \   set to dictionary  ${dict2}      ${key}=${value}
#add_cookies
#    [Arguments]  ${cookies}     ${cookiedict}
#    [Documentation]  *处理Cookie*
#    @{cookielist}=  split string  ${cookies}    ;
#    :FOR    ${cookie}   INSERT INTO LIST  @{cookielist}     #用;分隔cookie
#    \   run keyword if      '${cookie}'=='${None}'  exit for loop
#    \   ${cookie_split}=    split string    ${cookie}   =
#    set to dictionary   ${cookiedict}    ${cookie_split[0]}=${cookie_split[1]}