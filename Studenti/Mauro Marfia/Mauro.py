stanze = ["camera", "cucina", "salotto", "bagno", "camera da letto"]
tre_prese = [s for s in stanze if len(s) <= 5]
print(tre_prese)