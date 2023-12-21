from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject


class CRUDCharityProject(CRUDBase):

    async def get_project_id_by_name(
        self,
        project_name: str,
        session: AsyncSession,
    ) -> Optional[int]:
        '''Получение id проекта по имени.'''
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
        '''Сортировка всех закрытых проектов.'''
        close_projects = await session.execute(
            select(CharityProject).where(
                CharityProject.fully_invested
            ).order_by(CharityProject.close_date - CharityProject.create_date))
        return close_projects.scalars().all()


charity_project_crud = CRUDCharityProject(CharityProject)
