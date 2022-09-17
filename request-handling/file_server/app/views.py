import datetime

from django.shortcuts import render
from django.views.generic import TemplateView
from .settings import FILES_PATH
import os


class FileList(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, date=None):
        # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
        files = os.listdir(FILES_PATH)
        file_list = []
        result = {'files': file_list}
        for file in files:
            file_stat = os.stat(os.path.join(FILES_PATH, file))
            if date is not None:
                received_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
                if received_date == datetime.datetime.utcfromtimestamp(file_stat.st_ctime).date():
                    file_list.append(
                        {
                            'name': file,
                            'ctime': datetime.datetime.utcfromtimestamp(file_stat.st_ctime),
                            'mtime': datetime.datetime.utcfromtimestamp(file_stat.st_mtime)
                        })
                result['date'] = received_date

            else:
                file_list.append(
                            {
                                'name': file,
                                'ctime': datetime.datetime.utcfromtimestamp(file_stat.st_ctime),
                                'mtime': datetime.datetime.utcfromtimestamp(file_stat.st_mtime)
                            })
        return result


def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    path = os.path.join(FILES_PATH, name)
    with open(str(path), encoding='utf8') as f:
        file = f.read()
    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': file}
    )

