class Device:
    def __init__(self, name, buffer_size=0):
        self.name = name
        self.buffer = []
        self.buffer_size = buffer_size
        self.pause = False

    def receive_data(self, data):
        if self.pause:
            print(f"Sending paused. Buffer full for {self.name}.")
            return

        if len(self.buffer) < self.buffer_size:
            self.buffer.append(data)
            print(f"Data '{data}' sent to {self.name}. Current buffer: {self.buffer}")
        else:
            self.pause = True
            print(f"Buffer full for {self.name}. Data '{data}' could not be sent. Sending paused.")
    
    def clear_buffer(self):
        self.buffer = []
        self.pause = False
        print(f"Buffer cleared for {self.name}. Device resumed for data receiving.")


class Switch:
    def __init__(self, name, connections=None):
        self.name = name
        self.connections = connections if connections else {}

    def add_connection(self, sender, receiver):
        self.connections[(sender, receiver)] = True

    def display_connections(self):
        print(f"Connections for {self.name}:")
        for pair in self.connections:
            print(f"  {pair[0].name} -> {pair[1].name}")

def throughput(switches):
    receiver_count = {}
    for switch in switches:
        for sender, receiver in switch.connections:
            if receiver is not Y: 
                if receiver in receiver_count:
                    receiver_count[receiver] += 1
                else:
                    receiver_count[receiver] = 1

    for receiver, count in receiver_count.items():
        if receiver is S1:
                print(f"Throughput for devices sending to Y: {1/count:.2f}")
        else:
                print(f"\nThroughput for devices sending to {receiver.name}: {1/count:.2f}")
        
        
def send_data_loop(sender, receiver):
    data_count = 1
    if not receiver.pause:
        data = f'Data{data_count} from {sender.name}'
        print(f"{sender.name} attempts to send '{data}' to {receiver.name}.")
        receiver.receive_data(data)
        data_count += 1

def clear_buffers(devices):
    for device in devices:
        device.clear_buffer()
        
# Setup devices
A = Device('A')
B = Device('B')
C = Device('C')
D = Device('D', buffer_size=3)
X = Device('X')
Y = Device('Y', buffer_size=3)
S2_device = Device('S2')  # Used as a conceptual pass-through

# Setup switches with connections
S2 = Switch('S2')
S1 = Switch('S1', {(A, D): True, (B, D): True, (S2, Y): True})
S2 = Switch('S2', {(C, D): True, (X, Y): True, (C, S1): True, (X, S1): True})

# Display connections
S1.display_connections()
S2.display_connections()

# Calculate and display throughput
print("\nThroughput Calculations:")
throughput([S1, S2])

# Example of sending loop
print("\nSending data from A to D:")
send_data_loop(A, D)
print("\nSending data from B to D:")
send_data_loop(B, D)
print("\nSending data from C to D:")
send_data_loop(C, D)
print("\nSending data from A to D:")
send_data_loop(A, D)
print("\nSending data from X to Y:")
send_data_loop(X, Y)

print("\n\n!!!PLEASE NOTE the above C device is being considered as C0, therefore I am adding C1 to C7 to represent the other 8 devices that replace C0!!!\n\n")
print("\nAdding other C devices C1 to C7:")
print("\nAdding C1: \n\n")
#Adding the other devices from Cn where n -> (2,8) 

C1 = Device('C1')
S2 = Switch('S2', {(C, D): True, (X, Y): True, (C, S1): True, (X, S1): True,(C1, D): True, (C1, S1): True})

S2.display_connections()
throughput([S1, S2])

print("\nAdding C2: \n\n")

C2 = Device('C2')
S2 = Switch('S2', {(C, D): True, (X, Y): True, (C, S1): True, (X, S1): True,(C1, D): True, (C1, S1): True, (C2, D): True, (C2, S1): True})

S2.display_connections()
throughput([S1, S2])


print("\nAdding C3: \n\n")

C3 = Device('C3')
S2 = Switch('S2', {(C, D): True, (X, Y): True, (C, S1): True, (X, S1): True,(C1, D): True, (C1, S1): True, (C2, D): True, (C2, S1): True, (C3, D): True, (C3, S1): True})

S2.display_connections()
throughput([S1, S2])


print("\nAdding C4: \n\n")

C4 = Device('C4')
S2 = Switch('S2', {(C, D): True, (X, Y): True, (C, S1): True, (X, S1): True,(C1, D): True, (C1, S1): True, (C2, D): True, (C2, S1): True, (C3, D): True, (C3, S1): True, (C4, D): True, (C4, S1): True})

S2.display_connections()
throughput([S1, S2])


print("\nAdding C5: \n\n")

C5 = Device('C5')
S2 = Switch('S2', {(C, D): True, (X, Y): True, (C, S1): True, (X, S1): True,(C1, D): True, (C1, S1): True, (C2, D): True, (C2, S1): True, (C3, D): True, (C3, S1): True, (C4, D): True, (C4, S1): True, (C5, D): True, (C5, S1): True})

S2.display_connections()
throughput([S1, S2])


print("\nAdding C6: \n\n")

C6 = Device('C6')
S2 = Switch('S2', {(C, D): True, (X, Y): True, (C, S1): True, (X, S1): True,(C1, D): True, (C1, S1): True, (C2, D): True, (C2, S1): True, (C3, D): True, (C3, S1): True, (C4, D): True, (C4, S1): True, (C5, D): True, (C5, S1): True, (C6, D): True, (C6, S1): True})

S2.display_connections()
throughput([S1, S2])


print("\nAdding C7: \n\n")

C7 = Device('C7')
S2 = Switch('S2', {(C, D): True, (X, Y): True, (C, S1): True, (X, S1): True,(C1, D): True, (C1, S1): True, (C2, D): True, (C2, S1): True, (C3, D): True, (C3, S1): True, (C4, D): True, (C4, S1): True, (C5, D): True, (C5, S1): True, (C6, D): True, (C6, S1): True, (C7, D): True, (C7, S1): True})

S2.display_connections()
throughput([S1, S2])

print("\nClearning Buffers")
clear_buffers([D, Y])

#print("\nSending data from A to D:")
#send_data_loop(A, D)
#print("\nSending data from B to D:")
#send_data_loop(B, D)
#print("\nSending data from C to D:")
#send_data_loop(C, D)
#print("\nSending data from A to D:")
#send_data_loop(A, D)




