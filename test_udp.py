# import socket

# UDP_IP = "127.0.0.1"
# UDP_PORT = 12345

# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock.bind((UDP_IP, UDP_PORT))

# print("Waiting for OpenBCI data...")

# while True:
#     data, addr = sock.recvfrom(65535)
#     print(data.decode("utf-8", errors="replace"))




# import socket

# UDP_IP = "0.0.0.0"
# UDP_PORT = 12345

# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# sock.bind((UDP_IP, UDP_PORT))

# print("Listening for OpenBCI UDP packets...")
# print("Port:", UDP_PORT)

# while True:
#     data, addr = sock.recvfrom(65535)

#     print("PACKET RECEIVED!")
#     print("From:", addr)
#     print("Data:", data[:200])
#     print("--------------------")





# import socket
# import json
# import time

# UDP_IP = "127.0.0.1"
# UDP_PORT = 12345

# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock.bind((UDP_IP, UDP_PORT))

# print("Receiving live EEG data...")
# print("Summarizing packets (press Ctrl+C to stop)\n")

# packet_count = 0
# last_print = time.time()

# while True:
#     packet, addr = sock.recvfrom(65535)

#     try:
#         message = json.loads(packet.decode("utf-8"))
#         rows = message["data"]
#         packet_count += 1

#         if time.time() - last_print >= 1:
#             print(f"\nPackets received: {packet_count}")
#             print("Data type:", message["type"])
#             print("Number of rows:", len(rows))

#             for i, row in enumerate(rows):
#                 if row:
#                     print(
#                         f"Row {i + 1}: "
#                         f"samples={len(row)}, "
#                         f"min={min(row):.2f}, "
#                         f"max={max(row):.2f}, "
#                         f"first={row[:3]}"
#                     )

#             last_print = time.time()

#     except (ValueError, KeyError, TypeError) as e:
#         print("Could not parse packet:", e)







import socket
import json
import time
import statistics

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", 12345))

print("Live EEG channel investigation")
print("Press Ctrl+C to stop\n")

last_print = time.time()

while True:
    packet, addr = sock.recvfrom(65535)

    try:
        message = json.loads(packet.decode("utf-8"))
        rows = message["data"]

        if time.time() - last_print >= 1:

            print("\n--- LIVE SIGNALS ---")

            for i, row in enumerate(rows):
                if row and any(v != 0 for v in row):
                    print(
                        f"Row {i + 1}: "
                        f"Mean={statistics.mean(row):.2f} | "
                        f"Min={min(row):.2f} | "
                        f"Max={max(row):.2f} | "
                        f"Range={max(row)-min(row):.2f}"
                    )

            last_print = time.time()

    except (ValueError, KeyError, TypeError):
        pass
