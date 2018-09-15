from django.db import models
from datetime import datetime

# Create your models here.


# 新建一个班级模型类
class BanClass(models.Model):
    name = models.CharField(max_length=30, verbose_name='班级')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '班级信息'
        verbose_name_plural = verbose_name


# 创建学生信息
class StudentInfo(models.Model):
    name = models.CharField(max_length=30, verbose_name='学生姓名')
    age = models.IntegerField(default=18, verbose_name='学生年龄')
    gender = models.CharField(max_length=10, choices=(('girl', '女'), ('boy', '男')), default='girl', verbose_name='性别')
    banclass = models.ForeignKey(BanClass, verbose_name='所属班级')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '学生信息'
        verbose_name_plural = verbose_name


# 学生详细信息
class StudentDetail(models.Model):
    student_num = models.CharField(max_length=30, verbose_name='学号')
    student_phone = models.CharField(max_length=11, verbose_name='手机')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    studentinfo = models.OneToOneField(StudentInfo, verbose_name='所属学生')

    def __str__(self):
        return self.student_num

    class Meta:
        verbose_name = '学生详细信息'
        verbose_name_plural = verbose_name
