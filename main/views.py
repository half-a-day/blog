from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView
from .models import Post,Category
import markdown

# Create your views here.
#使用类视图
class IndexView(ListView):
	model = Post
	template_name = 'main/index.html'
	context_object_name = 'post_list'
	paginate_by = 8  #分页数

class PostDetailView(DetailView):
	model = Post
	template_name = 'main/detail.html'
	context_object_name = 'post'
	def get(self,request,*args,**kwargs):
		response = super(PostDetailView,self).get(request,*args,**kwargs)
		self.object.increased_views()
		return response
	def get_object(self,queryset=None):
		post = super(PostDetailView,self).get_object(queryset=None)
		post.content = markdown.markdown(post.content,extensions=[
			'markdown.extensions.extra',
			'markdown.extensions.codehilite',
			'markdown.extensions.toc',
			])
		return post

class ArchivesView(IndexView):
	def get_queryset(self):
		return super(Archives,self).get_queryset.filter(created_time__year=year,
		created_time__month=month)

#属性值与IndexView相同直接继承
class CategoryView(IndexView):
	def get_queryset(self):
		cate = get_object_or_404(Category,pk=self.kwargs.get('pk'))
		return super(CategoryView,self).get_queryset().filter(category=cate)
#get_queryset获取所有文章，使用super复写，过滤
