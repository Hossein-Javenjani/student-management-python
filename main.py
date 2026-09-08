from student_manager import StudentManager
stu = StudentManager()

while True :
    print (f'=====Student Management=====\n1.add student\n2.show student\n3.search_student\n4.delete_student\n5.edit_student\n6.save\n7.load\n8.exit')
    choosed = input("choose : \n")
    if choosed == '1' :
        print(f"{"=" * 10} add student {"=" * 10}")
        stu.add_stu()
    elif choosed == "2" :
        print(f'{"=" * 10} show student information {"=" * 10}')
        stu.show_stu()
    elif choosed == '3' :
        print(f'{"=" * 10} search student {"=" * 10}')
        stu.search()
    elif choosed == '4' :
        print(f'{"=" * 10} delete student {"=" * 10}')
        stu.delete()
    elif choosed == '5' :
        print(f'{"=" * 10} edit student {"=" * 10}')
        stu.edit()
    elif choosed == '6' :
        print(f'{"=" * 10} save student information {"=" * 10}')
        stu.save()
    elif choosed == '7' :
        print(f'{"=" * 10} load student information {"=" * 10}')
        stu.load()
    elif choosed == "8" :
        print("Goodbye!")
        break
    else :
        input("select true option!")
