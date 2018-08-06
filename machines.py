#Returns the correct machines for cloud computing app

#Lists keep the machine together with the base price

#Amazon has (machine, reserved price, on-demand price/hour, spot price/hour )
#Google & miserver are (machine, reserved price / month)
amazon_normal = [("t2.small, 2(GB), 1, ", 10.51, 0.023, 0.0069),
                ("t2.large, 4(GB), 2, ", 41.98, 0.0928, 0.0278),
                ("t2.xlarge, 16(GB), 4, ", 97.09, 0.1856, 0.0557),
                ("t2.2xlarge, 32(GB), 8, ", 167.90, 0.3712, 0.1114),
                ("m5.4xlarge, 64(GB), 16, ", 358.43, 0.768, 0.2527),
                ("m5.12xlarge, 192(GB), 48, ", 1074.56, 2.304, 2.304),
                ]

amazon_optimized = [("c5.xlarge, 8(GB), 4, ", 78.84, 0.17, 0.0638),
                    ("c5.4xlarge, 32(GB), 16, ", 315.36, 0.68, 0.2469),
                    ("c5.9xlarge, 72(GB), 36, ", 708.83, 1.53, 0.3197),
                    ("r4.xlarge, 30.5(GB), 4, ", 122.64, 0.266, 0.063),
                    ("r4.2xlarge, 61(GB), 8, ", 245.28, 0.532, 0.1268),
                    ("r4.4xlarge, 122(GB), 16, ", 490.56, 1.064, 0.1489),
                    ]

google_normal = [("n1-standard-1, 3.75(GB), 1, ", 24.27),
                ("n1-standard-2, 7.5(GB), 2, ", 48.55),
                ("n1-standard-4, 15(GB), 4, ", 97.09),
                ("n1-standard-8, 30(GB), 8, ", 194.18),
                ("n1-standard-16, 60(GB), 16, ", 388.36),
                ("n1-standard-32, 120(GB), 32", 776.72),
                ]

google_optimized = [("n1-highcpu-4, 3.6(GB), 4, ", 72.46),
                    ("n1-highcpu-16, 14.4(GB), 16, ", 289.84),
                    ("n1-highcpu-32, 28.8(GB), 32, ", 579.68),
                    ("n1-highmem-4, 26(GB), 4, ", 121.0),
                    ("n1-highmem-8, 52(GB), 8, ", 242.0),
                    ("n1-highmem-16, 104(GB), 16, ", 484.0),
                    ]

miserver_normal = [("server1, 2(GB), 1, ", 16.795),
                    ("server2, 4(GB), 2, ", 31.295),
                    ("server3, 16(GB), 4, ", 118.295),
                    ("server4, 32(GB), 8, ", 234.295),
                    ("server5, 64(GB), 8, ", 466.295),
                    ("server6, 128(GB), 32, ", 932.295),
                    ]

# =================== Hard-Coded Additional Storage Pricing ====================
#Amazon General Purpose SSD. cost/GB/month
am_add_s = 0.1

#Google SSD Provisioned Space
g_add_s = 0.17

#MiServer. General Replicated
mi_add_s = 0.0735

#User wants to sort by # of CPUs
def get_cpu_machine(CPU, storage, hours):
    #default value
    machine = [amazon_normal[0], google_normal[0], miserver_normal[0]]
    output = ["", "", ""]

    correct_index = find_near_cpu(CPU)
    machine[0] = amazon_normal[correct_index]
    machine[1] = google_normal[correct_index]
    machine[2] = miserver_normal[correct_index]

    #amazon pricing is in the first slot of output
    tmp = machine[0][1] + am_add_s * storage
    output[0] = "Reserved: " + machine[0][0] + str(storage) + "(GB), $" + str(tmp) + "\n"

    tmp = machine[0][2] * hours + am_add_s * storage
    output[0] += "On-Demand: " + machine[0][0] + str(storage) + "(GB), $" + str(tmp)

    #Google Pricing
    tmp = machine[1][1] + g_add_s * storage
    output[1] = machine[1][0] + str(storage) + "(GB), $" + str(tmp)

    #miserver Pricing
    tmp = machine[2][1] + mi_add_s * storage
    output[2] = machine[2][0] + str(storage) + "(GB), $" + str(tmp)

    #Output is a list containing 3 strings [amazon, google, miserver]
    return output

