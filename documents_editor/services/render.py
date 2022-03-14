from docxtpl import DocxTemplate


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
        
        doc = DocxTemplate('forms/formtest.docx')
        context = {
            'name': form.name,
            'position': form.position,
            'rank': form.rank,
        }
        doc.render(context)
        doc.save('templates/tmp.docx')
        return 'успешно'
    
    @staticmethod
    @debug_errors
    def get_params_from_html_template(docx_template)-> str:
        doc = DocxTemplate(docx_template)
        parametrs = doc.get_undeclared_template_variables()
        return parametrs