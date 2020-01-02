# Django连接远程数据库

> 2019-9-12 16:00 by `lidongdong`

参考资料：

<https://blog.csdn.net/nghuyong/article/details/54638474> 



## 步骤

1. 在Django项目的`settings.py`中配置数据库: 

   ```python
   # 例如:
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'mysql',
           'USER': 'root',
           'PASSWORD': '123456',
           'HOST': '192.168.186.136',
           'PORT': '3306',
       }
   }
   
   注意：'HOST'写的是虚拟机端的IP地址
   ```

2. 在虚拟机终端连接数据库并执行以下命令

   ```python
   GRANT ALL ON safeDb.* TO root@'%' IDENTIFIED BY 'xaut.qll'
   # 相当于授权，任何IP都可以连接
   ```

3. 执行如下命令

   ```shell
   python manage.py migrate    # 用来写入数据库
   ```

   

#### 说明：

​	如果运行代码之后报出     `NoneType`   错误，需要检查数据库的配置文件是否写对，如果浏览器中打不开，尝试调试manage文件 来定义IP和端口。

#### 