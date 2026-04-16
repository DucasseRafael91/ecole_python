from datetime import date
from ecole.models.teacher import Teacher
from ecole.models.course import Course


class MockCourse:
    def __init__(self):
        self.teacher = None
        self.students_taking_it = []


def test_teacher_str(mocker):
    teacher = Teacher(first_name="Alice", last_name="Dupont", age=22, hiring_date=date(2024, 1, 30))
    mocker.patch.object(teacher, '__str__', return_value="OK")
    expected_value = "OK"
    assert str(teacher) == expected_value


def test_teacher_add_course(mocker):
    teacher = Teacher(first_name="Alice", last_name="Dupont", age=22, hiring_date=date(2024, 1, 30))
    mock_course = MockCourse()
    teacher.add_course(mock_course)
    assert mock_course.teacher == teacher