# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from auto.models import resultchart
from auto.models import resultjs
from auto.models import timejob
from django.core import serializers
from django.db.models import Count  # 数据库查询统计

import os, json, time, shutil, sys, subprocess, threading, sched


def index(request):
    return render(request, 'auto/index.html')


def scriptmanage(request):
    file = []
    project = {}
    dirr = []
    for root, dirs, files in os.walk('./script/', True):

        for x in range(len(files) - 1):
            if files[x].endswith("py") == False:
                del files[x]
        file.append(files)
        dirr.append(dirs)
    for x in range(len(dirr[0])):
        project[(dirr[0][x])] = file[x + 1]
    return render(request, "auto/scriptManage.html", {'project': project})


def projectmanage(request):
    dirss = []
    filess = []
    data = {}
    for root, dirs, files in os.walk('./script/', True):
        for x in range(len(files) - 1):
            if files[x].endswith("py") == False:
                del files[x]
        dirss.append(dirs)
        filess.append(files)

    for x in range(len(dirss[0])):
        data[dirss[0][x]] = {}
        data[dirss[0][x]]['path'] = str(os.path.join('./script/', dirss[0][x]))
        data[dirss[0][x]]['filenum'] = len(filess[x + 1])
        data[dirss[0][x]]['ctime'] = time.strftime("%m-%d", time.localtime(os.stat(data[dirss[0][x]]['path'])[9]))
    return render(request, "auto/projectManage.html", {'data': data})


def changeproject(request):
    if request.POST:
        try:
            os.rename("./script/" + request.POST['oldprojectname'], "./script/" + request.POST['projectname'])
            timejob.objects.filter(pjname=request.POST['oldprojectname']).update(pjname=request.POST['projectname'])
            return HttpResponseRedirect('/projectmanage')
        except Exception as e:
            return HttpResponse(e)


def deleteproject(request):
    if request.POST['projectname'] != "":
        try:
            shutil.rmtree("./script/" + request.POST['projectname'])
            timejob.objects.filter(pjname=request.POST['projectname']).delete()
        except Exception:
            return HttpResponse(Exception)
        else:
            return HttpResponseRedirect('/projectmanage')
    else:
        return HttpResponse("请选择要删除的脚本");


def createproject(request):
    if request.POST:
        if os.path.exists("./script/" + request.POST['projectname']):
            return HttpResponse(request.POST['projectname'] + "项目已存在")
        else:
            os.mkdir("./script/" + request.POST['projectname'], 0o775)
            for x in range(3):
                newjob = timejob()
                newjob.stime = "0800"
                newjob.pjname = request.POST['projectname']
                newjob.stat = 0
                newjob.save()
            return HttpResponseRedirect('/projectmanage')


def runscript(request):
    if request.POST:
        # x = request.body
        res = {}
        # files = x.decode('unicode_escape')
        files = json.loads(request.body)
        rem = resultchart()
        rem.stime = time.time()
        codenum = 0
        succnum = 0
        for key, value in files.items():
            rem.projectname = key
            for file in value:
                jsrem = resultjs()
                jsrem.stime = time.time()
                code = subprocess.getstatusoutput("python3 ./script/" + key + "/" + file)
                res[file] = [code[0], code[1]]
                codenum += 1
                if code[0] == 0:
                    succnum += 1
                else:
                    jsrem.jsname = file
                    jsrem.errreason = code[1]
                    jsrem.save()

        rem.etime = time.time()
        rem.rtime = rem.etime - rem.stime
        rem.successrate = int((succnum / codenum) * 100)
        rem.stime = time.strftime("%Y-%m-%d  %H:%M:%S", time.localtime(rem.stime))
        rem.etime = time.strftime("%Y-%m-%d  %H:%M:%S", time.localtime(rem.etime))
        rem.save()

        return HttpResponse(json.dumps(res))


def uploadfiles(request):
    if request.POST:
        files = request.FILES.getlist('fileslist');
        for f in files:
            if os.path.exists("./script/" + request.POST['projectname'] + "/" + f.name):
                return HttpResponse(request.POST['projectname'] + "项目中已存在" + f.name)
            else:
                with open("./script/" + request.POST['projectname'] + "/" + f.name, "wb+") as des:
                    for t in f.chunks():
                        des.write(t)
        return HttpResponseRedirect('/scriptmanage')


