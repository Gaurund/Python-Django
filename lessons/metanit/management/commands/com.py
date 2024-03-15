from django.core.management import BaseCommand
from metanit.models import Student, Course


def metanit():
    tom = Student.objects.create(name="Tom")
    tom.courses.create(name="Algebra")
    courses = Student.objects.get(name="Tom").courses.all()
    students = Student.objects.filter(courses__name="Algebra")
    print(students)
    python = Course.objects.filter(name="Python")
    print(python)
    python.student_set.create(name="Bob")
    sam = Student(name="Sam")
    sam.save()
    python.student_set.add(sam)
    students = python.student_set.all()
    print(students)
    number = python.student_set.count()
    print(number)
    python.student_set.remove(sam)
    python.student_set.clear()


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("client_pk", type=int)
        parser.add_argument(
            "--p",
            type=int,
            nargs="+",
            default=0
            )

    def handle(self, *args, **options):
        client_pk = options.get("client_pk")
        products = options.get("products")
        self.stdout.write(f"{client_pk}")
        self.stdout.write(f"{products}")
