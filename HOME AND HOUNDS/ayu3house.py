import datetime

class LocalServiceApp:
    """
    A simple, terminal-based application for a local service business.
    It features service highlights, testimonials, and a booking form.
    """

    def __init__(self):
        # Data structure to hold booked appointments (in-memory storage)
        self.bookings = []

        # Static content for the application (UPDATED)
        self.services = {
            1: "🏠 Home Repair: Minor fixes, plumbing, electrical checks.",
            2: "🧹 Home Cleaning: Deep cleaning (includes kitchen and washroom), weekly/bi-weekly residential services.",
            3: "🐾 Pet Care: Dog walking, in-home feeding, pet body care (grooming/bathing), and overnight sitting."
        }

        #  testimonials with  names (Piyush, Roshni, Arya, Vanya)
        self.testimonials = [
            "⭐⭐⭐⭐⭐ - 'The cleaning crew was fast, thorough, and very professional. Highly recommend!' - Piyush chutkuuuuuuuuu ismall baby of daddy ",
            "⭐⭐⭐⭐⭐ - 'Fixed my leaky faucet the same day I called. Excellent home repair service.' - Roshni",
            "⭐⭐⭐⭐⭐ - 'My dog loves the walker! Great communication and very reliable pet care.' - Arya",
            "⭐⭐⭐⭐⭐ - 'Amazing deep clean before our party. Everything sparkled and the team was efficient.' - Vanya"
        ]
        self.app_title = "Local Community Services Hub"

    def _header(self, title):
        """Prints a standardized header for sections."""
        print("\n" + "=" * 60)
        print(f"|{title.center(58)}|")
        print("=" * 60)

    def display_highlights(self):
        """Displays the list of services offered."""
        self._header("SERVICE HIGHLIGHTS")
        print("We cover all your needs with professional, local experts:\n")
        for num, desc in self.services.items():
            print(f"  [{num}] {desc}")
        print("\n" + "-" * 60)
        input("Press Enter to return to the menu...")

    def display_testimonials(self):
        """Displays client testimonials."""
        self._header("CLIENT TESTIMONIALS")
        for testimonial in self.testimonials:
            print(f"\n{testimonial}")
        print("\n" + "-" * 60)
        input("Press Enter to return to the menu...")

    def booking_form(self):
        """Guides the user through the booking process."""
        self._header("BOOK A SERVICE")
        print("Please provide the required details below.")

        # --- 1. Service Selection ---
        print("\nAvailable Services:")
        for num, desc in self.services.items():
            print(f"  {num}. {desc.split(':')[0]}")

        while True:
            try:
                service_choice = int(input("\nEnter the number of the service you want to book (1-3): "))
                if service_choice in self.services:
                    service_name = self.services[service_choice].split(':')[0].strip()
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 3.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        # --- 2. Gathering Details ---
        name = input("Your Full Name: ").strip()
        while not name:
            name = input("Name cannot be empty. Your Full Name: ").strip()

        phone = input("Contact Phone Number: ").strip()
        # Simple phone validation (non-empty and mostly digits)
        while not phone or not phone.replace('-', '').isdigit():
             phone = input("Invalid phone. Please enter a valid number: ").strip()

        address = input("Service Address: ").strip()
        while not address:
            address = input("Address cannot be empty. Service Address: ").strip()

        # --- 3. Date and Time Suggestion ---
        print("\n--- Preferred Timing ---")
        date_input = input("Preferred Date (DD/MM/YYYY): ").strip()
        time_input = input("Preferred Time (e.g., 10:00 AM): ").strip()

        # --- 4. Confirmation and Storage ---
        new_booking = {
            "id": len(self.bookings) + 1,
            "service": service_name,
            "client_name": name,
            "contact_phone": phone,
            "address": address,
            "preferred_date": date_input,
            "preferred_time": time_input,
            "status": "Pending",
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        self.bookings.append(new_booking)

        self._header("BOOKING CONFIRMATION")
        print(f"Thank you, {name}! Your booking for {service_name} has been submitted.")
        print(f"Reference ID: {new_booking['id']}")
        print(f"We will contact you at {phone} within 2 hours to confirm the details.")
        print("\n" + "-" * 60)
        input("Press Enter to return to the menu...")

    def display_all_bookings(self):
        """
        Internal function to display all stored bookings.
        In a real app, only an admin would see this.
        """
        self._header("VIEW ALL BOOKINGS (Admin View)")
        if not self.bookings:
            print("No bookings have been made yet.")
            print("\n" + "-" * 60)
            input("Press Enter to return to the menu...")
            return

        for booking in self.bookings:
            print("-" * 60)
            print(f"ID: {booking['id']} | Status: {booking['status']}")
            print(f"Service: {booking['service']}")
            print(f"Client: {booking['client_name']} (Tel: {booking['contact_phone']})")
            print(f"Address: {booking['address']}")
            print(f"Requested: {booking['preferred_date']} at {booking['preferred_time']}")
        print("-" * 60)
        input("Press Enter to return to the menu...")


    def main_menu(self):
        """The main navigation loop for the application."""
        while True:
            self._header(self.app_title)
            print("Please select an option:")
            print("  [1] View Service Highlights")
            print("  [2] Read Client Testimonials")
            print("  [3] Book a Service (Form)")
            print("  [4] EXIT Application")
            # print("  [9] View all bookings (Debug)") # Optional debug feature

            choice = input("\nEnter your choice (1-4): ").strip()

            if choice == '1':
                self.display_highlights()
            elif choice == '2':
                self.display_testimonials()
            elif choice == '3':
                self.booking_form()
            # elif choice == '9': # Debug view
            #     self.display_all_bookings()
            elif choice == '4':
                print("\nThank you for using our service hub. we look forward to serve you next time")
                break
            else:
                print("\nInvalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    # Create an instance of the application and start the main menu
    app = LocalServiceApp()
    app.main_menu()