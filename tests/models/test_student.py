from ecole.models.student import Student
from ecole.models.course import Course


class MockStudent:
    def __init__(self):
        self.student_nbr = 1
        self.courses_taken = []

    def __str__(self):
        return f"Bob Martin (20 ans), n° étudiant : {self.student_nbr}"

    def add_course(self, course):
        self.courses_taken.append(course)
        course.students_taking_it.append(self)


class MockCourse:
    def __init__(self):
        self.students_taking_it = []


def test_student_str(mocker):
    Student.students_nb = 0
    student = Student(first_name="Bob", last_name="Martin", age=20)

    mocker.patch.object(student, '__str__', return_value="100")

    expected_value = "100"
    assert str(student) == expected_value


def test_student_add_course(mocker):
    mock_student = MockStudent()
    mock_course = MockCourse()

    mocker.patch('ecole.models.student.Student', return_value=mock_student)

    student = Student(first_name="Bob", last_name="Martin", age=20)
    student.add_course(mock_course)

    assert mock_course in student.courses_taken
    assert student in mock_course.students_taking_it