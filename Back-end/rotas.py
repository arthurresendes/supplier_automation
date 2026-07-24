from fastapi import APIRouter, status, File, HTTPException, UploadFile
import pandas as pd
import io

router = APIRouter(prefix='/api/v1')

@router.get('/', tags=['GET'], summary='Rota base', status_code=status.HTTP_200_OK)
async def rota_base():
    return {'Message': 'Hello World'}

@router.post('/transform-file', tags=['POST'], summary='Convertendo planilha (xlsx ou csv para json)', status_code=status.HTTP_201_CREATED)
async def conversao(file: UploadFile = File(...)):
    nome_arquivo = file.filename.lower()
    
    try:
        conteudo = await file.read()
        if nome_arquivo.endswith('.xlsx'):
            df = pd.read_excel(io.BytesIO(conteudo))
        elif nome_arquivo.endswith('.csv'):
            df = pd.read_csv(io.BytesIO(conteudo), encoding='utf-8')
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail='Arquivo não permitido. Envie apenas .csv ou .xlsx'
            )
        df = df.astype(object).where(pd.notna(df), None) # Trata como objeto e convere os nan para null
        res = df.to_dict(orient='records')
        return {'Result': res}

    except HTTPException as http_err:
        raise http_err
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, 
            detail=f'Erro ao processar o conteúdo do arquivo: {str(e)}'
        )