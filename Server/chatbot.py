import json
import os
import random

# --- NẠP QUY TẮC TỪ FILE ---
base_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_path, "rules.json")

rules = []
try:
    with open(file_path, "r", encoding="utf-8") as f:
        rules = json.load(f)
    print(f"✅ Đã nạp {len(rules)} quy tắc từ rules.json")
except Exception as e:
    print(f"❌ Lỗi nạp rules.json: {e}")

# --- HÀM CHUẨN HÓA VĂN BẢN (XÓA DẤU) ---
def remove_accent(text):
    """Chuyển văn bản có dấu thành không dấu để so sánh linh hoạt hơn"""
    accents = {
        'á': 'a', 'à': 'a', 'ả': 'a', 'ã': 'a', 'ạ': 'a',
        'ă': 'a', 'ắ': 'a', 'ằ': 'a', 'ẳ': 'a', 'ẵ': 'a', 'ặ': 'a',
        'â': 'a', 'ấ': 'a', 'ầ': 'a', 'ẩ': 'a', 'ẫ': 'a', 'ậ': 'a',
        'đ': 'd',
        'é': 'e', 'è': 'e', 'ẻ': 'e', 'ẽ': 'e', 'ẹ': 'e',
        'ê': 'e', 'ế': 'e', 'ề': 'e', 'ể': 'e', 'ễ': 'e', 'ệ': 'e',
        'í': 'i', 'ì': 'i', 'ỉ': 'i', 'ĩ': 'i', 'ị': 'i',
        'ó': 'o', 'ò': 'o', 'ỏ': 'o', 'õ': 'o', 'ọ': 'o',
        'ô': 'o', 'ố': 'o', 'ồ': 'o', 'ổ': 'o', 'ỗ': 'o', 'ộ': 'o',
        'ơ': 'o', 'ớ': 'o', 'ờ': 'o', 'ở': 'o', 'ỡ': 'o', 'ợ': 'o',
        'ú': 'u', 'ù': 'u', 'ủ': 'u', 'ũ': 'u', 'ụ': 'u',
        'ư': 'u', 'ứ': 'u', 'ừ': 'u', 'ử': 'u', 'ữ': 'u', 'ự': 'u',
        'ý': 'y', 'ỳ': 'y', 'ỷ': 'y', 'ỹ': 'y', 'ỵ': 'y'
    }
    result = ""
    for char in text.lower():
        result += accents.get(char, char)
    return result

# --- HÀM TÌM KIẾM QUY TẮC PHÙ HỢP ---
def find_matching_rule(user_input):
    """
    Tìm quy tắc phù hợp nhất dựa trên keywords.
    Hỗ trợ so sánh cả có dấu và không dấu.
    CHỈ trả về rule khi có ít nhất 1 keyword khớp.
    """
    user_input_lower = user_input.lower()
    user_input_no_accent = remove_accent(user_input)
    
    best_match = None
    best_score = 0
    best_priority = -1
    
    for rule in rules:
        keywords = rule.get("keywords", [])
        score = 0
        
        for keyword in keywords:
            keyword_lower = keyword.lower()
            keyword_no_accent = remove_accent(keyword)
            
            # Kiểm tra cả có dấu và không dấu
            if keyword_lower in user_input_lower or keyword_no_accent in user_input_no_accent:
                score += 1
        
        # Chỉ xét rule nếu có ít nhất 1 keyword khớp
        if score > 0:
            priority = rule.get("priority", 0)
            
            # Ưu tiên: score cao hơn > priority cao hơn
            if score > best_score or (score == best_score and priority > best_priority):
                best_score = score
                best_priority = priority
                best_match = rule
    
    return best_match

# --- HÀM LẤY RESPONSE ---
def get_response_text(rule):
    """
    Lấy response từ rule.
    Hỗ trợ cả string và array (chọn ngẫu nhiên nếu là array).
    """
    response = rule.get("response", "Xin lỗi, mình không hiểu câu hỏi của bạn.")
    
    if isinstance(response, list):
        # Chọn ngẫu nhiên từ danh sách response
        return random.choice(response)
    else:
        return response

# --- HÀM XỬ LÝ CHÍNH ---
def get_response(user_input, session_id="default"):
    """
    Nhận input từ người dùng và trả về response phù hợp.
    """
    # Kiểm tra input rỗng
    if not user_input or not user_input.strip():
        return "Bạn chưa nhập câu hỏi."
    
    try:
        # Tìm quy tắc phù hợp
        matched_rule = find_matching_rule(user_input)
        
        if matched_rule:
            return get_response_text(matched_rule)
        else:
            return "Hiện tại mình chưa có thông tin cụ thể về vấn đề này. Bạn vui lòng liên hệ Phòng Đào tạo qua số (028) 3512-0756 nhé!"
    
    except Exception as e:
        print(f"Lỗi xử lý: {str(e)}")
        return "Xin lỗi, có lỗi hệ thống xảy ra."

if __name__ == "__main__":
    print("Testing Rule-Based Chatbot...")
    print("User: Xin chào")
    print("Bot:", get_response("Xin chào"))
    print("User: hoc phi")
    print("Bot:", get_response("hoc phi"))
    print("User: cntt")
    print("Bot:", get_response("cntt"))