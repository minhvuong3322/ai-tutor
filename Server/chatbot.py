import json

# mở và đọc data trong rules.json
with open("rules.json", "r", encoding="utf-8") as f:
    rules = json.load(f)

# sử lý chính
def get_response(user_input):
    user_input = user_input.lower()  

    matched_rules = []

    for rule in rules:
        for keyword in rule["keywords"]:
            if keyword.lower() in user_input: 
                matched_rules.append(rule)
                break

    if matched_rules:
        for rule in matched_rules:
            rule.setdefault("priority", 0)
        best_rule = max(matched_rules, key=lambda r: r["priority"])
        return best_rule["response"]

    return "Xin lỗi, tôi chưa hiểu câu hỏi."


# Cho phép test nhanh nếu chạy trực tiếp
if __name__ == "__main__":
    while True:
        user_input = input("Bạn: ")
        if user_input.lower() in ["thoát", "exit", "quit"]:
            break
        print("UTHBot:", get_response(user_input))
