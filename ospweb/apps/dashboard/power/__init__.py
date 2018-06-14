# coding=utf8
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import Q
from django.http import JsonResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from pure_pagination.mixins import PaginationMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from  django.http import  HttpResponse, JsonResponse, QueryDict
from django.conf import settings
from dashboard.models import UserProfile
from django.contrib.auth.models import  Permission
import json
import logging
import traceback
from  dashboard.forms import  PowerForm, PowerUpdateForm


logger = logging.getLogger('opsweb')




class PowerListView(LoginRequiredMixin, PaginationMixin, ListView):
    '''
    动作：getlist, create
    '''
    model = Permission
    template_name = "dashboard/power_list.html"
    context_object_name = "powerlist"
    paginate_by = 10
    keyword = ''

    def get_queryset(self):
        queryset = super(PowerListView, self).get_queryset()
        self.keyword = self.request.GET.get('keyword', '').strip()
        if self.keyword:
            queryset = queryset.filter(Q(name__icontains=self.keyword) |
                                       Q(codename__icontains=self.keyword))
        return queryset

    def get_context_data(self, **kwargs):
        context = super(PowerListView, self).get_context_data(**kwargs)
        context['keyword'] = self.keyword
        return context


    def post(self, request):
        form = PowerForm(request.POST)
        if form.is_valid():
            form.save()
            res = {'code': 0, 'result': '权限添加成功'}
        else:
            # form.errors会把验证不通过的信息以对象的形式传到前端，前端直接渲染即可
            res = {'code': 1, 'errmsg': form.errors}
        return JsonResponse(res, safe=True)


    def delete(self, request, *args, **kwargs):
        data = QueryDict(request.body)
        pk = data.get('id')
        try:
            perm  = self.model.objects.get(pk=pk)
            if perm.group_set.all() or  perm.user_set.all():
                res = {"code": 1, "errmsg": "删除错误请联系管理员"}
            else:
                self.model.objects.get(pk=pk).delete()
                res = {"code": 0, "errmsg": "删除成功"}

        except:
            res = {"code": 1, "errmsg": "删除错误请联系管理员"}
            #logger.error("")
        return JsonResponse(res, safe=True)


class PowerDetailView(LoginRequiredMixin, DetailView):

    model = Permission
    template_name = "dashboard/power_edit.html"
    context_object_name = 'power'
    next_url = '/dashboard/powerlist/'

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        p = self.model.objects.get(pk=pk)
        form = PowerUpdateForm(request.POST, instance=p)
        if form.is_valid():
            form.save()
            res = {"code": 0, "result": "更新成功", 'next_url': self.next_url}
        else:
            res = {"code": 1, "errmsg": form.errors, 'next_url': self.next_url}
            logger.error("delete power  error: %s" % traceback.format_exc())
        return render(request, settings.JUMP_PAGE, res)




