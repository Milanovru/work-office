from docxtpl import DocxTemplate
import re


def debug_errors(func):
    def wrapper(args):
        try:
            return func(args)
        except Exception as e:
            return e
    return wrapper
    

class DocxRender:

    @staticmethod
    @debug_errors
    def render_docx(form) -> str:
        """
        form = (position='string', rank='string', name='string').
        """
        
        doc = DocxTemplate('forms/test.docx')
        context = {
            'name': form.name,
            'position': form.position,
            'rank': form.rank,
        }
        doc.render(context)
        doc.save('templates/tmp.docx')
        return 'успешно'
    
    @staticmethod
    def configurate_template(html_template)-> str:
        index = 0
        while True:
            regex = re.search(r'{{\w*}}', html_template[index:])  # ищет паттерн {{ }}
            if regex:
                tag_class, tag_placeholder = DocxRender.generate_input_attribute(regex.group(0))
                pattern = f'<input type="text" class="input-data input-{tag_class}" placeholder={tag_placeholder}>'
                html_template = html_template.replace(
                    regex.group(0), pattern)  # заменяет паттерн на тег
                index += regex.end()  # начало поиска передвигается на место, где произошла замена
            else:
                index += 1
            if index == len(html_template):
                return html_template

    @classmethod
    def generate_input_attribute(cls, tag: str) -> tuple:
        """Принимает строку ввиде объекта шаблонизатора и возвращает класс и плайсхолден для тега.

        Args:
            tag (str): {{ tag }}

        Returns:
            tuple: название класса, текст для плейсхолдера
        """
        if tag == '{{position}}':
            return 'position', 'Должность'
        elif tag == '{{rank}}':
            return 'rank', 'Звание'
        elif tag == '{{name}}':
            return 'name', 'Фамилия_И.О.'