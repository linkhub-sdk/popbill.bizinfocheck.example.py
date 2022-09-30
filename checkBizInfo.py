# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp

imp.reload(sys)
try:
    sys.setdefaultencoding('UTF8')
except Exception as E:
    pass

import testValue

from popbill import BizInfoCheckService, PopbillException

bizInfoCheckService = BizInfoCheckService(testValue.LinkID, testValue.SecretKey)
bizInfoCheckService.IsTest = testValue.IsTest
bizInfoCheckService.IPRestrictOnOff = testValue.IPRestrictOnOff
bizInfoCheckService.UseStaticIP = testValue.UseStaticIP
bizInfoCheckService.UseLocalTimeYN = testValue.UseLocalTimeYN

'''
사업자번호 1건에 대한 기업정보를 확인합니다.
- https://docs.popbill.com/bizinfocheck/python/api#CheckBizInfo
'''

try:
    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 조회할 사업자번호
    targetCorpNum = "6798700433"

    result = bizInfoCheckService.checkBizInfo(CorpNum, targetCorpNum)

    print("corpNum (사업자번호) : %s " % result.corpNum)
    print("companyRegNum (법인번호): %s " % result.companyRegNum)
    print("checkDT (확인일시) : %s  " % result.checkDT)
    print("corpName (상호): %s " % result.corpName)
    print("corpCode (기업형태코드): %s " % result.corpCode)
    print("corpScaleCode (기업규모코드): %s " % result.corpScaleCode)
    print("personCorpCode (개인법인코드): %s " % result.personCorpCode)
    print("headOfficeCode (본점지점코드) : %s " % result.headOfficeCode)
    print("industryCode (산업코드) : %s " % result.industryCode)
    print("establishCode (설립구분코드) : %s " % result.establishCode)
    print("establishDate (설립일자) : %s " % result.establishDate)
    print("CEOName (대표자명) : %s " % result.ceoname)
    print("workPlaceCode (사업장구분코드): %s " % result.workPlaceCode)
    print("addrCode (주소구분코드) : %s " % result.addrCode)
    print("zipCode (우편번호) : %s " % result.zipCode)
    print("addr (주소) : %s " % result.addr)
    print("addrDetail (상세주소) : %s " % result.addrDetail)
    print("enAddr (영문주소) : %s " % result.enAddr)
    print("bizClass (업종) : %s " % result.bizClass)
    print("bizType (업태) : %s " % result.bizType)
    print("result (결과코드) : %s " % result.result)
    print("resultMessage (결과메시지) : %s " % result.resultMessage)
    print("closeDownTaxType (사업자과세유형) : %s " % result.closeDownTaxType)
    print("closeDownTaxTypeDate (과세유형전환일자): %s" % result.closeDownTaxTypeDate)
    print("closeDownState (휴폐업상태) : %s " % result.closeDownState)
    print("closeDownStateDate (휴폐업일자) : %s " % result.closeDownStateDate)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
