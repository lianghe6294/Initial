# day03.py · BMI 计算器
# 目标：输入身高体重，算出 BMI，并按标准给出判断

print("=== BMI 计算器 ===")

# 提示用户输入身高和体重
name = input("请输入姓名:").strip()
height_str = input("请输入身高(cm):")
weight_str = input("请输入体重(kg):")

height = float(height_str)
weight = float(weight_str)

# 公式：BMI = 体重（kg） ÷ 身高的平方（m²）
height_m = height / 100
bmi = weight / (height_m ** 2)

print(f"{name}，你的 BMI 是:{bmi:.1f}")

# 判断标准：
#    小于 18.5         -> 偏瘦
#    18.5 到 24 之间   -> 正常
#    24 到 28 之间     -> 超重
#    28 及以上         -> 肥胖
if bmi < 18.5:
    print("偏瘦")
elif bmi < 24:
    print("正常")
elif bmi < 28:
    print("超重")
else:
    print("肥胖")

print("=== 计算完成 ===")