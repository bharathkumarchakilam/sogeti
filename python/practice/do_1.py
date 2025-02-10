T = int(input())
while T > 0:
    N, Q = map(int, input().split())
    people = {}
    for _ in range(N):
        name, age, hobbies, favourite_chocolate = input().split()
        people[name] = [age, hobbies, favourite_chocolate]
    for _ in range(Q):
        Query = input()
        if Query in people:
            print(", ".join(people[Query]))
    T -= 1
