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


#STILL need to do the optimized cases
