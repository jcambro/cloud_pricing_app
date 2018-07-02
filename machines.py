#Returns the correct machines for cloud computing app

#Lists keep the machine together with the base price
amazon_normal = [("t2.small, 2(GB), 1, ", 10.51),
                ("t2.large, 4(GB), 2, ", 41.98),
                ("t2.xlarge, 16(GB), 4, ", 97.09),
                ("t2.2xlarge, 32(GB), 8, ", 167.90),
                ("m5.4xlarge, 64(GB), 16, ", 358.43)
                ]

amazon_optimized = [("c5.xlarge, 8(GB), 4, ", 78.84),
                    ("c5.4xlarge, 32(GB), 16, ", 315.36),
                    ("r4.xlarge, 30.5(GB), 4, ", 122.64),
                    ("r4.2xlarge, 61(GB), 8, ", 245.28),
                    ]

google_normal = [("n1-standard-1, 3.75(GB), 1, ", 24.27),
                ("n1-standard-2, 7.5(GB), 2, ", 48.55),
                ("n1-standard-4, 15(GB), 4, ", 97.09),
                ("n1-standard-8, 30(GB), 8, ", 194.18),
                ("n1-standard-16, 60(GB), 16, ", 388.36),
                ]

google_optimized = [("n1-highcpu-4, 3.6(GB), 4, ", 72.46),
                    ("n1-highcpu-16, 14.4(GB), 16, ", 289.84),
                    ("n1-highmem-4, 26(GB), 4, ", 121.0),
                    ("n1-highmem-8, 52(GB), 8, ", 242.0),
                    ]

miserver_normal = [("server1, 2(GB), 1, ", 16.795),
                    ("server2, 4(GB), 2, ", 31.295),
                    ("server3, 16(GB), 4, ", 118.295),
                    ("server4, 32(GB), 8, ", 234.295),
                    ("server5, 64(GB), 8, ", 466.295),
                    ]

def get_cpu_machine(CPU, storage):
    #default value
    machine = [amazon_normal[0], google_normal[0], miserver_normal[0]]
    output = ["", "", ""]

    if CPU <= 1:
        machine[0] = amazon_normal[0]
        machine[1] = google_normal[0]
        machine[2] = miserver_normal[0]
    elif CPU <= 2:
        machine[0] = amazon_normal[1]
        machine[1] = google_normal[1]
        machine[2] = miserver_normal[1]
    elif CPU <= 4:
        machine[0] = amazon_normal[2]
        machine[1] = google_normal[2]
        machine[2] = miserver_normal[2]
    else:
        machine[0] = amazon_normal[3]
        machine[1] = google_normal[3]
        machine[2] = miserver_normal[3]

    #amazon pricing is in the first slot of output
    tmp = machine[0][1] + 0.1 * storage
    output[0] = machine[0][0] + str(storage) + "(GB), $" + str(tmp)

    #Google Pricing
    tmp = machine[1][1] + 0.17 * storage
    output[1] = machine[1][0] + str(storage) + "(GB), $" + str(tmp)

    #miserver Pricing
    tmp = machine[2][1] + 0.0735 * storage
    output[2] = machine[2][0] + str(storage) + "(GB), $" + str(tmp)

    return output

def get_ram_machine(RAM, storage):
    #default value
    machine = [amazon_normal[0], google_normal[0], miserver_normal[0]]
    output = ["", "", ""]

    if RAM <= 2:
        machine[0] = amazon_normal[0]
        machine[1] = google_normal[0]
        machine[2] = miserver_normal[0]
    elif RAM <= 4:
        machine[0] = amazon_normal[1]
        machine[1] = google_normal[1]
        machine[2] = miserver_normal[1]
    elif RAM <= 16:
        machine[0] = amazon_normal[2]
        machine[1] = google_normal[2]
        machine[2] = miserver_normal[2]
    elif RAM <= 32:
        machine[0] = amazon_normal[3]
        machine[1] = google_normal[3]
        machine[2] = miserver_normal[3]
    else:
        machine[0] = amazon_normal[4]
        machine[1] = google_normal[4]
        machine[2] = miserver_normal[4]

    #amazon pricing is in the first slot of output
    tmp = machine[0][1] + 0.1 * storage
    output[0] = machine[0][0] + str(storage) + "(GB), $" + str(tmp)

    #Google Pricing
    tmp = machine[1][1] + 0.17 * storage
    output[1] = machine[1][0] + str(storage) + "(GB), $" + str(tmp)

    #miserver Pricing
    tmp = machine[2][1] + 0.0735 * storage
    output[2] = machine[2][0] + str(storage) + "(GB), $" + str(tmp)

    return output

