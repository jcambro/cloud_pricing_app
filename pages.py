from Tkinter import *
import calculation
import machines

my_font = ("Helvetica", 20)
major_font = ("Helvetica", 30, "bold")
minor_font = ("Helvetica", 26, "bold")
small_font = ("Helvetica", 16)

foreg = "white"
backg = "gray40"
button_backg = "blue4"
active_bg = "blue3"
active_fg = "white"

#helper function that completely empties all the widgets on a page
def clear_grid(the_page):
	for widge in the_page.grid_slaves():
		widge.grid_remove()

#====================== Intro Page ============================================
class StartPage(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.config(bg="gray40")

		self.label = Label(self, text="Welcome to Cloud Cost Comparison", bg=backg, fg=foreg, font=major_font).grid(row=0, column=1, padx=10, pady=15)
		self.label2 = Label(self, text="Compare Between Amazon, Google, and the University of Michigan\nPlease Make A Selection Below", bg=backg, fg=foreg, font=minor_font).grid(row=1, column=1, padx=10, pady=15)
		self.storage_page = Button(self, text="Explore Storage Pricing", font=my_font, height=2, width=25, bg=button_backg, fg=foreg, activebackground=active_bg, activeforeground=active_fg, command= lambda: controller.show_frame(StoragePage) ).grid(row=2, column=1, padx=10, pady=5)
		self.compute_page = Button(self, text="Explore Computing Pricing",font=my_font, height=2, width=25, bg=button_backg, fg=foreg, activebackground=active_bg, activeforeground=active_fg, command= lambda: controller.show_frame(ComputingIntro) ).grid(row=3, column=1, padx=10, pady=5)
		self.width_spacer = Label(self, width=14, bg=backg, fg=foreg ).grid(row=0, column=0)

#====================== Storage Varibale Input ================================
class StoragePage(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.config(bg=backg)
		self.par_controller = controller

		self.width_spacer = Label(self, width=37, bg=backg, fg=foreg)
		self.width_spacer.grid(row=1, column=0)

		self.label1 = Label(self, text="Storage Needed (GB)", bg=backg, fg=foreg, font=my_font)
		self.label1.grid(row=1, column=1)
		self.entry1 = Entry(self, font=my_font)
		self.entry1.insert(10, "0")
		self.entry1.grid(row=1, column=2, padx=10, pady=10)

		self.label2 = Label(self, text="Read Operations (in thousands)", bg=backg, fg=foreg, font=my_font)
		self.label2.grid(row=2, column=1)
		self.entry2 = Entry(self, font=my_font)
		self.entry2.insert(10,"0")
		self.entry2.grid(row=2, column=2, padx=10, pady=10)

		self.label3 = Label(self, text="Write Operations (in thousands)", bg=backg, fg=foreg, font=my_font)
		self.label3.grid(row=3, column=1)
		self.entry3 = Entry(self, font=my_font)
		self.entry3.insert(10, "0")
		self.entry3.grid(row=3, column=2, padx=10, pady=10)

		self.label4 = Label(self, text="Data Scanned (GB)", bg=backg, fg=foreg, font=my_font)
		self.label4.grid(row=4, column=1)
		self.entry4 = Entry(self, font=my_font)
		self.entry4.insert(10, "0")
		self.entry4.grid(row=4, column=2, padx=10, pady=10)

		self.label5 = Label(self, text="Data Returned (GB)", bg=backg, fg=foreg, font=my_font)
		self.label5.grid(row=5, column=1)
		self.entry5 = Entry(self, font=my_font)
		self.entry5.insert(10, "0")
		self.entry5.grid(row=5, column=2, padx=10, pady=10)

		self.calc_button = Button(self, text="Calculate Final Cost",font=my_font, bg=button_backg, fg=foreg, activebackground=active_bg, activeforeground=active_fg, padx=10, pady=10, command=self.get_input )
		self.calc_button.grid(row=6, column=1, columnspan=2, sticky="ew", pady=10)

		self.home_button = Button(self, text="Home", font=my_font, bg=button_backg, fg=foreg, activebackground=active_bg, activeforeground=active_fg, padx=1, pady=1, command=self.go_home)
		self.home_button.grid(row=0, column=0, sticky=N+W)

	def go_home(self):
		self.par_controller.reset_frame(StoragePage)

	#Takes all the text entry input and puts them into variables
	def get_input(self):
		self.storage_needed = float(self.entry1.get() )
		self.read_ops = float(self.entry2.get() )
		self.write_ops = float(self.entry3.get() )
		self.data_scan = float(self.entry4.get() )
		self.data_return = float(self.entry5.get() )

		#Delete entries to make room for the final result
		#I cannot make a new page without the variables updating correctly
		clear_grid(self)

		self.home_button.grid(row=0, column=0, sticky=N+W)
		self.label6 = Label(self, text="Final Price Calculations", bg=backg, fg=foreg, font=major_font).grid(row=0, column=1, sticky=W)

		#Calculate all of the pricing options
		#AMAZON
		self.am_s3 = calculation.aws_s3_price(self.storage_needed, self.data_return, self.data_scan, self.write_ops, self.read_ops)
		self.am_s3ia = calculation.aws_s3ia_price(self.storage_needed, self.data_return, self.data_scan, self.write_ops, self.read_ops)
		self.am_glac = calculation.aws_glacier_price(self.storage_needed, self.data_return, self.data_scan, self.write_ops, self.read_ops)

		#GOOGLE
		self.g_mr = calculation.google_mr_price(self.storage_needed, self.data_return, self.data_scan, self.write_ops, self.read_ops)
		self.g_near = calculation.google_near_price(self.storage_needed, self.data_return, self.data_scan, self.write_ops, self.read_ops)
		self.g_cold = calculation.google_cold_price(self.storage_needed, self.data_return, self.data_scan, self.write_ops, self.read_ops)
		#MICHIGAN
		self.m_base = calculation.mi_base_price(self.storage_needed, self.data_return, self.data_scan, self.write_ops, self.read_ops)
		self.m_bs = calculation.mi_bs_price(self.storage_needed, self.data_return, self.data_scan, self.write_ops, self.read_ops)
		self.m_br = calculation.mi_br_price(self.storage_needed, self.data_return, self.data_scan, self.write_ops, self.read_ops)
		self.m_sr = calculation.mi_sr_price(self.storage_needed, self.data_return, self.data_scan, self.write_ops, self.read_ops)

		#All the Amazon labels and packing
		self.label7 = Label(self, text="Amazon Pricing (per month)", bg=backg, fg=foreg, font=minor_font).grid(row=1, column=0)
		self.label8 = Label(self, text="S3 = $" + str(self.am_s3), bg=backg, fg=foreg, font=my_font ).grid(row=2, column=1)
		self.label9 = Label(self, text="S3 Infrequent Access = $" + str(self.am_s3ia), bg=backg, fg=foreg, font=my_font).grid(row=3, column=1)
		self.label10 = Label(self, text="Glacier = $" + str(self.am_glac), bg=backg, fg=foreg, font=my_font).grid(row=4, column=1)

		#All of the Google labels and packing
		self.label11 = Label(self, text="Google Pricing (per month)", bg=backg, fg=foreg, font=minor_font).grid(row=5, column=0)
		self.label12 = Label(self, text="Multi-Regional & Regional = $" + str(self.g_mr), bg=backg, fg=foreg, font=my_font).grid(row=6, column=1)
		self.label13 = Label(self, text="Nearline = $" + str(self.g_near), bg=backg, fg=foreg, font=my_font).grid(row=7, column=1)
		self.label14 = Label(self, text="Coldline = $" + str(self.g_cold), bg=backg, fg=foreg, font=my_font).grid(row=8, column=1)

		#All of the Miserver labels and packing
		self.label15 = Label(self, text="MiStorage Pricing (per month)",bg=backg, fg=foreg, font=minor_font).grid(row=9, column=0)
		self.label16 = Label(self, text="Base = $" + str(self.m_base), bg=backg, fg=foreg, font=my_font).grid(row=10, column=1)
		self.label17 = Label(self, text="Base & Snapshots = $" + str(self.m_bs), bg=backg, fg=foreg, font=my_font).grid(row=11, column=1)
		self.label18 = Label(self, text="Base & Replication = $" + str(self.m_br), bg=backg, fg=foreg, font=my_font).grid(row=12, column=1)
		self.label19 = Label(self, text="Snapshots & Replication = $" + str(self.m_sr), bg=backg, fg=foreg, font=my_font).grid(row=13, column=1)

#====================== Computing first selection ==============================
class ComputingIntro(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.config(bg=backg)
		self.par_controller = controller

		self.width_spacer = Label(self, width=47, bg=backg, fg=foreg)
		self.width_spacer.grid(row=0, column=1)
		self.height_spacer = Label(self, height=17, bg=backg, fg=foreg)
		self.height_spacer.grid(row=7, column=1)

		self.label1 = Label(self, text="Please Pick An Option", bg=backg, fg=foreg, font=major_font)
		self.label1.grid(column=10, row=0, pady=10, padx=5, columnspan=2)

		self.button1 = Button(self, text="Pre-Built Computing", height=2, width=17, font=my_font, bg=button_backg, fg=foreg, activebackground=active_bg, activeforeground=active_fg, command= lambda: self.par_controller.show_frame(ComputingPreBuilt) )
		self.button1.grid(row=3, column=10 ,padx=10, pady=5, columnspan=2)

		self.button2 = Button(self, text="Build Your Own", font=my_font, height=2, width=17, bg=button_backg, fg=foreg, activebackground=active_bg, activeforeground=active_fg, command= lambda: self.par_controller.show_frame(ComputingOwnBuild) )
		self.button2.grid(row=4, column=10, padx=10, pady=5, columnspan=2)

		self.button3 = Button(self, text="View AWS Options", font=my_font, height=2, width=17, bg=button_backg, fg=foreg, activebackground=active_bg, activeforeground=active_fg, command= lambda: self.par_controller.show_frame(AWS_Info) )
		self.button3.grid(row=5, column=10, padx=10, pady=5, columnspan=2)

		self.home_button = Button(self, text="Home", font=my_font, bg=button_backg, fg=foreg, activebackground=active_bg, activeforeground=active_fg, padx=1, pady=1, command=self.go_home)
		self.home_button.grid(row=0, column=0, sticky=W)

	def go_home(self):
		self.par_controller.reset_frame(ComputingIntro)

#====================== AWS Info ==============================================
class AWS_Info(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.config(bg=backg)
		self.par_controller = controller

		self.width_spacer = Label(self, width=29, bg=backg, fg=foreg)
		self.width_spacer.grid(row=0, column=1)

		self.home_button = Button(self, text="Home", font=my_font, bg=button_backg, fg=foreg, activebackground=active_bg, activeforeground=active_fg, padx=1, pady=1, command=self.go_home)
		self.home_button.grid(row=0, column=0, sticky=W)

		self.label1 = Label(self, text="AWS Types and Information", font=major_font, bg=backg, fg=foreg)
		self.label1.grid(column=2, row=0, pady=5, padx=5, columnspan=2)

		self.label2 = Label(self, text="Spot", font=minor_font, bg=backg, fg=foreg)
		self.label2.grid(row=1, column=2)

		self.label3 = Label(self, text="Reserved", font=minor_font, bg=backg, fg=foreg)
		self.label3.grid(row=3, column=2)

		self.label4 = Label(self, text="On-Demand", font=minor_font, bg=backg, fg=foreg)
		self.label4.grid(row=5, column=2)

		self.spot_info = "Spot Instances utilize spare AWS compute capacity. Amazon \nreserves the right to interupt computation with a two minute warning. \nSpot instances are meant for flexible applications that can easily \nbe paused and resumed."
		self.label5 = Label(self, text=self.spot_info, font=small_font, bg=backg, fg=foreg)
		self.label5.grid(row=2, column=2)

		self.reserved_info = "Reserved instances provide users with steady EC2 availability. \nUsers are given capacity reservation to use \nimmediately when needed. Reserved instances are meant for\n steady state usage and can be purchased with a 1 or 2\n year commitment."
		self.label6 = Label(self, text=self.reserved_info, font=small_font, bg=backg, fg=foreg)
		self.label6.grid(row=4, column=2)

		self.od_info = "On-Demand instances provide compute capacity per hour or per second. \nNo long term commitments are needed and users can \neasily increase or decrease compute capacity. On-Demand is meant \nfor short term and unpredictable loads."
		self.label7 = Label(self, text=self.od_info, font=small_font, bg=backg, fg=foreg)
		self.label7.grid(row=6, column=2)

		self.button1 = Button(self, text="Compare Prices", font=my_font, bg=button_backg, fg=foreg, activebackground=active_bg, activeforeground=active_fg, padx=5, pady=5, command= lambda: self.par_controller.show_frame(AWS_compare) )
		self.button1.grid(row=7, column=2, padx=10, pady=5)

	def go_home(self):
		self.par_controller.reset_frame(AWS_Info)

#====================== AWS cost compare ====================================
class AWS_compare(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.config(bg=backg)
		self.par_controller = controller

		self.home_button = Button(self, text="Home", font=my_font, bg=button_backg, fg=foreg, activebackground=active_bg, activeforeground=active_fg, padx=1, pady=1, command=self.go_home)
		self.home_button.grid(row=0, column=0, sticky=W)

		self.height_spacer = Label(self, height=15, bg=backg, fg=foreg)
		self.height_spacer.grid(row=8, column=0)

		self.width_spacer = Label(self, width=40, bg=backg, fg=foreg)
		self.width_spacer.grid(row=1, column=0)

		self.label1 = Label(self, text="Compare AWS Prices", bg=backg, fg=foreg, font=minor_font)
		self.label1.grid(row=0, column=1, padx=5, pady=5, columnspan=2)

		self.label2 = Label(self, text="RAM required (GB)", bg=backg, fg=foreg, font=my_font)
		self.label2.grid(row=3, column=1, padx=5, pady=5)

		self.entry1 = Entry(self, font=my_font)
		self.entry1.insert(10, "0")
		self.entry1.grid(row=3, column=2)

		self.label3 = Label(self, text="CPUs Needed", bg=backg, fg=foreg, font=my_font)
		self.label3.grid(row=4, column=1, padx=5, pady=5)

		self.entry2 = Entry(self, font=my_font)
		self.entry2.insert(10, "0")
		self.entry2.grid(row=4, column=2)

		self.label5 = Label(self, text="Disk Space (GB)", bg=backg, fg=foreg, font=my_font)
		self.label5.grid(row=5, column=1, padx=5, pady=5)

		self.entry4 = Entry(self, font=my_font)
		self.entry4.insert(10, "0")
		self.entry4.grid(row=5, column=2)

		self.label4 = Label(self, text="Estimate of Hours per Month", bg=backg, fg=foreg, font=my_font)
		self.label4.grid(row=6, column=1, padx=5, pady=5)

		self.entry3 = Entry(self, font=my_font)
		self.entry3.insert(10, "0")
		self.entry3.grid(row=6, column=2)

		self.button1 = Button(self, text="Display Options", font=my_font, bg=button_backg, fg=foreg, activebackground=active_bg, activeforeground=active_fg, padx=5, pady=5, command=self.display_compare)
		self.button1.grid(row=7, column=2, padx=10, pady=5)

	def go_home(self):
		self.par_controller.reset_frame(AWS_compare)

	def display_compare(self):
		self.ram_wanted = float(self.entry1.get() )
		self.cpu_wanted = float(self.entry2.get() )
		self.hours = float(self.entry3.get() )
		self.storage_wanted = float(self.entry4.get() )

		clear_grid(self)

		self.home_button.grid(row=0, column=0, sticky=W)

		self.width_spacer2 = Label(self, width=45, bg=backg, fg=foreg)
		self.width_spacer2.grid(row=1, column=0)

		self.height_spacer2 = Label(self, height=5, bg=backg, fg=foreg)
		self.height_spacer2.grid(row=2, column=1)

		self.label5 = Label(self, text="Final Price Calculations", bg=backg, fg=foreg, font=major_font).grid(row=0, column=2, pady=5)

		self.intro = "Prices are based on a machine with: \n" + str(self.ram_wanted) + "(GB) of RAM \n" + str(self.cpu_wanted) + " CPU(s)\n " + str(self.storage_wanted) + "(GB) of Disk Space\n" + str(self.hours)  + " hours in use / month"
		self.label6 = Label(self, text=self.intro, bg=backg, fg=foreg, font=my_font).grid(row=1, column=2, pady=5)

		self.amazon_custom = machines.aws_compare_prices(self.ram_wanted, self.cpu_wanted, self.storage_wanted, self.hours)
		self.amazon_title = Label(self, text="Amazon EC2", bg=backg, fg=foreg, pady=5, font=major_font).grid(row=2, column=2)
		self.amazon_p = Label(self, text=self.amazon_custom, bg=backg, fg=foreg, pady=5, font=my_font).grid(row=3, column=2)

#====================== Own Build Variables ====================================
class ComputingOwnBuild(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.config(bg=backg)
		self.par_controller = controller

		self.home_button = Button(self, text="Home", font=my_font, bg=button_backg, fg=foreg, activebackground=active_bg, activeforeground=active_fg, padx=1, pady=1, command=self.go_home)
		self.home_button.grid(row=0, column=0, sticky=W)

		self.height_spacer = Label(self, height=18, bg=backg, fg=foreg)
		self.height_spacer.grid(row=6, column=0)

		self.width_spacer = Label(self, width=45, bg=backg, fg=foreg)
		self.width_spacer.grid(row=1, column=0)

		self.build_title = Label(self, text="Enter Your Specifications", bg=backg, fg=foreg, font=major_font)
		self.build_title.grid(row=0, column=1, columnspan=2)

		self.label2 = Label(self, text="RAM (GB)", bg=backg, fg=foreg, font=my_font)
		self.label2.grid(row=1, column=1)
		self.entry2 = Entry(self, font=my_font)
		self.entry2.insert(10, "0")
		self.entry2.grid(row=1, column=2, padx=10, pady=10)

		self.label3 = Label(self, text="Number of CPUs", bg=backg, fg=foreg, font=my_font)
		self.label3.grid(row=2, column=1)
		self.entry3 = Entry(self, font=my_font)
		self.entry3.insert(10,"0")
		self.entry3.grid(row=2, column=2, padx=10, pady=10)

		self.label4 = Label(self, text="Disk Space (GB)", bg=backg, fg=foreg, font=my_font)
		self.label4.grid(row=3, column=1)
		self.entry4 = Entry(self, font=my_font)
		self.entry4.insert(10, "0")
		self.entry4.grid(row=3, column=2, padx=10, pady=10)

		self.label5 = Label(self, text="Hours In Use per Month", bg=backg, fg=foreg, font=my_font)
		self.label5.grid(row=4, column=1)
		self.entry5 = Entry(self, font=my_font)
		self.entry5.insert(10, "0")
		self.entry5.grid(row=4, column=2, padx=10, pady=10)

		self.button4 = Button(self, text="Calculate Price", font=my_font, bg=button_backg, fg=foreg, activebackground=active_bg, activeforeground=active_fg, padx=10, pady=10, command=self.calc_build )
		self.button4.grid(column=1, row=5, columnspan=2, sticky="ew", pady=10)

	def go_home(self):
		self.par_controller.reset_frame(ComputingOwnBuild)

	def calc_build(self):
		self.ram_wanted = float(self.entry2.get())
		self.cpu_wanted = float(self.entry3.get())
		self.storage_wanted = float(self.entry4.get())
		self.hours = float(self.entry5.get())

		clear_grid(self)
		self.home_button.grid(row=0, column=0, sticky=W)

		self.calc_title = Label(self, text="Final Price Calculation", bg=backg, fg=foreg, font=major_font).grid(row=0, column=1, columnspan=2)
		self.intro = "Prices are based on a machine with: \n" + str(self.ram_wanted) + "(GB) of RAM \n" + str(self.cpu_wanted) + " CPU(s)\n " + str(self.storage_wanted) + "(GB) of Disk Space\n" + str(self.hours) + " hours in use / month"
		self.into_label = Label(self, text=self.intro, padx=5, pady=5, bg=backg, fg=foreg, font=minor_font).grid(row=1, column=1, columnspan=2)

		self.miserver_price = calculation.mi_build_price(self.cpu_wanted, self.ram_wanted, self.storage_wanted)
		self.google_price = calculation.google_build_price(self.cpu_wanted, self.ram_wanted, self.storage_wanted)

		self.google_title = Label(self, text="Google Compute Engine: ", bg=backg, fg=foreg, pady=5, font=my_font).grid(row=2, column=1)
		self.google_p = Label(self, text="$" + str(self.google_price), bg=backg, fg=foreg, pady=5, font=my_font).grid(row=2, column=2)

		#get a custom amazon machine based on RAM for comparrison.
		self.amazon_custom = machines.find_comparable(self.ram_wanted, self.cpu_wanted, self.storage_wanted, self.hours)
		self.amazon_title = Label(self, text="Amazon EC2: ", bg=backg, fg=foreg, pady=5, font=my_font).grid(row=5, column=1)
		self.amazon_p = Label(self, text=self.amazon_custom, bg=backg, fg=foreg, pady=5, font=my_font).grid(row=5, column=2)

		self.close_label = Label(self, text = "A Comparable Amazon Machine", bg=backg, fg=foreg, pady=10, font=minor_font).grid(row=4, column=1, columnspan=2)

		self.mi_title = Label(self, text="MiServer: ", bg=backg, fg=foreg, pady=5, font=my_font).grid(row=3, column=1)
		self.mi_p = Label(self, text="$" + str(self.miserver_price), bg=backg, fg=foreg, pady=5, font=my_font).grid(row=3, column=2)

		self.height_spacer2 = Label(self, height=7, bg=backg, fg=foreg)
		self.height_spacer2.grid(column=0, row=8)

		self.width_spacer2 = Label(self, width=25, bg=backg, fg=foreg)
		self.width_spacer2.grid(column=0, row=1)

#====================== Computing second selection  ============================
class ComputingPreBuilt(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.config(bg=backg)
		self.par_controller = controller

		self.width_spacer = Label(self, width=42, bg=backg, fg=foreg)
		self.width_spacer.grid(row=1, column=0)

		self.height_spacer = Label(self, height=15, bg=backg, fg=foreg)
		self.height_spacer.grid(row=4, column=0)

		self.home_button = Button(self, text="Home", font=my_font, bg=button_backg, fg=foreg, activebackground=active_bg, activeforeground=active_fg, padx=1, pady=1, command=self.go_home)
		self.home_button.grid(row=0, column=0, sticky=W)

		self.label2 = Label(self, text="Select What You Want To Sort By", bg=backg, fg=foreg, font=major_font)
		self.label2.grid(row=0, column=1, padx=10, pady=10)

		self.button1 = Button(self, text="RAM",font=my_font, bg="blue4", fg="white", activebackground="blue3", activeforeground="white", height=2, width=20, command= lambda: self.par_controller.show_frame(ComputingRAM))
		self.button1.grid(row=1, column=1, padx=10, pady=5)

		self.button2 = Button(self, text="Number of CPUs", bg=button_backg, fg=foreg, activebackground=active_bg, activeforeground=active_fg, font=my_font, height=2, width=20, command= lambda: self.par_controller.show_frame(ComputingCPU) )
		self.button2.grid(row=2, column=1, padx=10, pady=5)

		self.button3 = Button(self, text="Display All Options", font=my_font, height=2, width=20, bg=button_backg, fg=foreg, activebackground=active_bg, activeforeground=active_fg, command= lambda: self.par_controller.show_frame(ComputingAll) )
		self.button3.grid(row=3, column=1, padx=10, pady=5)

	def go_home(self):
		self.par_controller.reset_frame(ComputingPreBuilt)

#====================== Sort by RAM ============================================
class ComputingRAM(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.config(bg=backg)
		self.par_controller = controller

		self.home_button = Button(self, text="Home", font=my_font, bg=button_backg, fg=foreg, activebackground=active_bg, activeforeground=active_fg, padx=1, pady=1, command=self.go_home)
		self.home_button.grid(row=0, column=0, sticky=W)

		self.height_spacer = Label(self, height=23, bg=backg, fg=foreg)
		self.height_spacer.grid(row=8, column=0)

		self.width_spacer = Label(self, width=32, bg=backg, fg=foreg)
		self.width_spacer.grid(row=1, column=0)

		self.label0 = Label(self, text="You have selected RAM", bg=backg, fg=foreg, font=minor_font)
		self.label0.grid(row=0, column=1, padx=5, pady=5, columnspan=2)

		self.label1 = Label(self, text="How much is required (GB)?", bg=backg, fg=foreg, font=my_font)
		self.label1.grid(row=3, column=1, padx=5, pady=5)

		self.entry1 = Entry(self, font=my_font)
		self.entry1.insert(10, "0")
		self.entry1.grid(row=3, column=2)

		self.label3 = Label(self, text="Additional Disk Space Needed (GB)", bg=backg, fg=foreg, font=my_font)
		self.label3.grid(row=4, column=1, padx=5, pady=5)

		self.entry3 = Entry(self, font=my_font)
		self.entry3.insert(10, "0")
		self.entry3.grid(row=4, column=2)

		self.label4 = Label(self, text="Hours In Use per Month", bg=backg, fg=foreg, font=my_font)
		self.label4.grid(row=5, column=1, padx=5, pady=5)

		self.entry4 = Entry(self, font=my_font)
		self.entry4.insert(10, "0")
		self.entry4.grid(row=5, column=2)

		self.button1 = Button(self, text="Display Options", font=my_font, bg=button_backg, fg=foreg, activebackground=active_bg, activeforeground=active_fg, padx=5, pady=5, command=self.display_ram)
		self.button1.grid(row=6, column=2, padx=10, pady=5)

	def go_home(self):
		self.par_controller.reset_frame(ComputingRAM)

	def display_ram(self):
		self.ram_wanted = float(self.entry1.get())
		self.storage_wanted = int(self.entry3.get())
		self.hours = float(self.entry4.get())

		clear_grid(self)
		self.home_button.grid(row=0, column=0, sticky=NW)
		self.tmp = 0

		#Comes back as a list [Amazon, Google, Miserver]
		self.matches = machines.get_ram_machine(self.ram_wanted, self.storage_wanted, self.hours)

		self.amazon = self.matches[0]
		self.google = self.matches[1]
		self.miserver = self.matches[2]

		#List is ordered [Title, EC2 title, Amazon machine, compute engine title, google machine]
		#Returns any optimized machines available
		self.optim = machines.get_ram_optimized(self.ram_wanted, self.storage_wanted, self.hours)

		#This only displays if there is enough to have optimized. Otherwise they are empty strings.
		self.extra = self.optim[0]
		self.am_ex1 = self.optim[1]
		self.am_ex2 = self.optim[2]
		self.g_ex1 = self.optim[3]
		self.g_ex2 = self.optim[4]

		self.entered_text = str(int(self.ram_wanted)) + "GB of RAM, " + str(int(self.storage_wanted)) + "GB of Disk Space, and " + str(int(self.hours)) + " hours/month"

		self.label7 = Label(self, text="Selected Machines Based on RAM Requirement\n" + self.entered_text + "\n[Machine, RAM, # of CPUs, Disk, Cost/month]", bg=backg, fg=foreg, font=major_font )
		self.label7.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

		self.label8 = Label(self, text="Google Compute Engine: ", bg=backg, fg=foreg, font=my_font)
		self.label8.grid(row=1, column=1, padx=3, pady=7)

		self.label9 = Label(self, text=self.google, bg=backg, fg=foreg, font=my_font)
		self.label9.grid(row=1, column=2, padx=3, pady=7)

		self.label10 = Label(self, text="Amazon EC2: ", bg=backg, fg=foreg, font=my_font)
		self.label10.grid(row=2, column=1, padx=3, pady=7)

		self.label11 = Label(self, text=self.amazon, bg=backg, fg=foreg, font=my_font)
		self.label11.grid(row=2, column=2, padx=3, pady=7)

		self.label12 = Label(self, text="MiServer: ", bg=backg, fg=foreg, font=my_font)
		self.label12.grid(row=3, column=1, padx=3, pady=7)

		self.label13 = Label(self, text=self.miserver, bg=backg, fg=foreg, font=my_font)
		self.label13.grid(row=3, column=2, padx=3, pady=7)

		self.label14 = Label(self, text=self.extra, bg=backg, fg=foreg, font=minor_font)
		self.label14.grid(row=4, column=1, padx=3, pady=10, columnspan=2)

		self.label15 = Label(self, text=self.g_ex1, bg=backg, fg=foreg, font=my_font)
		self.label15.grid(row=5, column=1, padx=3, pady=7)

		self.label16 = Label(self, text=self.g_ex2, bg=backg, fg=foreg, font=my_font)
		self.label16.grid(row=5, column=2, padx=3, pady=7)

		self.label17 = Label(self, text=self.am_ex1, bg=backg, fg=foreg, font=my_font)
		self.label17.grid(row=6, column=1, padx=3, pady=7)

		self.label18 = Label(self, text=self.am_ex2, bg=backg, fg=foreg, font=my_font)
		self.label18.grid(row=6, column=2, padx=3, pady=7)

#====================== Sort By CPU ============================================
class ComputingCPU(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.config(bg=backg)
		self.par_controller = controller

		self.home_button = Button(self, text="Home", font=my_font, bg=button_backg, fg=foreg, activebackground=active_bg, activeforeground=active_fg, padx=1, pady=1, command=self.go_home)
		self.home_button.grid(row=0, column=0, sticky=W)

		self.height_spacer = Label(self, height=23, bg=backg, fg=foreg)
		self.height_spacer.grid(row=6, column=0)

		self.width_spacer = Label(self, width=32, bg=backg, fg=foreg)
		self.width_spacer.grid(row=1, column=0)

		self.label1 = Label(self, text="You have selected CPUs", bg=backg, fg=foreg, font=minor_font)
		self.label1.grid(row=0, column=1, padx=5, pady=5, columnspan=2)

		self.label2 = Label(self, text="How many are required?", bg=backg, fg=foreg, font=my_font)
		self.label2.grid(row=2, column=1, padx=5, pady=5)

		self.entry2 = Entry(self, font=my_font)
		self.entry2.insert(10, "0")
		self.entry2.grid(row=2, column=2)

		self.label4 = Label(self, text="Additional Disk Space Needed (GB)", bg=backg, fg=foreg, font=my_font)
		self.label4.grid(row=3, column=1, padx=5, pady=5)

		self.entry4 = Entry(self, font=my_font)
		self.entry4.insert(10, "0")
		self.entry4.grid(row=3, column=2)

		self.label5 = Label(self, text="Hours In Use per Month", bg=backg, fg=foreg, font=my_font)
		self.label5.grid(row=4, column=1, padx=5, pady=5)

		self.entry5 = Entry(self, font=my_font)
		self.entry5.insert(10, "0")
		self.entry5.grid(row=4, column=2)

		self.button1 = Button(self, text="Display Options", font=my_font, bg=button_backg, fg=foreg, activebackground=active_bg, activeforeground=active_fg, padx=5, pady=5, command=self.display_cpu)
		self.button1.grid(row=5, column=2, padx=10, pady=5)

	def go_home(self):
		self.par_controller.reset_frame(ComputingCPU)

	def display_cpu(self):
		self.cpu_wanted = float(self.entry2.get())
		self.storage_wanted = float(self.entry4.get())
		self.hours = float(self.entry5.get())

		clear_grid(self)
		self.home_button.grid(row=0, column=0, sticky=NW)

		self.matches = machines.get_cpu_machine(self.cpu_wanted, self.storage_wanted, self.hours)
		self.tmp = 0

		#Comes back as a list [Amazon, Google, Miserver]
		self.amazon = self.matches[0]
		self.google = self.matches[1]
		self.miserver = self.matches[2]

		#List is ordered [Title, EC2 title, Amazon machine, compute engine title, google machine]
		#Returns any optimized machines available
		self.optim = machines.get_cpu_optimized(self.cpu_wanted, self.storage_wanted, self.hours)

		#This only displays if there is enough to have optimized. Otherwise they are empty strings.
		self.extra = self.optim[0]
		self.am_ex1 = self.optim[1]
		self.am_ex2 = self.optim[2]
		self.g_ex1 = self.optim[3]
		self.g_ex2 = self.optim[4]

		self.entered_text = str(int(self.cpu_wanted)) + " CPUs, " + str(int(self.storage_wanted)) + "GB of Disk Space, and " + str(int(self.hours)) + " hours/month"

		self.label19 = Label(self, text="Selected Machines Based on CPU Requirement\n" + self.entered_text + "\n[Machine, RAM, # of CPUs, Disk, Cost/month]", bg=backg, fg=foreg, font=major_font )
		self.label19.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

		self.label20 = Label(self, text="Google Compute Engine: ", bg=backg, fg=foreg, font=my_font)
		self.label20.grid(row=1, column=1, padx=3, pady=7)

		self.label21 = Label(self, text=self.google, bg=backg, fg=foreg, font=my_font)
		self.label21.grid(row=1, column=2, padx=3, pady=7)

		self.label22 = Label(self, text="Amazon EC2: ", bg=backg, fg=foreg, font=my_font)
		self.label22.grid(row=2, column=1, padx=3, pady=7)

		self.label23 = Label(self, text=self.amazon, bg=backg, fg=foreg, font=my_font)
		self.label23.grid(row=2, column=2, padx=3, pady=7)

		self.label24 = Label(self, text="MiServer: ", bg=backg, fg=foreg, font=my_font)
		self.label24.grid(row=3, column=1, padx=3, pady=7)

		self.label25 = Label(self, text=self.miserver, bg=backg, fg=foreg, font=my_font)
		self.label25.grid(row=3, column=2, padx=3, pady=7)

		self.label26 = Label(self, text=self.extra, bg=backg, fg=foreg, font=minor_font)
		self.label26.grid(row=4, column=1, padx=3, pady=10, columnspan=2)

		self.label27 = Label(self, text=self.g_ex1, bg=backg, fg=foreg, font=my_font)
		self.label27.grid(row=5, column=1, padx=3, pady=7)

		self.label28 = Label(self, text=self.g_ex2, bg=backg, fg=foreg, font=my_font)
		self.label28.grid(row=5, column=2, padx=3, pady=7)

		self.label29 = Label(self, text=self.am_ex1, bg=backg, fg=foreg, font=my_font)
		self.label29.grid(row=6, column=1, padx=3, pady=7)

		self.label30 = Label(self, text=self.am_ex2, bg=backg, fg=foreg, font=my_font)
		self.label30.grid(row=6, column=2, padx=3, pady=7)

#====================== Display All Options ====================================
class ComputingAll(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.config(bg=backg)
		self.par_controller = controller

		self.home_button = Button(self, text="Home", font=my_font, bg=button_backg, fg=foreg, activebackground=active_bg, activeforeground=active_fg, padx=1, pady=1, command=self.go_home)
		self.home_button.grid(row=0, column=0, sticky=W)

		self.all_title = Label(self, text="All Machines Recorded [Machine, RAM, CPU, Price/Month]", bg=backg, fg=foreg, font=minor_font)
		self.all_title.grid(row=1, column=0, columnspan=3)

		self.label31 = Label(self, text="Google Compute Engine", bg=backg, fg=foreg, font=minor_font)
		self.label31.grid(row=2, column=0)

		self.google_out = machines.get_all_google()
		self.label32 = Label(self, text=self.google_out[0], bg=backg, fg=foreg, font=my_font)
		self.label32.grid(row=3, column=0, padx=7)

		self.label33 = Label(self, text="CPU Optimized", bg=backg, fg=foreg, font=my_font)
		self.label33.grid(row=4, column=0)

		self.label34 = Label(self, text=self.google_out[1], bg=backg, fg=foreg, font=my_font)
		self.label34.grid(row=5, column=0)

		self.label35 = Label(self, text="Ram Optimized", bg=backg, fg=foreg, font=my_font)
		self.label35.grid(row=6, column=0)

		self.label36 = Label(self, text=self.google_out[2], bg=backg, fg=foreg, font=my_font)
		self.label36.grid(row=7, column=0)

		self.label37 = Label(self, text="Amazon EC2", bg=backg, fg=foreg, font=minor_font)
		self.label37.grid(row=2, column=1)

		self.amazon_out = machines.get_all_amazon()
		self.label38 = Label(self, text=self.amazon_out[0], bg=backg, fg=foreg, font=my_font)
		self.label38.grid(row=3, column=1, padx=7)

		self.label39 = Label(self, text="CPU Optimized", bg=backg, fg=foreg, font=my_font)
		self.label39.grid(row=4, column=1)

		self.label40 = Label(self, text=self.amazon_out[1], bg=backg, fg=foreg, font=my_font)
		self.label40.grid(row=5, column=1)

		self.label41 = Label(self, text="Ram Optimized", bg=backg, fg=foreg, font=my_font)
		self.label41.grid(row=6, column=1)

		self.label42 = Label(self, text=self.amazon_out[2], bg=backg, fg=foreg, font=my_font)
		self.label42.grid(row=7, column=1)

		self.label43 = Label(self, text="MiServer", bg=backg, fg=foreg, font=minor_font)
		self.label43.grid(row=2, column=2)

		self.miserver_out = machines.get_all_miserver()
		self.label44 = Label(self, text=self.miserver_out, bg=backg, fg=foreg, font=my_font)
		self.label44.grid(row=3, column=2, padx=7)

	def go_home(self):
		self.par_controller.reset_frame(ComputingAll)
