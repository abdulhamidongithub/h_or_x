from django.shortcuts import render
from .models import Words, Wrong


def index(request):
    return render(request, 'search/newindex.html')

def result(request):
        qidiruv_sozi = request.GET.get('searched')
        t_soz = Words.objects.filter(word=qidiruv_sozi)
        if len(t_soz)>0:
            n_soz = Wrong.objects.filter(words_id = t_soz[0].id)
            return render(request, 'search/newresult.html', {'t_soz': t_soz[0].word, 'n_soz': n_soz})
        else:
            not_soz = Wrong.objects.filter(wrong_one=qidiruv_sozi)
            if len(not_soz)>0:
                tog_soz = Words.objects.filter(word=not_soz[0].words_id)
                all_not_soz = Wrong.objects.filter(words_id=tog_soz[0].id)
                return render(request, 'search/newresult.html', {'t_soz': tog_soz[0].word, 'n_soz': all_not_soz})
            else:
                return render(request, 'search/newresult.html', {'t_soz': "Ma'lumotlar omborida bunday so'z yo'q!"})

