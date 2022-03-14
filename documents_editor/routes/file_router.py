from fastapi import APIRouter
from fastapi.responses import JSONResponse
from schemas import form
from services.render import DocxRender
import mammoth
import os


router = APIRouter(
    prefix='/api/v1/files',
    tags=['files']
)

@router.get('/')
def get_templates():
    files = os.listdir('forms/')
    return files

@router.get('/{id}', response_model=form.DocumentParameters)
def get_parameters_from_docx(id: str):
    path = os.getcwd() + '/forms/'
    file = path + id
    parametrs = DocxRender.get_params_from_html_template(file)
    print(parametrs)
    # return parametrs

@router.get('/html-template/{id}')
def get_template_by_id(id: str):
    path = os.getcwd() + '/forms/'
    file = path + id
    with open(file, "rb") as docx_file:
        template = mammoth.convert_to_html(docx_file)    
    return template.value

@router.post('/{id}')
def format_template(model: form.OrderForm):
    if DocxRender.render_docx(model):
        return JSONResponse(content='success', status_code=201)
    else:
        return JSONResponse(content='error', status_code=402)
