from django import template

register = template.Library()

@register.filter
def hide_sensitive_info(value):
    parts = value.split(';')  # 将字段内容按分号分割成多个部分
    result = []  # 存储处理后的结果
    for part in parts:
        key, _, _ = part.partition('=')  # 获取键名
        result.append(f"{key}=***")  # 将等号后面的内容替换为***
    return ';'.join(result)[:-4]