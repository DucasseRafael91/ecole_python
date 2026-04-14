from datetime import date
from ecole.models.course import Course
from ecole.models.student import Student
from ecole.models.teacher import Teacher


def test_set_teacher(mocker):
    course = Course(name="Maths", start_date=date(2024, 1, 28), end_date=date(2024, 1, 30))
    teacher = Teacher(first_name="Alice", last_name="Dupont", age=22, hiring_date=date(2024, 1, 30))


    mocker.patch.object(course, 'set_teacher', return_value=100)

    expected_value = '100'
    assert str(course.set_teacher(teacher)) == expected_value

def test_add_student(mocker):
    course = Course(name="Maths", start_date=date(2024, 1, 28), end_date=date(2024, 1, 30))
    student = Student(first_name="Bob", last_name="Martin", age=20)


    mocker.patch.object(course, 'add_student', return_value=100)

    expected_value = '100'
    assert str(course.add_student(student)) == expected_value


def test_course_str_without_teacher():
    course = Course(name="Maths",start_date=date(2024, 1, 28),end_date=date(2024, 1, 30))
    expected_value = "Maths (2024-01-28 – 2024-01-30),\npas d'enseignant affecté"
    assert str(course) == expected_value

def test_course_str_with_teacher():
    course = Course(name="Maths",start_date=date(2024, 1, 28),end_date=date(2024, 1, 30))
    teacher = Teacher(first_name="Alice", last_name="Dupont", age=22, hiring_date=date(2024, 1, 30))
    course.set_teacher(teacher)
    expected_value = f"Maths (2024-01-28 – 2024-01-30),\nenseigné par {teacher}"
    assert str(course) == expected_value


def test_course_attributes_without_teacher():
    course = Course(name="Maths",start_date=date(2024, 1, 28),end_date=date(2024, 1, 30))
    assert course.name == "Maths"
    assert course.start_date == date(2024, 1, 28)
    assert course.end_date == date(2024, 1, 30)

def test_course_attributes_with_teacher():
    course = Course(name="Maths",start_date=date(2024, 1, 28),end_date=date(2024, 1, 30))
    teacher = Teacher(first_name="Alice", last_name="Dupont", age=22, hiring_date=date(2024, 1, 30))
    course.set_teacher(teacher)
    assert course.name == "Maths"
    assert course.start_date == date(2024, 1, 28)
    assert course.end_date == date(2024, 1, 30)
    assert course.teacher.first_name == "Alice"
    assert course.teacher.last_name == "Dupont"
    assert course.teacher.age == 22
    assert course.teacher.hiring_date == date(2024, 1, 30)