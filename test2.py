import math
 
# 初始數據
initial_population = 100  # 初始細菌數量
target_population = 50000  # 目標細菌數量
doubling_time = 3  # 每次倍增所需的時間 (小時)
 
# 使用公式來計算達到目標所需的時間 t
time_required = doubling_time * math.log(target_population / initial_population) / math.log(2)
 
# 印出結果
print(f"The population will first reach 50,000 after approximately {time_required:.2f} hours.")