import os

TEMPLATE_DIR = 'templates'  # adjust this to your actual templates folder
APP_NAME = 'mainapp'

views = []
urls = []

for root, dirs, files in os.walk(TEMPLATE_DIR):
    for file in files:
        if file.endswith('.html'):
            rel_path = os.path.relpath(os.path.join(root, file), TEMPLATE_DIR)
            url_path = rel_path.replace('\\', '/').replace('.html', '')
            view_name = url_path.replace('/', '_').replace('-', '_')

            # Create view function
            views.append(f"""
def {view_name}(request):
    return render(request, '{rel_path.replace("\\\\", "/")}')
""")

            # Create URL path
            urls.append(f"    path('{url_path}/', views.{view_name}, name='{view_name}'),")

# Generate views.py content
views_py = """from django.shortcuts import render\n""" + ''.join(views)

# Generate urls.py content
urls_py = f"""from django.urls import path
from . import views

urlpatterns = [
{chr(10).join(urls)}
]
"""

# Output the files
with open(f'{APP_NAME}/views.py', 'w', encoding='utf-8') as vf:
    vf.write(views_py)

with open(f'{APP_NAME}/urls.py', 'w', encoding='utf-8') as uf:
    uf.write(urls_py)

print("✅ views.py and urls.py have been generated.")

