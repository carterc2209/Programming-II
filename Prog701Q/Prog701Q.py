from helperProg701Q import *


def main():
    try:
        people: list[Vehicle] = []
        with open("../Langdat/prog702q.txt", 'r') as f:
            num = int(f.readline())
            while num != 401:
                name = f.readline()
                tires = f.readline()
                if num == 1:
                    worth = int(f.readline())
                    p = Cars(name, tires, worth)
                    people.append(p)
                elif num == 2:
                    miles = int(f.readline())
                    p = Trucks(name, tires, miles)
                    people.append(p)
                elif num == 3:
                    home = str(f.readline()).strip()
                    p = Busses(name, tires, home)
                    people.append(p)
                # num = int(f.readline())
            tot = 0.0
            cnt = 0
            tot_stus = 0
            large = ""
            small = "qadsf;ljyhtertfhdjklafhdjksafhdsjufhdsjkfhdskjfhdskjfhdsjfhdrsafudhsguofdsahiurhgeuishnugfidshghrweavhduigfiugfhdjgfdhsgoifdahgkfdkhglkfdhgklfdgjfdklgjfdklgjfdsklsgjfdgfjdsglkfdjglfdkjgfdklgjkfdsgkljfdgkljfdslkjgkjldfy"
            for person in people:
                if isinstance(person, Cars):
                    tot += person.gpa
                    cnt += 1
                elif isinstance(person, Trucks):
                    tot_stus += person.num_stu
                elif isinstance(person, Busses):
                    fw = person.fav_word
                    if len(fw) > len(large):
                        large = fw
                    if len(fw) < len(small):
                        small = fw
            print("Average Student GPA:", round(tot/cnt, 2))
            print("Total number of student taught:", tot_stus)
            print("Smallest favorite admin word:", small)
            print("Largest favorite admin word:", large)
    except OSError as e:
        print("Error:", e)
    pass


if __name__ == "__main__":
    main()
