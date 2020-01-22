def greeting(name, department):
    print("Welcome, " + name)
    print("You are a part of, " + department)


greeting("Nitin", "KVille")


def add(length, breadth):
    return length * breadth


print("Area of square: ", add(4, 4))


def convert_seconds(seconds):
    hour = seconds // 3600
    minutes = (seconds - (hour * 3600)) // 60
    remaining_seconds = (seconds - (hour * 3600) - (minutes * 60))
    return hour, minutes, remaining_seconds


hour, minutes, seconds = convert_seconds(5000)
print(hour, minutes, seconds)
