from django.contrib import admin
from django.utils.translation import gettext as _
from django.utils.html import format_html
# Register your models here.
# 导入Django的admin模块
from django.contrib import admin
# 导入你的模型
from .models import Env, Efmigrationshistory, Containers

# 定义你的模型的admin类，可以自定义显示的字段，过滤器，搜索框等


class StatusFilter(admin.SimpleListFilter):
    title = '账户是否启用'
    parameter_name = '账户是否启用'

    def lookups(self, request, model_admin):
        return (
            ('valid', '启用☑'),
            ('invalid', '禁用❎'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'valid':
            return queryset.filter(status=True)
        elif self.value() == 'invalid':
            return queryset.filter(status=False)

class EnvTypeFilter(admin.SimpleListFilter):
    title = '登陆方式'
    parameter_name = '登陆方式'

    def lookups(self, request, model_admin):
        return (
            ('scan', '扫码登陆'),
            ('sms', '短信登陆'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'scan':
            return queryset.filter(envt='2')
        elif self.value() == 'sms':
            return queryset.exclude(envt='2')


class EnvAdmin(admin.ModelAdmin):
   def _abbreviate_field(self, field):
      return format_html('<span class="tooltip" title="{}">{}</span>', field, self._abbreviate_field_content(field))
   def _abbreviate_field_content(self, field):
      return (field[:15] + '...') if field and len(field) > 15 else (field or '')
#   def _abbreviate_field(self, field):
#      return (field[:15] + '...') if field and len(field) > 15 else (field or '')
   def abbreviate_pin(self, obj):
      return self._abbreviate_field(obj.pin)
   abbreviate_pin.short_description = _('京东账户名(pin)')
   def abbreviate_remark(self, obj):
      return self._abbreviate_field(obj.remark)
   abbreviate_remark.short_description = _('备注')
   def abbreviate_wskey(self, obj):
      return self._abbreviate_field(obj.wskey)
   abbreviate_wskey.short_description = _('京东扫码获取的wskey')
   def abbreviate_ckvalue(self, obj):
      return self._abbreviate_field(obj.ckvalue)
   abbreviate_ckvalue.short_description = _('京东短信获取的mck')
   def abbreviate_imgurl(self, obj):
      return self._abbreviate_field(obj.imgurl)
   abbreviate_imgurl.short_description = _('用户头像链接')
   def abbreviate_uuid(self, obj):
      return self._abbreviate_field(obj.uuid)
   abbreviate_uuid.short_description = _('消息推送平台的uuid')
   def is_status(self, obj):
      return format_html('<span class="tooltip" title="{}">{}</span>', obj.status, "启用☑️" if obj.status else "禁用❎")
   is_status.short_description = "账户是否启用"
   def is_envt(self, obj):
      return format_html('<span class="tooltip" title="{}">{}</span>', obj.envt, "短信登陆" if obj.envt == 0 else "扫码登陆")
   is_envt.short_description = "登陆方式"
   abbreviate_remark.allow_tags = True
   list_display = ('abbreviate_pin' , 'abbreviate_remark', 'abbreviate_wskey', 'abbreviate_ckvalue', 'abbreviate_imgurl', 'abbreviate_uuid', 'is_status', 'is_envt')
   list_display_links = ('abbreviate_pin', 'abbreviate_remark', 'abbreviate_wskey', 'abbreviate_ckvalue', 'abbreviate_imgurl', 'abbreviate_uuid', 'is_status', 'is_envt')
   class Media:
      css = {
         'all': ('admin/css/custom_admin.css',)
         }
      js = ('admin/js/custom_admin.js',)
   search_fields = ('pin', 'remark', 'wskey', 'ckvalue', 'uuid')
   list_filter = (StatusFilter, EnvTypeFilter)

class EfmigrationshistoryAdmin(admin.ModelAdmin):
   list_display = ('migrationid', 'productversion')
   search_fields = ('migrationid', 'productversion')

class ContainersAdmin(admin.ModelAdmin):
   list_display = ('id', 'level', 'name', 'description', 'type', 'url', 'wskeycount', 'ckcount', 'wpapptoken', 'status', 'clientid', 'clientsecret')
   search_fields = ('name', 'description', 'url', 'wpapptoken', 'clientid', 'clientsecret')
   list_filter = ('level', 'type', 'status')
      # 将你的模型和admin类注册到admin模块中
admin.site.register(Env, EnvAdmin)
admin.site.register(Efmigrationshistory, EfmigrationshistoryAdmin)
admin.site.register(Containers, ContainersAdmin)

