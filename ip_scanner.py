from portscanner import run
import time

# user enter the IP addresses or websites to be scann separated with ","
targets = input("[!] Enter Website/s or IP/s to scan(use ',' for separation): ").split(",")

# user enter ports to be scanned separated with "-"
ports_to_scan = list(map(int, (input("[!] Enter ports to be scan\n"
                                     "[!] First is the port to start and second the port to end\n"
                                     "[!] Example(multiple ports) -> 1 - 10\n"
                                     "[!] Example(single port)    -> 25 \n>>> ").split("-"))))


# running the main function
# also starting time for running the script
start = time.time()
run(targets, ports_to_scan)
end = time.time()
diff = end - start

print(f"\nTime for scanning was: {diff:.2f} sec")
