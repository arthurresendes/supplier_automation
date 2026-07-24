from fastapi import APIRouter, status

router = APIRouter(prefix='/api/v1')

@router.get('/', tags=['GET'], summary='Rota base', status_code=status.HTTP_200_OK)
async def rota_base():
    return {'Message': 'Hello World'}