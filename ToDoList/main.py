from datetime import datetime, timedelta
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


def new_task(task_name, deadline_date):
    d_date = list(map(int, deadline_date.split("-")))
    new_row = Table(task=task_name, deadline=datetime(d_date[0], d_date[1], d_date[2]))
    session.add(new_row)
    session.commit()
    print("The task has been added!")


def show_tasks_today():
    today = datetime.today()
    print(f"Today {today.day} {today.strftime('%b')}:")

    rows = session.query(Table).filter(Table.deadline == today.date()).all()
    if len(rows) > 0:
        for index, row in enumerate(rows):
            print(f"{index + 1}. {row}")
    else:
        print("Nothing to do!")


def show_tasks_week():
    today = datetime.today()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for n in range(7):
        day = today + timedelta(days=n)
        print(f"{days[day.weekday()]} {day.day} {day.strftime('%b')}:")
        rows = session.query(Table).filter(Table.deadline == day.date()).all()
        if len(rows) > 0:
            for index, row in enumerate(rows):
                print(f"{index + 1}. {row}")
        else:
            print("Nothing to do!")
        print()


def show_tasks_all():
    print("All tasks:")

    rows = session.query(Table).order_by(Table.deadline).all()
    if len(rows) > 0:
        for index, row in enumerate(rows):
            print(f"{index + 1}. {row}. {row.deadline.day} {row.deadline.strftime('%b')}")
    else:
        print("Nothing to do!")
    print()


def missed_tasks():
    print("Missed tasks:")
    today = datetime.today()
    rows = session.query(Table).filter(Table.deadline < today.date()).all()
    if len(rows) > 0:
        for index, row in enumerate(rows):
            print(f"{index + 1}. {row}. {row.deadline.day} {row.deadline.strftime('%b')}")
    else:
        print("Nothing is missed!")
    print()


def delete_task():
    print("Choose the number of the task you want to delete:")
    rows = session.query(Table).order_by(Table.deadline).all()
    if len(rows) > 0:
        for index, row in enumerate(rows):
            print(f"{index + 1}. {row}. {row.deadline.day} {row.deadline.strftime('%b')}")
        num = input()
        specific_row = rows[int(num) - 1]
        session.delete(specific_row)
        session.commit()
        print("The task has been deleted!\n")
    else:
        print("Nothing to delete!")


def menu():
    while True:
        print("""1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit""")
        choice = input()
        if choice == "1":
            show_tasks_today()
        elif choice == "2":
            show_tasks_week()
        elif choice == "3":
            show_tasks_all()
        elif choice == "4":
            missed_tasks()
        elif choice == "5":
            task = input("Enter task:\n")
            dead_line = input("Enter deadline:\n")
            new_task(task, dead_line)
        elif choice == "6":
            delete_task()
        elif choice == "0":
            print("Bye!")
            break


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

menu()