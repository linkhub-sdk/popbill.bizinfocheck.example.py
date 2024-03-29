# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import imp
import sys

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
기업정보조회 단가를 확인합니다.
- https://developers.popbill.com/reference/bizinfocheck/python/api/point#GetUnitCost
"""

try:
    print("=" * 15 + " 기업정보조회 단가 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    unitCost = bizInfoCheckService.getUnitCost(CorpNum)

    print("조회 단가 : %f" % unitCost)
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
