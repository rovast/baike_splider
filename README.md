#baike_spider

抓取百度百科中，PHP词条 `http://baike.baidu.com/view/99.htm` 中出现的其他词条的 _url_ _词条标题_ _词条简介_ 数据，共计100条

> 此源码是参考慕课网上学习资源 `http://www.imooc.com/video/10692` 衍生而来，欢迎python初学者交流

思路：
1. 从页面中获取当前页面中词条相关的所有链接
2. 从给定的url中下载页面
3. 解析url页面，将有价值数据记录。将新的url补充进url管理器，将获取的词条标题等价值数据交于html输出器进行输出
4. html输出器将价值数据输出

## `splider_main.py` 总调度器
调度器主要用于整个业务逻辑的编写，负责协调各模块之间的关系

## `url_manager` url管理器
url管理器主要用于管理整个爬虫过程中涉及到的url，每当获取到新的url时就交给下载器进行下载，重复的url进行过滤。

## `html_downloader` html下载器
html下载器将url管理器交付过来的url进行下载，下载成功将内容给解析器进行解析，否则就返回下载失败

## `html_parser` html解析器
解析器将下载器的内容进行解析，将价值数据交付于输出器进行格式化输出，同时将页面中出现的新的url给url管理器进行管理

## `html_outputer` html输出器
将解析器传过来的价值数据进行格式化输出，便于浏览
