from django.shortcuts import render,get_object_or_404,redirect
from main.models import Post
from .models import Comments
from .forms import CommentForm


# Create your views here.
# def post_comment(request,post_pk):
# 	post = get_object_or_404(Post,pk=post_pk)
# 	if request.method == 'Post':
# 		form = CommentForm(request.post)
# 		if form.is_valid():
# 			#生成实例。但还不保存
# 			comment = form.save(commit=False)
# 			comment.post = post
# 			comment.save()
# 			#重定向，以url为参数，或模型(含有get_absolute_url)实例
# 			return redirect(post)
# 		else:
# 			#类似于Post.objects.filter(post=post),由于有了post，且关系为Foreignkey
# 			comment_list = post.comment_set.all()
# 			context = {'post':post,'form':form,'comment_list':comment_list}
# 			return render(request,'main/comment.html',context=context)
# 	return redirect(post)

def comments(request):
	form = CommentForm()
	comment_list = Comments.objects.all()
	context = {'form':form,'comment_list':comment_list}
	return render(request,'main/comment.html',context=context)