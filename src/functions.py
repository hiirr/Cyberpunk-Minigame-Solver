import os
import random

# Fungsi yang digunakan untuk output
def print_matrix(matrix):
    for row in matrix:
        for elem in row:
            print(elem, end=" ") 
        print()
    return

def print_sequences(sequences, rewards):
    for i in range(1, len(sequences)+1):
        print(f"{i}. ")
        for j in i:
            print(j, end=" ")
        print(rewards[i])
    return

def print_steps(arraySteps, file=None):
    for i in range(len(arraySteps)):
        r = arraySteps[i][0] + 1  
        c = arraySteps[i][1] + 1  
        if file:
            print("{}, {}".format(r, c), file=file)
        else:
            print("{}, {}".format(r, c))
    return

def print_data(buffer_size, matrix, sequences, rewards):
    print("\n----- DATA YANG DIDAPATKAN -----")
    print("- Ukuran buffer :", buffer_size)
    print("- Ukuran matriks:", len(matrix), "x", len(matrix[0]))
    print("- Matriks       :")
    print_matrix(matrix)
    print("- Jumlah sekuens:", len(sequences))
    print("- Daftar sekuens:")
    for i, (sequence, reward) in enumerate(zip(sequences, rewards), start=1):
        print(f"  {i}. {' '.join(sequence)} memiliki bobot sebesar {reward}.")
    return

def output_cli(reward, tokens, steps, time):
    if reward == 0:
        print("Tidak ada solusi yang memenuhi.")
    else:
        print(reward)
        sequence = " ".join(tokens)
        print(sequence)
        print_steps(steps)
        print("")
        print(f"{int(time*1000)} ms")
    return

def output_txt(reward, tokens, steps, time, name):
    folder = "test"
    file = os.path.join(folder, name)

    with open(file, 'w') as file:
        file.write(str(reward) + "\n")
        sequence = " ".join(tokens)
        file.write(sequence)
        file.write("\n")
        print_steps(steps, file=file)
        file.write(f"\n{str(int(time*1000))} ms")

    print(f"Solusi telah di simpan pada '{name}.txt'.")
    print("\n|----          SEE YOU SOON!!          ----|")
    return

# Fungsi yang digunakan untuk input
def read_txt():
    buffer_size = 0
    matrix_cols = 0
    matrix_rows = 0
    matrix = []
    number_seq = 0
    sequences = []
    rewards = []
    belum = True

    while belum:
        file = input("\nMasukan nama file dengan format '.txt': ")
        path = os.path.join("test", file)
        
        if os.path.exists(path):
            belum = False
            try:
                with open(path, 'r') as file:
                    lines = [line.strip() for line in file.readlines()]

                    buffer_size = int(lines[0])
                    matrix_size = lines[1]
                    matrix_cols = int(matrix_size.split()[0])
                    matrix_rows = int(matrix_size.split()[1])
                    for i in range(2, 2 + matrix_rows):
                        elements = lines[i].split()
                        matrix.append(elements)
                    number_seq = int(lines[2 + matrix_rows])
                    for i in range(3 + matrix_rows, len(lines), 2):
                        sequence = lines[i].split()
                        reward = int(lines[i + 1])
                        sequences.append(sequence)
                        rewards.append(reward)
                    
                jawaban = input("\nApakah ingin melihat data yang dimuat? (Y/N) ")
                answer = jawaban.upper()
                if answer == 'Y':
                    print_data(buffer_size, matrix, sequences, rewards)

            except FileNotFoundError:
                print(f"Error: File {path} tidak dapat dibaca, pastikan file dalam bentuk '.txt'!")

        else:
            print(f"\nError: File dengan nama '{path}' tidak ditemukan!")
            jawaban = input("Apakah ingin mencoba lagi? (Y/N) ")
            answer = jawaban.upper()
            print("")
            if answer != 'Y':
                belum = False
                print("\n|----          SEE YOU SOON!!          ----|")
                return None, None, None, None
        
    return buffer_size, matrix, sequences, rewards

def random_sequences(tokens, maxSeq):
    length = random.randint(2, maxSeq)
    return random.choices(tokens, k=length)

def random_reward():
    num = random.randint(1, 100) 
    if num % 5 != 0 :
        return num + (5 - num % 5) 
    else:
        return num

