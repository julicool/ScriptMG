# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from auto.models import userlogin
from auto.models import mobileinfo
from auto.models import sys_dict
from django.http import JsonResponse
from django.db.models import Count  # 数据库查询统计
import json
import time


def surelogin(request):
    if request.POST:
        userinfo = json.loads(request.body)
        username = userinfo['un']
        password = userinfo['pw']
        usercode = userinfo['code']
        password_0 = userlogin.objects.filter(username=username).values('passwd')
        if password_0.exists():
            if password == password_0[0]['passwd']:
                data = {}
                data["resultCode"] = 0
                data["resultContent"] = str("success")
                response = HttpResponse(json.dumps(data))
                response.set_cookie('username', username, max_age=2000)
                return response
            else:
                data = {}
                data["resultCode"] = 1
                data["resultContent"] = str("用户名/密码错误")
                return HttpResponse(json.dumps(data))
        else:

            if usercode == 0:
                data = {}
                data["resultCode"] = 2
                data["resultContent"] = str("当前用户未注册")
                return HttpResponse(json.dumps(data))

            elif usercode == 1:
                userlogin.objects.create(username=username, passwd=password)
                if userlogin.objects.filter(username=username).values('passwd').exists():
                    data = {}
                    data["resultCode"] = 3
                    data["resultContent"] = str("注册成功")
                    response = HttpResponse(json.dumps(data))
                    response.set_cookie('username', username, max_age=2000)
                    return response


def addmob(request):
    if request.POST:
        mobname = request.POST["mobname"]
        mobmodel = request.POST["mobmodel"]
        mobstat = request.POST["mobstat"]
        resolution = request.POST["resolution_x"] + "*" + request.POST["resolution_y"]
        system_type = request.POST["system_type"]
        system_numb = request.POST["system_numb"]
        mobileinfo.objects.create(mobname_id=mobname, mobmodel=mobmodel, mobstat=mobstat, resolution=resolution,
                                  system_type=system_type, system_numb=system_numb, create_time=int(time.time())
                                  )
        if mobileinfo.objects.filter(mobname=mobname).values().exists():
            return HttpResponseRedirect('/mobman')
        else:
            return HttpResponse("新增失败")
    else:
        return HttpResponse("请检查请求")


def delmob(request):
    if request.POST:
        del_info = json.loads(request.body)
        mobileinfo.objects.filter(id=del_info['id']).delete()
        data = {"resultCode": 0, "resultContent": "success"}
        return JsonResponse(data, safe=False)


def getmob(request):
    if request.GET:
        if request.GET['w'] != None:
            mobinfo = mobileinfo.objects.filter(id=request.GET['w']).values('mobname_id', 'mobmodel', 'mobstat',
                                                                            'resolution', 'system_type', 'system_numb')
            print(mobinfo)
            data = list(mobinfo)
            return JsonResponse(data, safe=False)
        else:
            data = {"resultCode": 1, "resultContent": "参数错误"}
            return JsonResponse(data, safe=False)
    elif request.POST:
        moblist = {}
        start = json.loads(request.POST['start'])
        end = start + 5
        sum = (mobileinfo.objects.aggregate(count=Count('id')))['count'] / 10
        if(sum == int(sum)):
            sum = int(sum)-1
        else:
            sum = int(sum)
        if end > sum:
            end = sum
        for i in range(start, end + 1):
            moblist[i] = list(mobileinfo.objects.values('mobname__deploy_name', 'mobmodel', 'mobstat', 'resolution',
                                                        'system_type', 'system_numb', 'id').order_by('-id')[
                              i * 10:(i + 1) * 10])
        sum_inf = {'sum': sum * 10, 'start': start, 'end': end}
        data = {'moblist': moblist, 'sum_inf': sum_inf}
        return JsonResponse(data, safe=False)


def get_mob_list(request):
    dev_list = sys_dict.objects.filter(dic_name="mobname").values('id', 'deploy_name')
    dev_list = list(dev_list)
    data = {'dev_list': dev_list}
    return JsonResponse(data, safe=False)


