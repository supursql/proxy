# 爬虫代理池

---

### 概览
![](https://raw.githubusercontent.com/supursql/picGo/master/mdImg/20230706202032.png)

- **存储模块**: 使用 Redis 有序集合，负责代理的去重和状态标识
- **获取模块**: 从代理网站爬取代理，将爬取的代理传递给存储模块
- **检测模块**: 定时通过存储模块获取所有代理，并对代理进行检测，根据不同的检测结果对代理设置不同的标识
- **接口模块**: 通过暴露API提供服务接口

---

### 接口
```angular2html
/random     随机获取一个高分代理
/all        获取所有代理
/count      获取当前数据库中代理的数量
```

### 使用
1. 克隆代码
```angular2html
git clone git@github.com:supursql/proxy.git
cd proxy
```
2. 下载docker
3. docker运行
```angular2html
docker-compose -f build.yaml up
```