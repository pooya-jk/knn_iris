__author__ = 'Pooya Koshanfar'

def find_smaller(first_num,second_num):
    if first_num>=second_num:
        return second_num
    else:
        return first_num

def find_avg(calculated_array):
    sum = 0
    for i in range(len(calculated_array)):
        sum += calculated_array[i][0]
    return sum/len(calculated_array)

def cal_dis(old_sample, new_sample):
    a1 = float(old_sample[0])
    b1 = float(old_sample[1])
    c1 = float(old_sample[2])
    d1 = float(old_sample[3])
    a2 = float(new_sample[0])
    b2 = float(new_sample[1])
    c2 = float(new_sample[2])
    d2 = float(new_sample[3])
    distance = abs((a1 - a2)) + abs((b1 - b2)) + abs((c1 - c2)) + abs((d1 - d2))
    return distance

def cal_dis_all(number_of_sample,old_samples,new_sample):
    calculated = []
    for i in range(number_of_sample):
        temp = []
        temp.append(cal_dis(old_samples[i],new_sample))
        temp.append(old_samples[i][4])
        calculated.append(temp)
    return calculated

def find_nearests(calculated_array):
    finded = []
    for i in range(len(calculated_array)):
        if calculated_array[i][0]<=find_avg(calculated_array):
            finded.append(calculated_array[i])
    return finded

def find_the_most(nearest_data):
    iris_setosa = 0
    iris_virsicolor = 0
    iris_virginica = 0
    for i in range(len(nearest_data)):
        if nearest_data[i][1] == 'Iris-setosa\r':
            iris_setosa += 1
        elif nearest_data[i][1] == 'Iris-versicolor\r':
            iris_virsicolor += 1
        else:
            iris_virginica += 1
    if iris_setosa>iris_virginica and iris_setosa>iris_virsicolor:
        return "iris_setosa"
    elif iris_setosa<iris_virginica and iris_virginica>iris_virsicolor:
        return "iris_virginica"
    elif iris_setosa<iris_virsicolor and iris_virginica<iris_virsicolor:
        return "iris_virsicolor"
    elif iris_virsicolor==iris_setosa and iris_virginica!=iris_setosa:
        return "not sure between iris_virsicolor and iris_setosa"
    elif iris_virsicolor!=iris_setosa and iris_virginica==iris_setosa:
        return "not sure between iris_virginica and iris_setosa"
    elif iris_virsicolor==iris_virginica and iris_virginica!=iris_setosa:
        return "not sure between iris-virginica and iris_virsicolor"
    elif iris_setosa==iris_virsicolor and iris_virginica==iris_virsicolor:
        return "not sure"

with open("Iris Dataset.txt", "r") as f:
    content = f.readlines()
for i in range(len(content)):
    content[i] = content[i].replace("\n", "")
    for j in range(4):
        newContent = content[i].split(",")
    content[i] = newContent
data = content
sepal_length = int(input("inter Sepal Length:"))
sepal_width = int(input("inter Sepal Width:"))
petal_lenght = int(input("inter Petal Length:"))
petal_width = int(input("inter Petal Length:"))
array = [sepal_length,sepal_width,petal_lenght,petal_width]
print(find_the_most(find_nearests(cal_dis_all(150,data,array))))
