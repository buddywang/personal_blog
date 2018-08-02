from django.shortcuts import render,get_list_or_404,get_object_or_404
from .models import Article,BlogType,ReadNum
from django.http import HttpResponseRedirect,HttpResponse
from .forms import SearchForm
from django.db.models import Count
from django.core.paginator import Paginator

# Create your views here.
#公共
def get_common_paginator(request,art_all):
    context = {}
    paginator = Paginator(art_all, 6)  # 每页10篇文章
    page_num = request.GET.get('page', 1)  # 获取URL的页面参数
    blog_of_page = paginator.get_page(page_num)  # 获取当前页码的文章
    date_lists = Article.objects.dates('date', 'month', order='DESC')  # 日期归档列表
    date_lists_dict = {}   #********
    for date_list in date_lists:
        date_count = Article.objects.filter(date__year=date_list.year,date__month=date_list.month).count()
        date_lists_dict[date_list] = date_count
    art_types = BlogType.objects.annotate(blog_count=Count('article'))
    # for art_type in art_types:
    #     art_type.num = Article.objects.filter(blogtype=art_type).count()
    page_list = list(range(max(blog_of_page.number - 2, 1), min(blog_of_page.number + 2, paginator.num_pages) + 1))  # 页码列表
    # 分页列表
    if blog_of_page.number == 4:
        page_list.insert(0, 1)
    if blog_of_page.number >= 5:
        page_list.insert(0, 1)
        page_list.insert(1, '...')
    if blog_of_page.number == paginator.num_pages - 3:
        page_list.append(paginator.num_pages)
    if blog_of_page.number <= paginator.num_pages - 4:
        page_list.append('...')
        page_list.append(paginator.num_pages)
    context['page_list'] = page_list
    context['art_lists'] = blog_of_page
    context['result_num'] = paginator.count
    context['date_lists_dict'] = date_lists_dict
    context['art_types'] = art_types
    return context

#博客主页处理
def index_handler(request):
    art_all = Article.objects.all().order_by('-date')
    form = SearchForm()
    context = get_common_paginator(request,art_all)
    context['result_title'] = '全部文章'
    context['form'] = form
    context['issearchpage'] = 0
    return render(request, 'index.html',context)

#文章详情处理
def detail_handler(request,id):
    article = get_object_or_404(Article,id=id)
    #阅读计数
    if not request.COOKIES.get('blog_%s_readed' % id ):
        if ReadNum.objects.filter(blog=article).count():
            #存在记录
            readnum = ReadNum.objects.get(blog=article)
        else:
            #不存在记录
            readnum = ReadNum(blog=article)
        readnum.read_num += 1
        readnum.save()

    previous_blog = Article.objects.filter(id__gt=id).last()
    next_blog = Article.objects.filter(id__lt=id).first()
    form = SearchForm()
    context = {}
    context['art'] = article
    context['form'] = form
    context['previous_blog'] = previous_blog
    context['next_blog'] = next_blog
    response = render(request,'detail.html', context)
    response.set_cookie('blog_%s_readed' % id ,'true')
    return response

#搜索功能
def Search(request):
    #实例搜索表单
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            searchkey=form.cleaned_data['search_key']
    else:
        form = SearchForm()
    if request.GET.get('search_key'):
        searchkey = str(request.GET.get('search_key'))

    art_all = Article.objects.filter(title__icontains=searchkey)
    context = context = get_common_paginator(request,art_all)
    context['result_title'] = searchkey+' 搜索结果'
    context['form'] = form
    context['searchkey'] = searchkey
    context['issearchpage'] = 1
    return render(request, 'index.html', context)

#文章分类页面处理
def article_with_type(request, Blogtype):
    btype = get_object_or_404(BlogType,blog_type=Blogtype)
    art_all = Article.objects.filter(blogtype=btype).order_by('-date')
    form = SearchForm()
    context = context = get_common_paginator(request,art_all)
    context['result_title'] = Blogtype+' 相关'
    context['form'] = form
    context['issearchpage'] = 0
    return render(request, 'index.html', context)

#日期分类页面处理
def article_with_date(request, year, month):
    art_all = Article.objects.filter(date__year=year,date__month=month).order_by('-date')
    form = SearchForm()
    context = context = get_common_paginator(request,art_all)
    context['result_title'] = '日期归档 '+str(year)+'/'+str(month)
    context['form'] = form
    context['issearchpage'] = 0
    return render(request, 'index.html', context)

#网站首页处理
def home_handler(request):
    return render(request,'home.html')