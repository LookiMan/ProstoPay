from sqlalchemy import delete
from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker  # type: ignore
from sqlalchemy.future import select

from .models import User
from .schemas import UserDTO


class UserService:
    def __init__(self, async_session: async_sessionmaker[AsyncSession]) -> None:
        """Ініціалізація UserService з асинхронною сесією"""
        self.async_session = async_session

    async def get(self, user_id: int) -> UserDTO:
        """Отримання користувача за його ID"""
        async with self.async_session() as session:
            # Створення запиту для вибору користувача за ID
            stmt = select(User).where(User.id == user_id)
            # Виконання запиту та отримання користувача
            result = await session.execute(stmt)
            user = result.scalars().first()
            # Перевірка наявності користувача, якщо не існує - підняти помилку
            if user is None:
                raise ValueError(f"User with id {user_id} not found")
            # Конвертація користувача в UserDTO та повернення його з методу get
            return UserDTO(user_id=user.id, username=user.username, email=user.email)

    async def add(self, user: UserDTO) -> None:
        """Додавання нового користувача"""
        async with self.async_session() as session:
            new_user = User(id=user.user_id, username=user.username, email=user.email)
            # Додавання користувача до сесії
            session.add(new_user)
            # Збереження транзакції
            await session.commit()

    async def update(self, user: UserDTO) -> None:
        """Оновлення існуючого користувача"""
        async with self.async_session() as session:
            # Створення запиту для оновлення даних користувача
            stmt = update(User).where(User.id == user.user_id).values(
                username=user.username, email=user.email
            )
            # Виконання запиту на оновлення
            await session.execute(stmt)
            # Збереження транзакції
            await session.commit()

    async def delete(self, user_id: int) -> None:
        """Видалення користувача за його ID"""
        async with self.async_session() as session:
            # Створення запиту для видалення користувача за його ID
            stmt = delete(User).where(User.id == user_id)
            # Виконання запиту на видалення
            await session.execute(stmt)
            # Збереження транзакції
            await session.commit()
