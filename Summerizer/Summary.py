import nltk
nltk.download('stopwords')

from summarizer import Summarizer
def Return_summary(content):

    model = Summarizer()

    summary_dict = model(content)

    print("\n"
          "Tóm tắt văn bản:")
    print(summary_dict)


    return summary_dict


# Tách văn bản thành danh sách các từ
# words = content.split()


# Tạo từ điển để lưu số lần xuất hiện của các từ
# word_count_dict = defaultdict(int)

# Đếm số lần xuất hiện của các từ (loại bỏ từ ngừng)
# for word in words:
# Loại bỏ các ký tự đặc biệt và chuyển thành chữ thường để tránh phân biệt in hoa và thường

# Kiểm tra xem từ có trong danh sách từ ngừng không
# if word not in english_stopwords:
# word_count_dict[word] += 1

# In ra các từ xuất hiện nhiều nhất (top 10 ví dụ)
# top_words = sorted(word_count_dict.items(), key=lambda x: x[1], reverse=True)[:10]
# print("Top 10 từ xuất hiện nhiều nhất (loại bỏ từ ngừng):")
# for word, count in top_words:
# print(f"Từ '{word}' xuất hiện {count} lần trong văn bản.")
