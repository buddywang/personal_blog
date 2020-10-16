# personal_blog
## 注意：本项目只是一个博客系统项目，重点在系统本身，日常博客写在[blog](https://github.com/buddywang/blog/issues)里
### 个人博客系统
- 本博客系统主要参照杨仕航老师的Django2视频教程，由Django2配合bootstrap4构建，对应python版本为3.6，django版本为2.0.5，数据库用的是MySQL5.7
- [Demo](http://wgh.pythonanywhere.com/)
### 运行环境
- 除了python与Django外，所需第三方库在requirment.txt文件中，在你的主机安装即可（pip install -r requirment.txt)
### 使用
- 只需修改settings.py里数据库的配置，还要在你的主机上找到manage.py文件所在目录，运行命令
 pytho manage.py makemigrations 和 python manage.py migrate创建数据库，再修改HTML模板里的个人信息即可部署使用
