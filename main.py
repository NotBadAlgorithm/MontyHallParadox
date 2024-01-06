import random

K = 10000000

def get_data():
    data = [0,0,1]
    random.shuffle([0,0,1])
    return data

def direct_strategy(data: list):
    return data[random.randint(0,2)]

def get_index_bad(data: list, i_ans):
    indexs_other = set((0,1,2)) - {i_ans}
    bads_indexs = []
    for i in indexs_other:
        if data[i] == 0:
            bads_indexs.append(i)
    return random.choice(bads_indexs)

def monty_hall_strategy(data: list):
    i_ans = random.randint(0,2)    
    i_bad = get_index_bad(data, i_ans)
    i_ans2 = list({0,1,2} - {i_ans, i_bad})[0]
    return data[i_ans2]


def main():
    cnt_direct = 0
    cnt_mh = 0
    for _ in range(K):
        data = get_data()
        cnt_direct += direct_strategy(data)
        cnt_mh += monty_hall_strategy(data) 
    
    print(f"probability Direct strategy: {100*cnt_direct/K:.2f}%")
    print(f"probability Monty Hall strategy: {100*cnt_mh/K:.2f}%")

if __name__ == "__main__":
    main()