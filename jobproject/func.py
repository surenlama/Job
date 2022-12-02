from django.template.loader import get_template, render_to_string
from weasyprint import HTML
from pathlib import Path
from django.conf import settings


def render_to_pdf(template_name, context=None, filename="document.pdf"):
    if context is None:
        context = {}
    html_string = render_to_string(template_name, context)
    html = HTML(string=html_string, base_url=context["base_url"])
    result = html.write_pdf(presentational_hints=True)
    created_file = Path(f"{settings.MEDIA_ROOT}/cv/")
    created_file.mkdir(parents=True, exist_ok=True)

    with open(created_file / filename, "wb") as file:
        file.write(result)
    return result