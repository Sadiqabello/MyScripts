import os
import re

template_dir = 'templates'  # adjust this path

for root, dirs, files in os.walk(template_dir):
    for file in files:
        if file.endswith('.html'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r+', encoding='utf-8') as f:
                content = f.read()

                content = re.sub(
                    r'(href|src)=["\'](?!http)([^"\']+)["\']',
                    r'\1="{% static \'\2\' %}"',
                    content
                )

                if '{% load static %}' not in content:
                    content = '{% load static %}\n' + content

                f.seek(0)
                f.write(content)
                f.truncate()