#This function returns the correct index for how many CPU's were requested.
def find_near_cpu(CPU):
    return_value = 0

    if CPU <= 1:
        return_value = 0
    elif CPU <=2:
        return_value = 1
    elif CPU<= 4:
        return_value = 2
    elif CPU <= 8:
        return_value = 3
    elif CPU <= 16:
        return_value = 4
    else:
        return_value = 5

    #The value returned is the correct index.
    return return_value

#Used if the user wants to sort by RAM
def get_ram_machine(RAM, storage, hours):
    #default value
    machine = [amazon_normal[0], google_normal[0], miserver_normal[0]]
    output = ["", "", ""]

    correct_index = find_near_ram(RAM)
    machine[0] = amazon_normal[correct_index]
    machine[1] = google_normal[correct_index]
    machine[2] = miserver_normal[correct_index]

    #amazon pricing is in the first slot of output
    tmp = machine[0][1] + am_add_s * storage
    output[0] = "Reserved: " + machine[0][0] + str(storage) + "(GB), $" + str(tmp) + "\n"

    tmp = machine[0][2] * hours + am_add_s * storage
    output[0] += "On-Demand: " + machine[0][0] + str(storage) + "(GB), $" + str(tmp)

    #Google Pricing
    tmp = machine[1][1] + g_add_s * storage
    output[1] = machine[1][0] + str(storage) + "(GB), $" + str(tmp)

    #miserver Pricing
    tmp = machine[2][1] + mi_add_s * storage
    output[2] = machine[2][0] + str(storage) + "(GB), $" + str(tmp)

    #Output is a list containing 3 strings [amazon, google, miserver]
    return output

#Finds the correct index to return based on RAM requirement
def find_near_ram(RAM):
    ind = 0

    if RAM <= 2:
        ind = 0
    elif RAM <= 4:
        ind = 1
    elif RAM <= 16:
        ind = 2
    elif RAM <= 32:
        ind = 3
    elif RAM <= 64:
        ind = 4
    else:
        ind = 5

    return ind

def get_cpu_optimized(CPU, storage, hours):
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
        #Too small of CPUs to have any optimization options
        return output
    else:
        ind = find_near_cpu_opt(CPU)
        machine[0] = amazon_optimized[ind]
        machine[1] = google_optimized[ind]

    #Amazon
    tmp = machine[0][1] + am_add_s * storage
    output[2] = "Reserved: " + machine[0][0] + str(storage) + "(GB), $" + str(tmp) + "\n"

    tmp = machine[0][2] * hours + am_add_s * storage
    output[2] += "On-Demand: " + machine[0][0] + str(storage) + "(GB), $" + str(tmp)

    #Google
    tmp = machine[1][1] + g_add_s * storage
    output[4] = machine[1][0] + str(storage) + "(GB), $" + str(tmp)

    return output

#Finds the correct CPU optimized index based on CPU requirement
def find_near_cpu_opt(CPU):
    index = 0

    if CPU <= 2:
        print "This is an error: CPU Optimized"
    elif CPU <=4:
        index = 0
    elif CPU <= 16:
        index = 1
    else:
        index = 2

    return index

def get_ram_optimized(RAM, storage, hours):
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
        #RAM is too small to have optimized options
        return output
    else:
        ind = find_near_ram_opt(RAM)
        machine[0] = amazon_optimized[ind]
        machine[1] = google_optimized[ind]

    #Amazon
    tmp = machine[0][1] + am_add_s * storage
    output[2] = "Reserved: " + machine[0][0] + str(storage) + "(GB), $" + str(tmp) + "\n"

    tmp = machine[0][2] * hours + am_add_s * storage
    output[2] += "On-Demand: " + machine[0][0] + str(storage) + "(GB), $" + str(tmp)

    #Google
    tmp = machine[1][1] + g_add_s * storage
    output[4] = machine[1][0] + str(storage) + "(GB), $" + str(tmp)

    return output

