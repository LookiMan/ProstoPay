import unittest

from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker  # type: ignore

from ..config import DATABASE_URL
from ..models import Base
from ..schemas import UserDTO
from ..service import UserService


class TestUserService(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        self.engine: AsyncEngine = create_async_engine(DATABASE_URL)
        self.async_session = async_sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            expire_on_commit=False,
        )
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async def asyncTearDown(self) -> None:
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)

    async def test_add_and_get_user(self) -> None:
        service = UserService(self.async_session)
        user = UserDTO(user_id=1, username='test_user', email='test@example.com')

        await service.add(user)

        retrieved_user = await service.get(1)
        self.assertEqual(retrieved_user, user)

    async def test_get_non_existing_user(self) -> None:
        service = UserService(self.async_session)

        with self.assertRaises(ValueError):
            await service.get(2)

    async def test_add_user_with_existing_user_id(self) -> None:
        service = UserService(self.async_session)
        user = UserDTO(user_id=1, username='test_user', email='test@example.com')

        await service.add(user)

        with self.assertRaises(IntegrityError):
            await service.add(user)

    async def test_update_user(self) -> None:
        service = UserService(self.async_session)
        user = UserDTO(user_id=1, username='test_user', email='test@example.com')

        await service.add(user)

        updated_user = UserDTO(user_id=1, username='new_test_user', email='new_test@example.com')
        await service.update(updated_user)

        retrieved_user = await service.get(1)
        self.assertEqual(retrieved_user, updated_user)

    async def test_delete_user(self) -> None:
        service = UserService(self.async_session)
        user = UserDTO(user_id=1, username='test_user', email='test@example.com')

        await service.add(user)
        await service.delete(1)

        with self.assertRaises(ValueError):
            await service.get(1)


if __name__ == '__main__':
    unittest.main()
