"""Ngày 2: Các khái niệm Python cần cho nghiên cứu AI."""
scores = [6, 8, 9, 7]

def average(values):
    return sum(values) / len(values)

def count_pass(values, threshold=7):
    count = 0
    for score in values:
        if score >= threshold:
            count += 1
    return count

print('Điểm:', scores)
print('Trung bình:', average(scores))
for threshold in (6, 7, 8):
    print('Đạt từ', threshold, ':', count_pass(scores, threshold))
