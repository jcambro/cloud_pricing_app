#Returns the correct machines for cloud computing app

amazon_normal = [("t2.small, 2(GB), 1, ", 10.51),
                ("t2.large, 4(GB), 2, ", 41.98),
                ("t2.xlarge, 16(GB), 4, ", 97.09),
                ("t2.2xlarge, 32(GB), 8, " 167.90),
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
                    ("n1-highmem-8, 52(GB), 8, " 242.0),
                    ]

miserver_normal = [("server1, 2(GB), 1, ", 16.795),
                    ("server2, 4(GB), 2, ", 31.295),
                    ("server3, 16(GB), 4, ", 118.295),
                    ("server4, 32(GB), 8, ", 234.295),
                    ("server5, 64(GB), 8, ", 466.295),
                    ]
