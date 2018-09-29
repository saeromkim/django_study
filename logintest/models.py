from django.db import models

class Member(models.Model) :
		name = models.CharField(max_length=50, default="unknown")
		age = models.IntegerField(default='20')
		phone = models.CharField(max_length=50, default="010-0000-0000")

		user_id = models.CharField(max_length=50, default="unknown")
		user_pw = models.CharField(max_length=50, default="unknown")

		def __str__(self) :
			return self.name #테이블 이름이 나오게 