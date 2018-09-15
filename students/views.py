from django.shortcuts import render, redirect, reverse
from .models import StudentInfo, BanClass, StudentDetail


# Create your views here.


def index(request):
    return render(request, 'index.html')


def students_list(request):
    all_student = StudentInfo.objects.all()
    return render(request, 'students_list.html',
                  {'all_student': all_student})


def student_delete(request, stu_id):
    if stu_id:
        student = StudentInfo.objects.filter(id=int(stu_id))[0]
        print(student)
        # 删主先删子

        student.studentdetail.delete()  # 主对象.字表类名小写为对应的子对象。
        student.delete()
    return redirect(reverse('students:students_list'))


def student_update(request, stu_id):
    if stu_id:
        student = StudentInfo.objects.filter(id=int(stu_id))[0]  # 返回的是StudentInfo对象
        if request.method == 'GET':
            bans = BanClass.objects.all()
            return render(request, 'student_update.html', {
                'student': student, 'bans': bans})
        else:
            student.name = request.POST.get('stuname', '')
            student.age = int(request.POST.get('stuage', ''))
            student.gender = request.POST.get('stugender', '')
            stunum = request.POST.get('stunum', '')
            stuban = request.POST.get('stuban', '')
            student.banclass = BanClass.objects.filter(name=stuban)[0]  # 子对象与新班级对象关联
            student.save()

            # 原先找出原先的学生的详情的对象，把找出的详情对象中的学号改为新的学号

            studd = StudentDetail.objects.filter(studentinfo=student.id)  # 返回的是列表
            if not studd:  # 说明子表没有相关联的对象
                studd = StudentDetail()
                studd.studentinfo = student  # 将新子表对象与主表对象关联
            else:
                studd = studd[0]  # 取出对象
            studd.student_num = stunum  # 修改了 学号
            studd.save()

        return redirect(reverse('students:students_list'))


def student_add(request):
    if request.method == 'GET':
        bans = BanClass.objects.all()
        return render(request, 'student_add.html', {'bans': bans})
    else:
        # 找到班级对象，将新创建的学生加入
        n = request.POST.get('ban', '')
        ban = BanClass.objects.filter(name=n)[0]

        # 新学生对象，接收数据
        new_student = StudentInfo()
        new_student.name = request.POST.get('name', '')
        new_student.age = int(request.POST.get('age', 0))
        new_student.gender = request.POST.get('gender', '')

        # 学生对象关联班级
        new_student.banclass = ban

        new_student.save()

        # 创建新的学生详细信息对象
        new_stu_det = StudentDetail()
        new_stu_det.student_num = request.POST.get('stunum', '')

        # 关联 学生对象和详情对象
        new_stu_det.studentinfo = new_student  # 个人觉得理解为 给子表的关键字段赋值 更为妥当

        new_stu_det.save()


    return redirect(reverse('students:students_list'))
