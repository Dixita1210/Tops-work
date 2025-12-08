class ClinicAppointment:
    def __init__(self):
        self.appointments = []

    def bookApprointment(self, dict1):
        self.dr_dict = dict1

        name = input("Enter patient Name: ")
        try:
            age = int(input("Enter Age: "))
            mobile_num =(input("Enter Mobile number: "))
            if len(mobile_num) !=10 or not mobile_num.isdigit():
                print('Enter 10 digit mobile number!')
                return 
        except ValueError:
            print(" Age must be numbers!")
            return


        
        print("\nAvailable Doctors:")
        for key, value in dict1.items():
            for dr_name in value:
                print(f"{key}) {dr_name}")

        doc_choice = int(input("Enter preferred Doctor Number: "))

        if doc_choice in dict1:
            doctor_info = dict1[doc_choice] #to store the selected dr info
            doctor_name = list(doctor_info.keys())[0] #first it will give all keys of dict which is doctors name then it will convert into list then [0] will give indexing 0
            print(f"\nSelected Doctor: {doctor_name}")

            slot_list = list(doctor_info[doctor_name].keys())

            print("\nAvailable Slots:")
            i = 1 #to give a numbering to each time 
            for slot in slot_list:
                print(f"{i} {slot}")
                i+=1
    
            slot_choice = int(input("\nEnter Slot Number: "))
            time_slot = slot_list[slot_choice - 1]
            result=self.checkAvaibility(doc_choice, doctor_name, time_slot)
            if result == self.dr_dict:
                self.appointments.append({
                "name": name,
                "age": age,
                "mobile": mobile_num,
                "doctor": doctor_name,
                "slot": time_slot
            })

            print("\n Appointment Booked Successfully!")
            print(f"Patient: {name} | Age: {age} | Mobile: {mobile_num}")
            print(f"Doctor: {doctor_name} | Slot: {time_slot}")
        else:
            print("\n Slot Full! Try another slot.")

        
        print("\nUpdated Doctor Slots:")
        print(self.dr_dict)


    def checkAvaibility(self, doctor_choice, doctor_name, time_slot):
        no_of_slots = self.dr_dict[doctor_choice][doctor_name][time_slot]
        print(f"Current bookings in this slot: {no_of_slots}")

        if no_of_slots < 3:
            self.dr_dict[doctor_choice][doctor_name][time_slot] = no_of_slots + 1
            return self.dr_dict
        else:
            return "Slots are already Booked Please selct other slots"
        

    def viewAppointment(self):
        try:
            mob =(input("\nEnter Mobile Number to view Appointment: "))
            if len(mob)!=10:
                print('Enter valid number')
        except ValueError:
            print(" Enter valid number!")
            return

        found = False
        for app in self.appointments:
            if app["mobile"] == mob:
                found = True
            print("\n Appointment Details:")
            print(f"Name: {app['name']}")
            print(f"Age: {app['age']}")
            print(f"Mobile: {app['mobile']}")
            print(f"Doctor: {app['doctor']}")
            print(f"Slot: {app['slot']}")

        if not found:
            print(" No appointment found for this number!")

            
    def cancelAppointment(self):
        try:
            mob =(input("\nEnter Mobile Number to cancel Appointment: "))
            if len(mob)!=10:
                print('Enter valid number')
        except ValueError:
            print(" Enter valid number!")
            return

        for app in self.appointments:
            if app["mobile"] == mob:
                # Reduce count back in doctor dict
                for key, doc in self.dr_dict.items():
                    if app["doctor"] in doc:
                        self.dr_dict[key][app["doctor"]][app["slot"]] -= 1

                self.appointments.remove(app)
                print("\n Appointment Cancelled Successfully!")
                return

        print(" No appointment found with this number!")




dict1 = {
    1: {'Mr. Patel': {'10 am': 0, '11 am': 0, '2 pm': 0}},
    2: {'Mr. Shah': {'11 am': 0, '12 am': 0, '2 pm': 0}},
    3: {'Mr. modi': {'10 am': 0, '11 am': 0}}
}

obj = ClinicAppointment()

while True:
    print("\n1. Book Appointment")
    print("2. View Appointment")
    print("3. Cancel Appointment")
    print("4. Exit")

    try:
        ch = int(input("Enter your choice: "))
    except ValueError:
        print(" Enter valid number!")
        continue

    match ch:
        case 1: obj.bookApprointment(dict1)
        case 2: obj.viewAppointment()
        case 3: obj.cancelAppointment()
        case 4:
            print("Exiting...")
            break
        case _: print("Invalid Choice!")