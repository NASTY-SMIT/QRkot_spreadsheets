from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_superuser, current_user
from app.crud.donation import donation_crud
from app.models import User
from app.schemas.donation import DonationBase, DonationCreate, DonationDB
from app.services.investment import investment

router = APIRouter()


@router.post(
    '/',
    response_model=DonationCreate,
    response_model_exclude_none=True,)
async def create_donation(
    donation: DonationBase,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    """Для зарегестрированных юзеров.
    Создание пожертвования."""
    new_donation = await donation_crud.create(donation, session, user)
    await investment(new_donation, 'CharityProject', session)
    return new_donation


@router.get(
    '/',
    response_model=list[DonationDB],
    dependencies=[Depends(current_superuser)],
    response_model_exclude_none=True,)
async def get_all_donations(
    session: AsyncSession = Depends(get_async_session)
):
    """Только для суперюзеров.
    Получение списка всех пожертвований."""
    return (await donation_crud.get_multi(session))


@router.get(
    '/my',
    response_model=list[DonationCreate],)
async def get_my_reservations(
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    """Для зарегестрированных юзеров.
    Получение списка своих пожертвований."""
    return (await donation_crud.get_by_user(session=session, user=user))
