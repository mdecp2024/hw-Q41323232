# 初始數據
initial_velocity_kmh = 310  # km/h
distance = 1000  # m
 
# 轉換初始速度為 m/s
initial_velocity = initial_velocity_kmh * 1000 / 3600  # m/s
 
# 設定最終速度為 0 (飛機停下)
final_velocity = 0  # m/s
 
# 使用運動學公式來解加速度
# v^2 = u^2 + 2as
# a = (v^2 - u^2) / (2 * s)
acceleration = (final_velocity**2 - initial_velocity**2) / (2 * distance)
 
# 印出結果
print(f"Required acceleration to stop the aircraft: {acceleration:.2f} m/s²")