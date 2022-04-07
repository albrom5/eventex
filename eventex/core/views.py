from django.views.generic import DetailView
from django.views.generic.list import ListView

from eventex.core.models import Speaker, Talk


home = ListView.as_view(template_name='index.html',
                        model=Speaker)

# def home(request):
#     speakers = Speaker.objects.all()
#
#     return render(request, 'index.html', {'speakers': speakers})

# def speaker_detail(request, slug):
#     speaker = get_object_or_404(Speaker, slug=slug)
#
#     return render(request, 'core/speaker_detail.html', {'speaker': speaker})

speaker_detail = DetailView.as_view(model=Speaker)

# def talk_list(request):
#     context = {
#         'morning_talks': Talk.objects.at_morning(),
#         'afternoon_talks': Talk.objects.at_afternoon(),
#     }
#     return render(request, 'core/talk_list.html', context)

talk_list = ListView.as_view(model=Talk)