def deletefiles(request):
    try:
        if request.POST:
            # x = request.body
            res = ""
            # files = x.decode('unicode_escape')
            files = json.loads(request.body)
            for key, value in files.items():
                for file in value:
                    if key != "":
                        os.remove("./script/" + key + "/" + file)
                        res = res + file + " "
                    else:
                        return HttpResponse("项目名称未传，请检查")
            return HttpResponse(json.dumps(1))
    except BaseException as e:
        return HttpResponse(json.dumps(str(e)))


def reschart(request):
    try:
        return render(request, "auto/reschart.html")
    except BaseException as e:
        return HttpResponse(json.dumps(str(e)))


def getreschart(request):
    try:
        n = int(request.POST['n']) * 14
        m = n + 14
        num = resultchart.objects.aggregate(count=Count('id'))
        if num['count'] < m:
            m = num['count']
        res = resultchart.objects.values('id', 'projectname', 'stime', 'rtime', 'successrate').order_by('-id')[n:m]
        res = {'num': num, 'res': list(res)}
        return HttpResponse(json.dumps(res))
    except Exception as e:
        return HttpResponse(json.dumps(str(e)))


def getresjs(request):
    try:
        res = resultjs.objects.values().order_by('-id')[n:m]
        res = {'num': num, 'res': list(res)}
        return HttpResponse(json.dumps(res))
    except Exception as e:
        return HttpResponse(json.dumps(str(e)))


def chotime(request):
    try:
        return render(request, 'auto/chotime.html')
    except Exception as e:
        return HttpResponse(json.dumps(str(e)))


def showtime(request):
    try:
        if request.POST:
            mess = json.loads(request.body)
            if mess['behaviour'] == 1:
                timejob.objects.filter(id=mess['id']).update(stat=mess['code'])
                return HttpResponse("修改成功！")

            if mess['behaviour'] == 2:
                x = timejob.objects.filter(pjname=mess['pjname']).values('stime', 'id').order_by('-id')
                return HttpResponse(json.dumps(list(x)))

        else:
            val = timejob.objects.values()
            val = list(val)
            pjn = timejob.objects.values_list('pjname', flat=True).distinct()
            pjn = list(pjn)
            res = {}

            for key in pjn:
                res[key] = []
            for key in val:
                if key['pjname'] in pjn:
                    res[key['pjname']].append({'id': key['id'], 'stime': key['stime'], 'stat': key['stat']})
            return HttpResponse(json.dumps(res))
    except Exception as e:
        return HttpResponse(json.dumps(str(e)))


def runsmjs(pjname):
    try:
        file = []
        codenum = 0
        succnum = 0
        for root, dirs, files in os.walk("./script/" + pjname + "/", True):
            for x in range(len(files) - 1):
                if files[x].endswith("py") == False:
                    del files[x]
            file = files
        rem = resultchart()
        rem.projectname = pjname
        rem.stime = time.time()

        for n in file:
            remjs = resultjs()
            remjs.stime = time.time()
            remjs.jsname = n
            code = subprocess.getstatusoutput("python3 ./script/" + pjname + "/" + n)
            codenum += 1
            if code[0] == 0:
                succnum += 1
            else:
                remjs.errreason = code[1]
                remjs.save()
        rem.etime = time.time()
        rem.rtime = rem.etime - rem.stime
        rem.successrate = int((succnum / codenum) * 100)
        rem.stime = time.strftime("%Y-%m-%d  %H:%M:%S", time.localtime(rem.stime))
        rem.etime = time.strftime("%Y-%m-%d  %H:%M:%S", time.localtime(rem.etime))
        rem.save()
        return 1
    except Exception as e:
        return json.dumps(str(e))


def foundjs(request):
    try:
        now = time.localtime(time.time())
        nowtime = time.strftime("%H%M", now)
        jstime = timejob()
        jobs = timejob.objects.filter(stime="0800", stat=1).values_list('pjname', flat=True)
        jobs = list(jobs)
        for j in jobs:
            r = threading.Thread(target=runsmjs, args=(j,))
            r.start()
        return HttpResponse("success")
    except Exception as e:
        return HttpResponse(e)


def timer(request):
    try:
        x = threading.activeCount()
        y = threading.enumerate()
        z = ""
        if x > 4:
            pass
        else:
            r = threading.Timer(60, foundjs)
            r.name = "tiemr"
            z = r.isAlive()
            r.start()
        return HttpResponse(x)
    except Exception as e:
        return HttpResponse(e)


def changetime(request):
    try:
        x = []
        x.append(request.POST['time1'])
        x.append(request.POST['time2'])
        x.append(request.POST['time3'])
        return HttpResponse(json.dumps(x))
    except Exception as e:
        return HttpResponse(json.dumps(e))
