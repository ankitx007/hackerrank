def count_substring(string, substring):
    count = sum([ 1 for i in range(len(string)-len(substring)+1) if string[i:i+len(substring)] == substring])
    return(count)

string = input().strip()
sub_string = input().strip()
l = count_substring(string, sub_string)
print(l)
