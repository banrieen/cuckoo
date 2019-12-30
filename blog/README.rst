=====
Blog 作为 Django 模块打包部署
=====

Django 文档快速入手实例.

打包好的模块，快速安装方法
-----------

1. Add "blog" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'blog',
    ]
2. Include the blog URLconf in your project urls.py like this::

    path('blog/', include('blog.urls')),

3. Run `python manage.py migrate` to create the blog models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/blog/ to participate in the poll.

请参照：Django Doc 