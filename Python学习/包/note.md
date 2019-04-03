# 1, 模块
- 一个模块就是一个包含Python代码的文件，后缀就是.py就可以，模块就是个Python文件
- 为什么我们用模块
    - 程序太大，编写维护需要拆分
    - 模块可以增加代码复用
    - 当做命名空间使用，避免命名冲突
 - 如果定义模块
    - 模块就是一个普通文件，所以任何代码直接书写
    - 不过需要规范
        - 函数（单一功能）
        - 类（相似功能的组合，或者类似业务模块）
        - 测试代码
  - 如使用模块
    - 直接导入
        - 假如模块名称直接以数字开头，需要借助于importlib帮助
            
                import importlib
                tuling = importlib.import_module("01)
                stu = tuling.Student()
        
    - 语法
        
            import module_name
            module_name.function_name
            module_name.class_name
    - import 模块 as 别名
        - 导入的同时给模块起一个别名
        - 其余用法跟第一种相同