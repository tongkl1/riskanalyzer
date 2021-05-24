# A股上市公司财务分析器

本项目是一款对A股上市公司进行财务分析、识别财务风险的工具.

# 部署

部署需保证5 GB的硬盘空间以应对将来可能使用的大型数据表. 作为参考, A股从1990年至今的日线行情约2 GB.

在部署前, 请确保你安装了Python 3.7及一个合理的数据库. 推荐使用MySQL, MariaDB, PostgreSQL, Oracle, etc. 轻量级的SQLite据说配置得好也能支持每秒十万级的并发, 但我没有相关经验.

首先, clone本项目到本地:

``` bash
git clone https://github.com/tongkl1/riskanalyzer
```

在项目文件夹下, 安装必须的Python包:

``` bash
python -m pip install -r requirements.txt
```

有时, 你使用的数据库与Python的接口包(如pymysql)在安装时会报错, 这多半是因为你缺少了某些必要的库, 请自行谷歌解决. 例如, MySQL的语境下, 一般可通过运行yum install mysql-devel或apt install libmysqlclient-dev解决.

成功运行后, 在数据库中建立一个项目专用数据库和用户, 并向用户授权此数据库的所有权限. 例如, 在MySQL的root用户下执行如下指令:

``` sql
create database riskanalyzer;
create user riskanalyzeruser identified by '123456';
grant all privileges on riskanalyzer.* to riskanalyzeruser;
```

然后, 在项目文件夹的riskanalyzer/settings.py中设置数据库连接方式. 上述数据库名和用户对应如下设置:

``` python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'riskanalyzer',
        'USER': 'riskanalyzeruser',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {'charset':'utf8mb4'},
    }
}
```

然后, 运行下列命令以执行数据库的初始化.

``` bash
python manage.py makemigrations
python manage.py migrate
```

[可选] 你还可以创建一个管理员用户以便查看数据表.

``` bash
python manage.py createsuperuser
```

# 运行

目前, 程序的运行仍然需要手工完成.

## 拉取数据

要拉取数据, 请在项目文件夹下执行如下命令.

``` bash
python manage.py shell
```

在生成的shell环境下运行下列语句:

``` python
from datafetcher.CSMARDataFetcher import CSMARDataFetcher
f = CSMARDataFetcher()
f.update_list()
f.fetch_all()
```

最后一条命令可能需要花费至多半小时下载所有数据. 如果运行正常, 你应该能够在数据库中的相关表中查询到所有数据.

# 汇报bug

如有bug, 请在本工程的issue页面提交.

# 工程进度

- [x] 财务数据及基本数据的获取
- [x] 财务指标计算 (2/10)
- [ ] 数据接口
- [ ] 界面开发
