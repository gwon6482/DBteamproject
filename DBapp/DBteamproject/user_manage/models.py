from django.db import models

# 여기에는 해당 앱에서 사용되는 모델들을 정의한다. 


#사용하려는 객체 생성 - 모델
#모델은 models.Moel을 상속받아야함
class user_c(models.Model):
    #모델의 필드들을 만들어줌
    #필드들은 models에서 각자 맞는 타입들을 상속받음
    username = models.CharField(max_length=32,verbose_name="사용자명")
    password = models.CharField(max_length=64,verbose_name="비밀번호")
    register_dttm = models.DateTimeField(auto_now_add=True, verbose_name="등록시간")


    #admin에서 확인했을때, 어떤 필드를 대표로 보여줄지 설정
    def __str__(self):
        return self.username

    #모델의 메타데이터 정의
    class Meta:
        #db_table : 데이터 베이스에 저장되는 테이블 명 설정    
        db_table = 'DBapp_user'
        #verbose_name : admin페이지에 표시되는 속성의 이름
        verbose_name = "사용자_구매자"
        #verbose_name_plural : 복수형 이름 (기본값은 s가 붙은 것)
        verbose_name_plural = "사용자_구매자"


