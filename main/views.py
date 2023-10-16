from django.shortcuts import render
from django.views import View

from main.models import Todo


class HomeView(View):
    template_name = 'index.html'
    context = {}

    def get(self, request):
        works = Todo.objects.all()
        print(works)
        work_data = []
        for work in works:
            text = Todo.objects.filter(work=work).first()
            work_data.append(work)
        self.context.update({'products': work_data})
        return render(request, self.template_name, self.context)


