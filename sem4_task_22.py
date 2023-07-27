def create_list(prompt: str) -> list:
    size: int = int(input(f"Enter the size of {prompt} array: "))
    result_list: list = []
    for i in range(size):
        result_list.append(int(input(f"Enter {i} element: ")))
    return result_list


n_list: list = create_list("first")
m_list: list = create_list("first")


res_list: list = list(set(n_list + m_list))
res_list.sort()

print(res_list)
