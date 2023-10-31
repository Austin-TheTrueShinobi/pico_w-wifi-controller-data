import socket
import redis

# Redis connection setup
redis_host = 'localhost'  # Redis server address
redis_port = 6379          # Redis server port
redis_db = 0               # Redis database index

# UDP server setup
udp_host = '0.0.0.0'      # Listen on all available interfaces
udp_port = 4242            # UDP port to listen on
buffer_size = 1024         # Size of the receive buffer

# Create a UDP socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind((udp_host, udp_port))

# Connect to Redis
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db)

print(f"Listening for UDP packets on port {udp_port}...")

while True:
    data, addr = udp_socket.recvfrom(buffer_size)  # Receive UDP data and sender's address
    data_str = data.decode('utf-8')               # Assuming data is in UTF-8 encoding
    print(f"Received UDP packet from {addr}: {data_str}")

    # Store data into Redis
    try:
        redis_client.lpush('udp_packets', data_str)  # Store data into a Redis list called 'udp_packets'
        print("Data stored in Redis.")
    except Exception as e:
        print(f"Failed to store data in Redis: {e}")

# Close the UDP socket (this part of the code is unreachable in this example)
udp_socket.close()
