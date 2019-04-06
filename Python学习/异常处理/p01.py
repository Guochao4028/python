
try:
    num = int(input("input number ?:"))
    print(100/num)
    #捕获异常后，把异常实例化，出错信息就会在实例化里
except ZeroDivisionError as e:
    print("error")
    # exit 是退出程序的意思
    # exit()
except Exception as  e:
    print(e)
else:
    print("has no")
finally:
    print("end")
print("h")


