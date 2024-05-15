class ParkingGarage:
     def __init__(self, max_tickets):       
        self.tickets = list(range(1, max_tickets + 1))
        self.parkingSpaces = list(range(1, max_tickets + 1))
        self.currentTicket = {}

     def takeTicket(self):
        if self.tickets:
            ticket_number = self.tickets.pop(0)
            parking_space = self.parkingSpaces.pop(0)
            self.currentTicket[ticket_number] = {
                'paid': False,
                'parking_space': parking_space
            }
            print(f"Your ticket is #{ticket_number}")
        else:
            print("Sorry, the parking garage is full.")

     def payForParking(self):
        ticket_number = input("What is your ticket #?\n'0' to quit\n")
        ticket_number = int(ticket_number)
        if ticket_number == 0:
            return

        if ticket_number in self.currentTicket:
            if not self.currentTicket[ticket_number]['paid']:
               
                amount = input("Your ticket # is {} is that correct? Y/N ".format(ticket_number))
                if amount.lower() == 'y':
                    payment_method = input("Your total is $15\nDebit or Credit?\n")
                    if payment_method.lower() in ['debit', 'credit']:
                        self.currentTicket[ticket_number]['paid'] = True
                        print("Thank you for your payment")
                    else:
                        print("Invalid payment method.")
                else:
                    print("Payment canceled.")
            else:
                print("This ticket has already been paid.")
        else:
            print("Invalid ticket number.")

     def leaveGarage(self):
        ticket_number = input("What is your ticket #?\n'0' to quit\n")
        ticket_number = int(ticket_number)
        if ticket_number == 0:
            return

        if ticket_number in self.currentTicket:
            if self.currentTicket[ticket_number]['paid']:
              
                self.parkingSpaces.append(self.currentTicket[ticket_number]['parking_space'])  
                del self.currentTicket[ticket_number]
            else:
                print("Please pay for your ticket first.")
        else:
            print("Invalid ticket number.")

     def showSpaces(self):
        
        print("Parking Spaces Left:", len(self.parkingSpaces))

     def menu(self):
        while True:
            print("What would you like to do?\n 'Show Spaces'/'Take Ticket'/'Pay Ticket'/'Leave'/'Quit'")
            choice = input().lower()

            if choice == 'show spaces':
                self.showSpaces()
            elif choice == 'take ticket':
                self.takeTicket()
            elif choice == 'pay ticket':
                self.payForParking()
            elif choice == 'leave':
                self.leaveGarage()
            elif choice == 'quit':
                break
            else:
                print("Invalid choice. Please try again.")



if __name__ == "main":
    max_tickets = 10
    garage = ParkingGarage(max_tickets)
    garage.menu()
