from faker import Faker
from jobplus.models import db,User,Job
from random import randint


fake = Faker()


def iter_user():
    for i in range(randint(11,21)):
        yield User(
            username = fake.word(),
            email = fake.word(),
            password = '123456',
            role = 10,
            logo = fake.word(),
            companyname = fake.word(),
            website = fake.word(),
            address = fake.word(),
            intro = fake.word(),
            desc = fake.word(),
            is_disable = True

        )


def iter_company():
    for i in range(randint(11,21)):
        yield User(
            username = fake.word(),
            email = fake.word(),
            password = '123456',
            role = 20,
            logo = fake.word(),
            companyname = fake.word(),
            website = fake.word(),
            address = fake.word(),
            intro = fake.word(),
            desc = fake.word(),
            is_disable = True
            )

def iter_m_admin():
    yield User(
        username = '532604040@qq.com',
        email = '532604040@qq.com',
        password = '123456',
        role = 30,
        )

def iter_m_company():
    yield User(
        companyname = fake.word(),
        email = '532604040chris@qq.com',
        password = '123456',
        role = 20,
        )

def iter_m_user():
    yield User(
        username = fake.word(),
        email = '532604040@163.com',
        password = '123456',
        role = 10
        )
def iter_jobs():
    for i in range(randint(11,21)):
        yield Job(
            jobname = fake.word(),
            salary = fake.building_number(),
            exprequirement = fake.word(),
            edurequirement = fake.word(),
            address = fake.word(),
            desc = fake.word(),
            requirement = fake.word()
        )

def run():
    for job in iter_jobs():
        db.session.add(job)
    for company in iter_company():
        db.session.add(company)
    for user in iter_user():
        db.session.add(user)
    for one in iter_m_admin():
        db.session.add(one)
    for on in iter_m_user():
        db.session.add(on)
    for n in iter_m_company():
        db.session.add(n)
    try:
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback
