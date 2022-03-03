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

@router.get('/{id}')
def get_template_by_id(id: str):
    path = os.getcwd() + '/forms/'
    file = path + id
    with open(file, "rb") as docx_file:
        template = mammoth.convert_to_html(docx_file)
    html = DocxRender.configurate_template(template.value)
    return html

@router.post('/{id}')
def format_template(model: form.OrderForm):
    if DocxRender.render_docx(model):
        return JSONResponse(content='success', status_code=201)
