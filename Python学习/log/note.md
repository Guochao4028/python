# log
- logging 模块提供模块级别的函数记录日志
- 包括四大组件
## 1，日志相关概念
- 日志
- 日志级别（level）
    - 不同的用户关注不同的程序信息
    - debug
    - info
    - notice
    - warning
    - error
    - critical
    - alert
    - emergency 
 - io操作 不要频繁操作
 - log的作用
    - 调试
    - 了解运行情况
    - 分析定位
 - 日志信息
    - time
    - 地点
    - level
    - 内容
 - 成熟的第三方
    - log4j
    - log4php
    - logging
 # 2 logging模块
 - 日志级别
    - 级别可以自定义
    - debug
    - info
    - warning
    - error
    - critical
 - 初始化/写日志实例需要指定级别，只有当前级别等于或高于级别才会被记录
 - 使用方式
    - 直接使用logging（封装了其他组件）
    - logging四大组件直接定制
 # 2.1 logging模块级别的日志
 - 使用以下几个函数
    - logging.debug(msg, *args, **kwargs)创建一条严重级别为debug的日志记录
    - logging.info(msg, *args, **kwargs)创建一条严重级别为info的日志记录
    - logging.warning(msg, *args, **kwargs)创建一条严重级别为warning的日志记录
    - logging.error(msg, *args, **kwargs)创建一条严重级别为error的日志记录
    - logging.critical(msg, *args, **kwargs)创建一条严重级别为critical的日志记录
    - logging.log(level, *args, **kwargs)创建一条严重级别为level的日志记录
    - logging.basicConfig(**kwargs) 对 root logger进行一次性配置  
 - logging.basicConfig(**kwargs)
    - 只在第一次调用时起作用
    - 不配置logger则使用默认值
        - 输出 sys.stderr
        - 级别:warning
        - 格式 level：log_name：content
        - 详见01.py 
    - format 参数
    
            %(levelno)s: 打印日志级别的数值
            %(levelname)s: 打印日志级别名称
            %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
            %(filename)s: 打印当前执行程序名
            %(funcName)s: 打印日志的当前函数
            %(lineno)d: 打印日志的当前行号
            %(asctime)s: 打印日志的时间
            %(thread)d: 打印线程ID
            %(threadName)s: 打印线程名称
            %(process)d: 打印进程ID
            %(message)s: 打印日志信息
            
 # 2.1.logging模块的处理流程
 - 四大组件
    - 日志器（Logger）产生日志的一个接口
    - 处理器（Handler）把产生的日志发送到相应的目的地
    - 过滤器（Filter）更精细的控制那些日志输出
    - 格式器（Formatter）对输出信息进行格式化

    