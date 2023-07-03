h, m, s = map(int, input().split())
time = int(input())
h_to_m = h*60
m_to_s = (h_to_m+m)*60
total_s = m_to_s + s + time

s_to_m = total_s//60

m_to_h = s_to_m//60
s_to_m = s_to_m%60
s = total_s%60

if m_to_h >=24 :
    m_to_h %= 24
print(m_to_h, s_to_m, s)