#Finds the correct index for RAM optimized machines based on RAM requirement.
def find_near_ram_opt(RAM):
    ind = 0

    if RAM <=4:
        print "This is an error message: RAM Optimized"
    elif RAM <= 32:
        ind = 3
    elif RAM <= 60:
        ind = 4
    else:
        ind = 5

    return ind

#This function is specifically for amazon during the build your own section
def find_comparable(RAM, CPU, storage, hours):
    output = ""

    #Protects div by 0 error
    #If statements decide if RAM / CPU ratio is skewed in one direction enough
    # to warrant getting an optimized machine or a regular one
    if CPU == 0:
        answers = get_ram_machine(RAM, storage, hours)
        output = answers[0]
    elif (RAM / CPU) >= 6:
        #Probably want a RAM optimized machine
        all_answers = get_ram_optimized(RAM, storage, hours)
        output = all_answers[2]
    elif (RAM / CPU) <= 2:
        #probably want a cpu optimized machine
        all_answers = get_cpu_optimized(CPU, storage, hours)
        output = all_answers[2]
    else:
        #Take a normal machine based on RAM.
        all_answers = get_ram_machine(RAM, storage, hours)
        output = all_answers[0]

    return output

def aws_compare_prices(RAM, CPU, storage, hours):
    output = ""
    index = 0
    am_machine = amazon_normal[0]

    #Prevents divide by zero
    if CPU == 0:
        index = find_near_ram(RAM)
        am_machine = amazon_normal[index]
    #Lots of RAM. Need RAM optimized
    elif (RAM / CPU) >= 6:
        index = find_near_ram_opt(RAM)
        am_machine = amazon_optimized[index]
    #Lots of CPU. Need CPU optimized
    elif (RAM / CPU) <= 2:
        index = find_near_cpu_opt(CPU)
        am_machine = amazon_optimized[index]
    #Fairly normal ratio. Just base off of normal ram.
    else:
        index = find_near_ram(RAM)
        am_machine = amazon_normal[index]

    tmp = am_machine[1] + am_add_s * storage
    output = "Reserved: " + am_machine[0] + str(storage) + "(GB), $" + str(tmp) + "\n"

    tmp = am_machine[2] * hours + am_add_s * storage
    output += "On-Demand: " + am_machine[0] + str(storage) + "(GB), $" + str(tmp) + "\n"

    tmp = am_machine[3] * hours + am_add_s * storage
    output += "Spot: " + am_machine[0] + str(storage) + "(GB), $" + str(tmp)

    return output

def get_all_amazon():
    #Output will be in the form [normal, cpu optimized, RAM optimized], all strings
    output = ["", "", ""]
    normal = ""
    cpu = ""
    ram = ""

    #Adds all normal amazon machines
    for i in amazon_normal:
        normal += i[0] + " $" + str(i[1]) + "\n"

    #adds all cpu optimized machines
    for x in range(0, 3):
        cpu += amazon_optimized[x][0] + " $" + str(amazon_optimized[x][1]) + "\n"

    #adds all RAM optimized machines
    for y in range(3, 6):
        ram += amazon_optimized[y][0] + " $" + str(amazon_optimized[y][1]) + "\n"

    output[0] = normal
    output[1] = cpu
    output[2] = ram
    return output

def get_all_google():
    #Output will be in the form [normal, cpu optimized, RAM optimized], all strings
    output = ["", "", ""]
    normal = ""
    cpu = ""
    ram = ""

    #adds all normal machines
    for i in google_normal:
        normal += i[0] + " $" + str(i[1]) + "\n"

    #adds all cpu optimized machines
    for x in range(0, 3):
        cpu += google_optimized[x][0] + " $" + str(google_optimized[x][1]) + "\n"

    #adds all RAM optimized machines
    for y in range(3, 6):
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
