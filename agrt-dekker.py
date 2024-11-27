# Algoritmo de Dekker (Exclusão Mútua para 2 Processos)
def dekker_algorithm():
    import threading
    import time

    turn = 0
    flag = [False, False]

    def process_0():
        nonlocal turn
        flag[0] = True
        while flag[1]:
            if turn != 0:
                flag[0] = False
                while turn != 0:
                    pass
                flag[0] = True
        print("Processo 0 na seção crítica")
        time.sleep(1)
        print("Processo 0 saindo da seção crítica")
        turn = 1
        flag[0] = False

    def process_1():
        nonlocal turn
        flag[1] = True
        while flag[0]:
            if turn != 1:
                flag[1] = False
                while turn != 1:
                    pass
                flag[1] = True
        print("Processo 1 na seção crítica")
        time.sleep(1)
        print("Processo 1 saindo da seção crítica")
        turn = 0
        flag[1] = False

    t0 = threading.Thread(target=process_0)
    t1 = threading.Thread(target=process_1)

    t0.start()
    t1.start()
    t0.join()
    t1.join()
