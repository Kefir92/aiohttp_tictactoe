from database import (
    BaseModel,
    users
    )

class User(BaseModel):

    async def check_email(self, email=None):
        async with self.db.acquire() as conn:
            return await conn.execute(users.select(users.c.email == email))

    async def authenticate(self, email=None, password=None):
        async with self.db.acquire() as conn:
            return await conn.execute(users.select().where(users.c.email == email).where(users.c.password == password))        

    async def create(self, data=None):
        return await self.sql_transaction(users.insert().values(
            login=data['login'], email=data['email'],
            password=data['password']))

    async def one(self, id=None):
        async with self.db.acquire() as conn:
            result = await conn.execute(users.select().where(users.c.id == id))
            return await result.first()
