from django.shortcuts import render

# Create your views here.
import base64
import os
import json
from django.conf import settings
from django.http import HttpResponseRedirect, response
from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect, reverse
from proweb.settings import MDEIA_ROOT, BASE_DIR
from .forms import UserRegisterForm, UserloginForm
from .utils import get_ql_token
from .models import Env
from django.db.models import Q
import sqlite3
from django.shortcuts import render
from django.http import JsonResponse
import subprocess
import requests

base_url = ""
client_id = ""
client_secret = ""
def extract_value(cookie_str, key):
    start_index = cookie_str.find(f'{key}=')
    if (start_index == -1):
        return None
    start_index += len(f'{key}=')
    end_index = cookie_str.find(';', start_index)
    if (end_index == -1):
        end_index = len(cookie_str)
    return cookie_str[start_index:end_index].strip()
    
def index(request):
    login_form = UserloginForm(request.POST or None)
    valid_values = []

    if request.method == 'POST':
        if login_form.is_valid():
            jd_cookie = login_form.cleaned_data['env']
            jd_remark = login_form.cleaned_data['remark']
            # 提取 pt_key/pt_pin 或者 pin/wskey 的值
            if 'pt_key=' in jd_cookie and 'pt_pin=' in jd_cookie:
                pt_key_value = extract_value(jd_cookie, 'pt_key')
                pt_pin_value = extract_value(jd_cookie, 'pt_pin')
                if pt_key_value and pt_pin_value:
                    valid_values = [pt_pin_value, pt_key_value, "pt_pin"]
            else:
                pin_value = extract_value(jd_cookie, 'pin')
                wskey_value = extract_value(jd_cookie, 'wskey')
                if pin_value and wskey_value:
                    valid_values = [pin_value, wskey_value, "wskey"]
            try:
                if valid_values and valid_values[2] == "pt_pin":
                    token = get_ql_token(base_url, client_id, client_secret)
                    headers = {
                        "Authorization": f"Bearer {token}",
                        "Content-Type": "application/json"
                    }

                    search_value = valid_values[0]  # 使用 pt_pin 作为查询条件
                    response = requests.get(f"{base_url}/open/envs?searchValue={search_value}", headers=headers)
                    # print("查询响应状态码：", response.status_code)
                    # print("查询响应内容：", response.text)
                    if response.status_code == 200:
                        envs = response.json()["data"]
                        pt_pin_exists = False
                        for env in envs:
                            if env["name"] == "JD_COOKIE" and f"pt_pin={valid_values[0]};" in env["value"]:
                                pt_pin_exists = True
                                new_env_value = f"pt_key={valid_values[1]};pt_pin={valid_values[0]};"
                                update_response = requests.put(
                                    f"{base_url}/open/envs",
                                    headers=headers,
                                    json={"id": env["id"], "name": "JD_COOKIE", "value": new_env_value}
                                )
                                # print("更新响应状态码：", update_response.status_code)
                                # print("更新响应内容：", update_response.text)
                                if update_response.status_code == 200:
                                    # 启用环境变量
                                    enable_response = requests.put(
                                        f"{base_url}/open/envs/enable",
                                        headers=headers,
                                        json=[env["id"]]
                                    )
                                    # print("启用响应状态码：", enable_response.status_code)
                                    # print("启用响应内容：", enable_response.text)
                                    if enable_response.status_code == 200:
                                        try:
                                            use1 = Env.objects.get(pin=valid_values[0])  # 使用正确的查询条件
                                            use1.ckvalue = new_env_value
                                            use1.status = 1  # 修改为正确的布尔值
                                            use1.save()
                                            return render(request, "index.html", {
                                                "msg": "登陆成功，有效期1~3天",
                                                "form": login_form
                                            })
                                        except Env.DoesNotExist:
                                            return render(request, "index.html", {
                                                "msg": "登陆成功，请前往主站重新登陆，获取推送二维码，谢谢!",
                                                "form": login_form
                                            })
                                    else:
                                        return render(request, "index.html", {
                                            "msg": "启用 pt_pin 失败,请稍后再试",
                                            "form": login_form
                                        })
                                else:
                                    return render(request, "index.html", {
                                        "msg": "更新 pt_pin 失败,请稍后再试",
                                        "form": login_form
                                    })
                        if not pt_pin_exists:
                            new_env_value = f"pt_key={valid_values[1]};pt_pin={valid_values[0]};"
                            add_response = requests.post(
                                f"{base_url}/open/envs",
                                headers=headers,
                                json=[{
                                    "name": "JD_COOKIE",
                                    "value": new_env_value,  # 将 value 作为字符串
                                    "remarks": jd_remark
                                }]
                            )
                            print("添加响应状态码：", add_response.status_code)
                            print("添加响应内容：", add_response.text)
                            if add_response.status_code == 200:
                                new_env_id = add_response.json()["data"][0]["id"]
                                # 启用新添加的环境变量
                                enable_response = requests.put(
                                    f"{base_url}/open/envs/enable",
                                    headers=headers,
                                    json=[new_env_id]
                                )
                                # print("启用响应状态码：", enable_response.status_code)
                                # print("启用响应内容：", enable_response.text)
                                if enable_response.status_code == 200:
                                    return render(request, "index.html", {
                                        "msg": "登陆成功，有效期1~3天",
                                        "form": login_form
                                    })
                                else:
                                    return render(request, "index.html", {
                                        "msg": "启用新的 pt_pin 失败",
                                        "form": login_form
                                    })
                            else:
                                return render(request, "index.html", {
                                    "msg": "添加新的 pt_pin 失败",
                                    "form": login_form
                                })
                    else:
                        return render(request, "index.html", {
                            "msg": "查询青龙环境变量失败，请联系网站管理员",
                            "form": login_form
                        })
                else:
                    token = get_ql_token(base_url, client_id, client_secret)
                    headers = {
                        "Authorization": f"Bearer {token}",
                        "Content-Type": "application/json"
                    }
                    search_value = valid_values[0]  # 使用 pin 作为查询条件
                    response = requests.get(f"{base_url}/open/envs?searchValue={search_value}", headers=headers)
                    # print("查询响应状态码：", response.status_code)
                    # print("查询响应内容：", response.text)
                    if response.status_code == 200:
                        envs = response.json()["data"]
                        pt_pin_exists = False
                        for env in envs:
                            if env["name"] == "JD_WSCK" and f"pin={valid_values[0]};" in env["value"]:
                                pt_pin_exists = True
                                new_env_value = f"wskey={valid_values[1]};pin={valid_values[0]};"
                                update_response = requests.put(
                                    f"{base_url}/open/envs",
                                    headers=headers,
                                    json={"id": env["id"], "name": "JD_WSCK", "value": new_env_value}
                                )
                                print("更新响应状态码：", update_response.status_code)
                                print("更新响应内容：", update_response.text)
                                if update_response.status_code == 200:
                                    # 启用环境变量
                                    enable_response = requests.put(
                                        f"{base_url}/open/envs/enable",
                                        headers=headers,
                                        json=[env["id"]]
                                    )
                                    # print("启用响应状态码：", enable_response.status_code)
                                    # print("启用响应内容：", enable_response.text)
                                    if enable_response.status_code == 200:
                                        try:
                                            return render(request, "index.html", {
                                                "msg": "登陆成功，有效期1~3天",
                                                "form": login_form
                                            })
                                        except Env.DoesNotExist:
                                            return render(request, "index.html", {
                                                "msg": "登陆成功，请前往主站重新登陆，获取推送二维码，谢谢!",
                                                "form": login_form
                                            })
                                    else:
                                        return render(request, "index.html", {
                                            "msg": "启用 wskey 失败",
                                            "form": login_form
                                        })
                                else:
                                    return render(request, "index.html", {
                                        "msg": "更新 wskey 失败",
                                        "form": login_form
                                    })
                        if not pt_pin_exists:
                            new_env_value = f"wskey={valid_values[1]};pin={valid_values[0]};"
                            add_response = requests.post(
                                f"{base_url}/open/envs",
                                headers=headers,
                                json=[{
                                    "name": "JD_WSCK",
                                    "value": new_env_value,  # 将 value 作为字符串
                                    "remarks": jd_remark
                                }]
                            )
                            # print("添加响应状态码：", add_response.status_code)
                            # print("添加响应内容：", add_response.text)
                            if add_response.status_code == 200:
                                new_env_id = add_response.json()["data"][0]["id"]
                                # 启用新添加的环境变量
                                enable_response = requests.put(
                                    f"{base_url}/open/envs/enable",
                                    headers=headers,
                                    json=[new_env_id]
                                )
                                # print("启用响应状态码：", enable_response.status_code)
                                # print("启用响应内容：", enable_response.text)
                                if enable_response.status_code == 200:
                                    return render(request, "index.html", {
                                        "msg": "登陆成功，有效期1~3天",
                                        "form": login_form
                                    })
                                else:
                                    return render(request, "index.html", {
                                        "msg": "启用新的 wskey 失败",
                                        "form": login_form
                                    })
                            else:
                                return render(request, "index.html", {
                                    "msg": "添加新的 wskey 失败",
                                    "form": login_form
                                })
                    else:
                        return render(request, "index.html", {
                            "msg": "查询青龙环境变量失败，请联系网站管理员",
                            "form": login_form
                        })
            except requests.RequestException as e:
                return render(request, "index.html", {
                    "msg": "请求青龙 API 出现异常，请联系网站管理员",
                    "form": login_form
                })
            except json.JSONDecodeError as e:
                return render(request, "index.html", {
                    "msg": "解析青龙 API 出现异常，请联系网站管理员",
                    "form": login_form
                })
            except Exception as e:
                return JsonResponse({"error": str(e)}, status=500)
        else:
            return render(request, "index.html", {
                "msg": "表单数据无效，请重新输入",
                "form": login_form
            })

    # 返回默认的渲染结果，用于 GET 请求
    return render(request, "index.html", {
        "msg": "欢迎使用查询JD-Pro系统",
        "form": login_form
    })
def user(request):
    user_form = UserRegisterForm(request.POST or None)
    if request.method == 'POST':
        if user_form.is_valid():
            username = user_form.cleaned_data['username']
            
            use = Env.objects.filter(Q(pin=username) | Q(uuid=username) | Q(remark=username))
            
            if use.exists():
                proceed_to_next_step = False
                results = []
                for obj in use:
                    results.append({
                        "pin": obj.pin,
                        "remark": obj.remark,
                        "uuid": obj.uuid,
                        "status": obj.status,
                        "wskey": obj.wskey,
                        "mck": obj.ckvalue,
                        "envt": obj.envt,
                        "id":obj.id,
                    })
                    if obj.status == 0:
                        proceed_to_next_step = True
                
                context = {
                    "msg": "数据存在",
                    "form": user_form,
                    "first_result": results,
                    "msg1": "账户已过期，请重新登陆后再查询<a href='https://pro.03vps.cn'>点我登陆</a>" if proceed_to_next_step else ""
                }
                return render(request, "user.html", context)
            else:
                return render(request, "user.html", {
                    "msg": "查询的数据不存在，请登陆后查询<a href='https://pro.03vps.cn'>点我登陆</a>",
                    "form": user_form
                })
        else:
            return render(request, "user.html", {
                "msg": "数据异常，请按照规则输入",
                "form": user_form
            })

    return render(request, "user.html", {
        "msg": "欢迎使用查询系统",
        "form": user_form
    })

