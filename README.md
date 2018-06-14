
# Confd_Web 配置管理平台





环境:

	CentOS 6/7 x64
	Python:  2.7.6
	Etcd： 3.2.18
	Confd:  0.16.0
	Nginx: 1.12.1


## 一.拓扑图:



![image](https://github.com/1032231418/PYVM/blob/master/conf_web_images/tuopu.png)	


## 二．涉及软件

	etcd：分布式KV存储系统，一般用于共享配置和服务注册与发现。是CoreOS公司发起的一个开源项目。 ETCD存储格式类似于文件系统，以根"/"开始下面一级级目录，最后一个是Key，一个key对应一个Value。
	etcd集群：使用Raft协议保证每个节点数据一致，由多个节点对外提供服务。这里只用单台。

	confd：管理本地应用配置文件，使用etcd或consul存储的数据渲染模板，还支持redis、zookeeper等。
	confd有一个watch功能，通过HTTP API定期监测对应的etcd中目录变化，获取最新的Value，然后渲染模板
	Nginx:  Nginx是一款轻量级的Web服务器/反向代理服务器以及电子邮件代理服务器，并在一个BSD-like协议下发行。由俄罗斯的程序设计师lgor Sysoev所开发，供俄国大型的入口网站及搜索引擎Rambler使用。其特点是占有内存少，并发能力强，事实上nginx的并发能力确实在同类型的网页服务器中表现较好。

## 三．软件部署

	环境说明:  建议使用 Cento7.X  X64
	
	1)安装etcd(这里安装的单机,集群环境根据自己的需求选取)
	
		# yum install etcd -y
		# sed -i  's/localhost/0.0.0.0/g'  /etc/etcd/etcd.conf  #配置监听地址
		# systemctl   start  etcd  &&  systemctl  enable  etcd  #启动服务设置开机动

	2)安装nginx
	
		#cd  /usr/local/src
		#wget  http://nginx.org/download/nginx-1.12.1.tar.gz
		#git clone https://github.com/yaoweibin/nginx_upstream_check_module.git  
		#tar  -zxvf  nginx-1.12.1.tar.gz 
		#cd nginx-1.12.1
		#patch  -p1 </usr/local/src/nginx_upstream_check_module/check_1.12.1+.patch
		#./configure   --prefix=/usr/local/nginx --add-module=/usr/local/src/nginx_upstream_check_module/
		make && make install
		#mkdir  /usr/local/nginx/conf/vhost/
		
![image](https://github.com/1032231418/PYVM/blob/master/conf_web_images/nginx.png)	

