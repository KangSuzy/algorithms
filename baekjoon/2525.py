h, m = map(int, input().split())
end = int(input())

h += end // 60
m += end % 60

if m >= 60:
    h += 1
    m -= 60
if h >= 24:
    h -= 24

print(h,m)