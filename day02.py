# day02.py · 名片生成器
# 目标：用 f-string 打印一张带分界线的名片
# 规则：带 [补完] 标记的地方需要你自己写，其余不用动

line = "=" * 30

name = input("两河").strip()
# [补完 1] 照着上面这行，再写三行：职位 job、公司 company、电话 phone
job = input("AI应用开发工程师").strip()
company = input("XX有限公司").strip()
phone = input("10086").strip()

print(line)
print("        个 人 名 片")
print(line)

# [补完 2] 用 f-string 打印「姓名：」这一行
# 提示：print(f"姓名：{name}")，其余三行照着写
print(f"姓名: {name}")
print(f"职位: {job}")
print(f"公司: {company}")
print(f"电话: {phone}")

print("-" * 30)

# [补完 3] 打印名字长度，效果是「名字长度：2 个字」
# 提示：里面用 len(name)

print(f"名字长度: {len(name)}个字")

print(line)
