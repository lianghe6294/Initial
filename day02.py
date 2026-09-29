# day02.py · 名片生成器
# 目标：用 f-string 打印一张带分界线的名片

line = "=" * 30

name = input("请输入姓名：").strip()
job = input("请输入职位：").strip()
company = input("请输入公司：").strip()
phone = input("请输入电话：").strip()

print(line)
print("        个 人 名 片")
print(line)

print(f"姓名: {name}")
print(f"职位: {job}")
print(f"公司: {company}")
print(f"电话: {phone}")

print("-" * 30)

print(f"名字长度: {len(name)}个字")

print(line)
