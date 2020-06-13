# url-survival-check

# 介绍
由于平时在做资产梳理的时候，往往会遇到对大量URL进行存活检测的工作，有时候有的URL使用http能打开，有的则使用https才能打开，手动去检测效率太低，因此简单写了一个批量检测工具。

# 安装
```
pip3 install requests
```
# 使用
```
python3 url_survival_check_min.py url.txt
python3 url_survival_check_max.py url.txt
```
# 注意事项
* `url_survival_check_min.py`的检测结果只有存活的URL，保存结果文件为`result_min.txt`
* `url_survival_check_max.py`的检测结果既包括存活的URL，也包括不存活的URL，保存结果文件为`result_max.txt`
# 使用示例
```
> python3 url_survival_check_min.py url.txt
http://xxx1.com  Not Survival
https://xxx1.com
http://xxx2.com
https://xxx2.com  Not Survival
```
```
> python3 url_survival_check_max.py url.txt
http://xxx1.com  Not Survival
https://xxx1.com
http://xxx2.com
https://xxx2.com  Not Survival
```
![](https://teamssix.oss-cn-hangzhou.aliyuncs.com/TeamsSix_Subscription_Logo2.png)
