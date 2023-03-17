# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp

imp.reload(sys)
try:
    sys.setdefaultencoding("UTF8")
except Exception as E:
    pass

import testValue

from popbill import BizInfoCheckService, PopbillException

bizInfoCheckService = BizInfoCheckService(testValue.LinkID, testValue.SecretKey)
bizInfoCheckService.IsTest = testValue.IsTest
bizInfoCheckService.IPRestrictOnOff = testValue.IPRestrictOnOff
bizInfoCheckService.UseStaticIP = testValue.UseStaticIP
bizInfoCheckService.UseLocalTimeYN = testValue.UseLocalTimeYN

"""
사업자번호를 조회하여 연동회원 가입여부를 확인합니다.
- https://developers.popbill.com/reference/bizinfocheck/python/api/member#CheckIsMember
"""

try:
    print("=" * 15 + " 연동회원 가입여부 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    result = bizInfoCheckService.checkIsMember(CorpNum)

    print("가입여부 : [%d] %s" % (result.code, result.message))
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