def get_cpu_optimized(CPU, storage):
    #List is ordered [Title, EC2, Amazon machine, compute engine, google machine]
    machine = [amazon_optimized[0], google_optimized[0]]
    output = ["", "", "", "", ""]
    tmp = 0
    output[0] = "Optimized CPU Options"
    output[1] = "Amazon EC2: "
    output[3] = "Google Compute Engine: "

    if CPU <=2:
        output[0] = ""
        output[1] = ""
        output[3] = ""

        #returns right away to avoid the calculation step.
        return output
    elif CPU <=4:
        machine[0] = amazon_optimized[0]
        machine[1] = google_optimized[0]
    else:
        machine[0] = amazon_optimized[1]
        machine[1] = google_optimized[1]

    tmp = machine[0][1] + 0.1 * storage
    output[2] = machine[0][0] + str(storage) + "(GB), $" + str(tmp)

    tmp = machine[1][1] + 0.17 * storage
    output[4] = machine[1][0] + str(storage) + "(GB), $" + str(tmp)

    return output

def get_ram_optimized(RAM, storage):
    #List is ordered [Title, EC2, Amazon machine, compute engine, google machine]
    machine = [amazon_optimized[2], google_optimized[2]]
    output = ["", "", "", "", ""]
    tmp = 0
    output[0] = "Memory Optimized Options"
    output[1] = "Amazon EC2: "
    output[3] = "Google Compute Engine: "

    if RAM <=4:
        output[0] = ""
        output[1] = ""
        output[3] = ""

        #returns right away to avoid the calculation step.
        return output
    elif RAM <=16:
        machine[0] = amazon_optimized[2]
        machine[1] = google_optimized[2]
    elif RAM <=32:
        machine[0] = amazon_optimized[2]
        machine[1] = google_optimized[2]
    else:
        machine[0] = amazon_optimized[3]
        machine[1] = google_optimized[3]

    tmp = machine[0][1] + 0.1 * storage
    output[2] = machine[0][0] + str(storage) + "(GB), $" + str(tmp)

    tmp = machine[1][1] + 0.17 * storage
    output[4] = machine[1][0] + str(storage) + "(GB), $" + str(tmp)

    return output

#This function is specifically for amazon during the build your own section
def find_comparable(RAM, CPU, storage):
    output = ""

    #Protects div by 0 error
    if CPU == 0:
        answers = get_ram_machine(RAM, storage)
        output = answers[0]
    elif (RAM / CPU) >= 6:
        #Probably want a RAM optimized machine
        all_answers = get_ram_optimized(RAM, storage)
        output = all_answers[2]
    elif (RAM / CPU) <= 2:
        #probably want a cpu optimized machine
        all_answers = get_cpu_optimized(CPU, storage)
        output = all_answers[2]
    else:
        #Take a normal machine based on RAM.
        all_answers = get_ram_machine(RAM, storage)
        output = all_answers[0]

    return output

def get_all_amazon():
    #Output will be in the form [normal, cpu optimized, RAM optimized]
    output = ["", "", ""]
    normal = ""
    cpu = ""
    ram = ""

    for i in amazon_normal:
        normal += i[0] + " $" + str(i[1]) + "\n"

    for x in range(0, 2):
        cpu += amazon_optimized[x][0] + " $" + str(amazon_optimized[x][1]) + "\n"

    for y in range(2, 4):
        ram += amazon_optimized[y][0] + " $" + str(amazon_optimized[y][1]) + "\n"

    output[0] = normal
    output[1] = cpu
    output[2] = ram
    return output

def get_all_google():
    #Output will be in the form [normal, cpu optimized, RAM optimized]
    output = ["", "", ""]
    normal = ""
    cpu = ""
    ram = ""

    for i in google_normal:
        normal += i[0] + " $" + str(i[1]) + "\n"

    for x in range(0, 2):
        cpu += google_optimized[x][0] + " $" + str(google_optimized[x][1]) + "\n"

    for y in range(2, 4):
        ram += google_optimized[y][0] + " $" + str(google_optimized[y][1]) + "\n"

    output[0] = normal
    output[1] = cpu
    output[2] = ram
    return output

def get_all_miserver():
    #miserver does not have special servers so we can just return a string instead. 
    output = ""

    for i in miserver_normal:
        output += i[0] + " $" + str(i[1]) + "\n"

    return output
