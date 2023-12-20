from typing import Optional

from sqlalchemy import extract, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject


class CRUDCharityProject(CRUDBase):

    async def get_project_id_by_name(
        self,
        project_name: str,
        session: AsyncSession,
    ) -> Optional[int]:
        """Получение id проекта по имени."""
        db_project_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == project_name
            )
        )
        db_project_id = db_project_id.scalars().first()
        return db_project_id

    async def get_projects_by_completion_rate(
        self,
        session: AsyncSession
    ) -> list:
        """Сортировка всех закрытых проектов."""
        close_projects = await session.execute(
            select(CharityProject).where(
                CharityProject.fully_invested
            ).order_by(
                extract('year', CharityProject.close_date) - extract('year', CharityProject.create_date),
                extract('month', CharityProject.close_date) - extract('month', CharityProject.create_date),
                extract('day', CharityProject.close_date) - extract('day', CharityProject.create_date),
                extract('hour', CharityProject.close_date) - extract('hour', CharityProject.create_date),
                extract('minute', CharityProject.close_date) - extract('minute', CharityProject.create_date),
                extract('second', CharityProject.close_date) - extract('second', CharityProject.create_date),
            )
        )
        return close_projects.scalars().all()


charity_project_crud = CRUDCharityProject(CharityProject)
