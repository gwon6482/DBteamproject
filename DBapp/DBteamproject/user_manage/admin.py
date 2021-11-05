from django.contrib import admin
from django.db import models
from .models import user_c

# 여기에 모델을 regist해야 admin페이지에서 직접 관리할 수 있다.
# 모델별로 Admin클래스를 정의하여야 한다.

#Admin클래스에서는 Admin상에서 보여지는 모델에 대하여 정의한다.
class user_cAdmin(admin.ModelAdmin):
    list_display = ('username','password','register_dttm')

#마지막으로 admin.site.register에서 매개변수로 모델과,Admin 클래스사용하여 실행하면
#등록이 완료된다. 
admin.site.register(user_c,user_cAdmin)