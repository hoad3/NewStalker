from collections import Counter
import underthesea
import re
# Văn bản đầu vào
def return_topic(content):

    # Phân đoạn văn bản thành các câu
    sentences = underthesea.sent_tokenize(content)

    # Tải danh sách từ dừng tiếng Việt từ một nguồn nào đó, ví dụ từ một tệp tin
    stopwords = set()
    with open("Stopwords.txt", "r", encoding="utf-8") as file:
        stopwords.update(file.read().splitlines())

    # Khởi tạo danh sách để lưu trữ từ khóa
    keywords = []

    # Loại bỏ các ký tự dấu và trích xuất từ khóa từ mỗi câu
    for sentence in sentences:
        # Loại bỏ các ký tự dấu (chấm, phẩy, ngoặc, dấu cách dư thừa, v.v.) bằng biểu thức chính quy
        sentence_cleaned = re.sub(r'[.,();:\[\]{}!?\\\-+*/"]', '', sentence)

        # Phân đoạn câu đã được làm sạch thành các từ
        words = underthesea.word_tokenize(sentence_cleaned)

        # Trích xuất từ khóa từ mỗi câu và loại bỏ các từ dừng
        for word in words:
            if word not in stopwords:
                keywords.append(word)

    # Thống kê số lần xuất hiện của từng từ khóa
    keyword_counts = Counter(keywords)

    sorted_keywords = sorted(keyword_counts.items(), key=lambda x: x[1], reverse=True)

    cleaned_text = re.sub(r'[.,();:\[\]{}!?\\\-+*/"\']', '', content)
    # Tách văn bản thành các từ bằng khoảng trắng
    words = cleaned_text.split()

    # Đếm số từ trong danh sách
    actual_word_count = 0
    for _, count in sorted_keywords:
        actual_word_count += count

    # In ra số từ
    print(f"Số từ trong văn bản là: {actual_word_count}")

    top_keywords = sorted_keywords[:15]

    to_dict = dict((keyword, count / actual_word_count) for keyword, count in top_keywords)

    # In ra danh sách các từ khóa
    print("Danh sách các từ khóa:")
    for keyword, count in top_keywords:  # Lấy 10 từ khóa xuất hiện nhiều nhất
        print(f"{keyword}: {count}")

    print("Từ khóa dạng dict:")
    print(to_dict)

    return to_dict