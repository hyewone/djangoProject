from django.http import HttpResponse
from django.shortcuts import render
import win32com.client,pythoncom



def test(request):
    pythoncom.CoInitialize()
    # 연결 여부 체크
    objCpCybos = win32com.client.Dispatch("CpUtil.CpCybos")
    bConnect = objCpCybos.IsConnect
    if (bConnect == 0):
        print("PLUS가 정상적으로 연결되지 않음. ")
        exit()

    # 종목코드 리스트 구하기
    objCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
    codeList = objCpCodeMgr.GetStockListByMarket(1)  # 거래소
    codeList2 = objCpCodeMgr.GetStockListByMarket(2)  # 코스닥

    print("거래소 종목코드", len(codeList))
    for i, code in enumerate(codeList):
        secondCode = objCpCodeMgr.GetStockSectionKind(code)
        name = objCpCodeMgr.CodeToName(code)
        stdPrice = objCpCodeMgr.GetStockStdPrice(code)
        print(i, code, secondCode, stdPrice, name)

    print("코스닥 종목코드", len(codeList2))
    for i, code in enumerate(codeList2):
        secondCode = objCpCodeMgr.GetStockSectionKind(code)
        name = objCpCodeMgr.CodeToName(code)
        stdPrice = objCpCodeMgr.GetStockStdPrice(code)
        print(i, code, secondCode, stdPrice, name)

    print("거래소 + 코스닥 종목코드 ", len(codeList) + len(codeList2))
    """
    codeList = [1, 2, 3, 4, 5]
    codeList2 = [6, 7, 8, 9, 10]
    """
    #codeList, codeList2 넘겨주기
    return render(request, 'test.html', { 'codeList' : codeList, 'codeList2' : codeList2 })


def test2(request):
    pythoncom.CoInitialize()
    # 연결 여부 체크
    objCpCybos = win32com.client.Dispatch("CpUtil.CpCybos")
    bConnect = objCpCybos.IsConnect
    if (bConnect == 0):
        print("PLUS가 정상적으로 연결되지 않음. ")
        exit()

    # 종목코드 리스트 구하기
    objCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
    codeList = objCpCodeMgr.GetStockListByMarket(1)  # 거래소
    codeList2 = objCpCodeMgr.GetStockListByMarket(2)  # 코스닥

    print("거래소 종목코드", len(codeList))
    for i, code in enumerate(codeList):
        secondCode = objCpCodeMgr.GetStockSectionKind(code)
        name = objCpCodeMgr.CodeToName(code)
        stdPrice = objCpCodeMgr.GetStockStdPrice(code)
        print(i, code, secondCode, stdPrice, name)

    print("코스닥 종목코드", len(codeList2))
    for i, code in enumerate(codeList2):
        secondCode = objCpCodeMgr.GetStockSectionKind(code)
        name = objCpCodeMgr.CodeToName(code)
        stdPrice = objCpCodeMgr.GetStockStdPrice(code)
        print(i, code, secondCode, stdPrice, name)

    print("거래소 + 코스닥 종목코드 ", len(codeList) + len(codeList2))
    data = ''.map(codeList2)
    return JsonResponse(data)