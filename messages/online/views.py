from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from online import models, forms
from online.forms import LiuyanForm
import logging

logging.basicConfig(level=logging.INFO)


@login_required
def liuyanlist(request):
    logging.info("access liuyanlist")
    content = {'messages': models.Info.get_infos()}
    return render(request, 'online/liuyanlist.html', content)


@login_required
def create(request):
    logging.info("access liuyanform")
    if request.method == 'POST':
        form = LiuyanForm(request.POST)
        if form.is_valid():
            logging.info("save liuyan info")
            models.Info.create_info(request.user.username, form.cleaned_data.get('title'), form.cleaned_data.get('content'))
            return HttpResponseRedirect('/online/')
        else:
            logging.info("部分信息为空，重新填写")
            form.add_error("部分信息为空，请重新填写")
            return render(request, 'online/liuyanform.html', {'form': form})
    else:
        logging.info("edit liuyan info")
        form = LiuyanForm()
        return render(request, 'online/liuyanform.html', {'form': form})


def delete(request):
    id = request.GET.get('id')
    models.Info.delete_info(id)
    return HttpResponseRedirect('/online/')