def updmob(request):
    if request.POST:
        id = request.POST["id"]
        mobname = request.POST["mobname"]
        mobmodel = request.POST["mobmodel"]
        mobstat = request.POST["mobstat"]
        resolution = request.POST["resolution_x"] + "*" + request.POST["resolution_y"]
        system_type = request.POST["system_type"]
        system_numb = request.POST["system_numb"]
        mobileinfo.objects.filter(id=id).update(mobname_id=mobname, mobmodel=mobmodel, mobstat=mobstat,
                                                resolution=resolution,
                                                system_type=system_type, system_numb=system_numb,
                                                create_time=int(time.time())
                                                )
        if mobileinfo.objects.filter(mobname=mobname).values().exists():
            return HttpResponseRedirect('/mobman')
        else:
            return HttpResponse("更新失败")
    else:
        return HttpResponse("更新失败")


def mob_stat(request):
    moblist = list(
        mobileinfo.objects.filter(mobstat=0).values('id', 'mobname__deploy_name', 'mobmodel', 'mobstat', 'resolution',
                                                    'system_type', 'system_numb', 'username', 'frist_time',
                                                    'last_time').order_by('last_time'))
    for i in range(0, len(moblist)):
        moblist[i]['frist_time'] = time.strftime("%m月%d日 %H:%M", time.localtime(moblist[i]['frist_time']))
        moblist[i]['last_time'] = time.strftime("%m月%d日 %H:%M", time.localtime(moblist[i]['last_time']))
    return JsonResponse(moblist, safe=False)


def bor_mob(request):
    if request.POST:
        mobinf = json.loads(request.body)
        mobileinfo.objects.filter(id=mobinf['u_id']).update(username=mobinf['u_name'], frist_time=int(time.time()),
                                                            last_time=(int(time.time()) + int(
                                                                mobinf['last_time']) * 3600))
        data = {'resultCode': 0, 'resultMess': '借用成功'}
        return JsonResponse(data, safe=False)
    else:
        data = {'resultCode': 1, 'resultMess': '参数错误'}
        return JsonResponse(data, safe=False)


def exprmob(request):
    if request.POST:
        moblist = {}
        start = json.loads(request.POST['start'])
        end = start + 5
        sum = (mobileinfo.objects.filter(last_time__gt=0).aggregate(count=Count('id')))['count'] / 11
        if(sum == int(sum)):
            sum = int(sum)-1
        else:
            sum = int(sum)
        if end > sum:
            end = sum
        for i in range(start, end + 1):
            moblist[i] = list(
                mobileinfo.objects.filter(last_time__gt=0).values('mobname__deploy_name', 'mobmodel',
                                          'username',
                                          'frist_time', 'last_time',
                                          'id').order_by('last_time')[
                i * 11:(i + 1) * 11])
        for i in moblist:
            for m in range(0, len(moblist[i])):
                moblist[i][m]['frist_time'] = time.strftime("%m月%d日 %H:%M", time.localtime(moblist[i][m]['frist_time']))
                if(moblist[i][m]['last_time']<time.time()):
                    moblist[i][m]['urgent'] = 1
                else:
                    moblist[i][m]['urgent'] = 0
                moblist[i][m]['last_time'] = time.strftime("%m月%d日 %H:%M", time.localtime(moblist[i][m]['last_time']))
        sum_inf = {'sum': sum * 11, 'start': start, 'end': end}
        data = {'moblist': moblist, 'sum_inf': sum_inf}
        return JsonResponse(data, safe=False)


def returnmob(request):
    if request.POST:
        try:
            mobid = int(request.POST['id'])
            mobileinfo.objects.filter(id=mobid).update(username=None, frist_time=None, last_time=None)
            data = {'resultCode': 0, 'resultMess': '删除成功'}
            return JsonResponse(data, safe=False)
        except Exception as e:
            data = {'resultCode': 1, 'resultMess': str(e)}
            return JsonResponse(data, safe=False)