def read_cli():
    # Token
    number_token = int(input("Jumlah token unik yang diinginkan: "))
    list_token = []
    for i in range(number_token):
        token_i = input(f"Token ke-{i+1}: ")
        list_token.append(token_i)

    # Buffer
    buffer_size = int(input("Masukan ukuran buffer yang diinginkan: "))

    # Matriks
    matrix_size = input("Masukan ukuran matriks yang diinginkan (kolom baris): ")
    matrix_col = int((matrix_size.split())[0])
    print(matrix_col)
    matrix_row = int((matrix_size.split())[1])
    print(matrix_row)
    matrix = [[random.choice(list_token) for _ in range(matrix_col)] for _ in range(matrix_row)]

    # Sekuens
    number_seq = int(input("Masukkan jumlah sekuens yang diinginkan: "))
    maximal_size_seq = int(input("Masukkan ukuran maksimal sekuens yang diinginkan: "))
    sequences = []
    for j in range(number_seq):
        sequence = random_sequences(list_token, maximal_size_seq)
        sequences.append(sequence)

    # Rewards
    rewards = []
    for k in range(number_seq):
        reward = random.randint(1, 50)
        rewards.append(reward)
    print_data(buffer_size, matrix, sequences, rewards)

    return buffer_size, matrix, sequences, rewards

# Fungsi yang digunakan untuk proses
def startMove0N(matrix, n):
    currentArray = []
    currentSteps = []
    for i in range(1, len(matrix)):
        array = []
        steps = []
        array.append(matrix[0][n])
        steps.append([0,n])
        array.append(matrix[i][n])
        steps.append([i,n])
        currentArray.append(array)
        currentSteps.append(steps)
    return currentArray, currentSteps

def horizontal_move(arrayBefore, stepsBefore, matrix):
    currentArray = []
    currentSteps = []
    for p in range(len(stepsBefore)):
        i = stepsBefore[p][len(stepsBefore[p])-1][0]
        for j in range(len(matrix[i])):
            old_array = arrayBefore[p]
            old_steps = stepsBefore[p]
            if [i,j] not in old_steps:
                new_steps = old_steps.copy()
                new_array = old_array.copy()
                new_array.append(matrix[i][j])
                new_steps.append([i,j])
                currentArray.append(new_array)
                currentSteps.append(new_steps)
            else:
                continue   

    return currentArray, currentSteps

def vertical_move(arrayBefore, stepsBefore, matrix):
    currentArray = []
    currentSteps = []
    for p in range(len(stepsBefore)):
        j = stepsBefore[p][len(stepsBefore[p])-1][1]
        for i in range(len(matrix)):
            old_array = arrayBefore[p]
            old_steps = stepsBefore[p]
            if [i,j] not in old_steps:
                new_steps = old_steps.copy()
                new_array = old_array.copy()
                new_array.append(matrix[i][j])
                new_steps.append([i,j])
                currentArray.append(new_array)
                currentSteps.append(new_steps)
            else:
                continue   

    return currentArray, currentSteps

def is_sequence_in_array(sequence, array):
    lengthSequence = len(sequence)
    lengthArray = len(array)
    if lengthSequence > lengthArray:
        return False
    for i in range(lengthArray - lengthSequence + 1):
        if array[i:i+lengthSequence] == sequence:
            return True
    return False

def process(bufferSize, matrix, sequences, rewards):
    saved_array = []
    saved_steps = []
    saved_reward = 0
    max_rewards = sum(rewards)

    for start in range(len(matrix[0])):
        arrayNow, stepsNow = startMove0N(matrix, start)
        for i in range(1, bufferSize-1):
            if i % 2 == 0:
                arrayNow, stepsNow = vertical_move(arrayNow, stepsNow, matrix)
            else:
                arrayNow, stepsNow = horizontal_move(arrayNow, stepsNow, matrix)

        for chance in range(len(arrayNow)):
            reward = 0
            for seq in range(len(sequences)):
                init = is_sequence_in_array(sequences[seq], arrayNow[chance])
                if init:
                    reward += rewards[seq]
            if reward > saved_reward:
                saved_reward = reward
                saved_array = arrayNow[chance]
                saved_steps = stepsNow[chance]
            if reward == max_rewards:
                saved_reward = reward
                saved_array = arrayNow[chance]
                saved_steps = stepsNow[chance]
                break

    return saved_reward, saved_array, saved_steps