import random
from datetime import datetime
USERNAME = "hardik"
PASSWORD = "Hardik123"
KNOWN_DEVICES = {"Laptop-123"}
DEMO_LOCATION = "India-Lucknow"
BUSINESS_HOURS =(6, 22)
def now_str():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
def print_header():
    print("="*64)
    print("Adaptive 2FA demo(console)".center (64, "=" ))
    print("=" * 64)
def biometric_flow(device,reasons):
    print("\n[2FA] HIGH RISK → Biometric Authentication Required")
    print(f"[Reasons] {', '.join(reasons)}")
    entered = input("Type BIOMETRIC_OK to pass authentication:").strip()
    if entered == "BIOMETRIC_OK":
        if device:
                KNOWN_DEVICES.add(device)
                print("\n[LOGIN]Success !(Biometric verified)")
                print(f"[INFO]Time: {now_str()}Location: {device or 'Unknown'}")
        else:
            print("[ERROR]Biometric Authentication Failed! Login denied.")
def otp_flow(device, reasons):
        otp = str(random.randint(100000,999999))
        print("\n[2FA]MEDIUM RISK-OTP required")
        print(f"[Reasons]{', '.join(reasons)}")
        print(f"[OTP]Your one-time code is:{otp}")
        entered = input("Enter OTP :").strip()
        if entered == otp:
           KNOWN_DEVICES.add(device)
           print("\n[LOGIN]Success !(New Device verified by OTP)")
           print(f"[INFO]Time:{now_str()}|Location:{DEMO_LOCATION} |Device:{device}")
        else:
           print("\n[ERROR]OTP Wrong OTP! Login denied.")
def low_flow(device):
      print("\n[RISK]LOW--NO2FA needed.")
      print("[LOGIN]Success !")
      print(f"[INFO]Time:{now_str()}|Location:{DEMO_LOCATION})|Device:{device}")
def main():
        print_header()
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        device = input("Device Name: ").strip()
        ip_known_raw = input("Is IP known? (Y/N): ").strip().lower()
        ip_known = (ip_known_raw == "Y")
        if not password or username != USERNAME or password != PASSWORD:
            print("\n[AUTH] incorrect Username or Password !")
            biometric_flow(device if device else"unknown device",["Wrong/Empty Password"])
            return
        reasons = []
        score = 0
        if device not in KNOWN_DEVICES:
            score += 2
            reasons.append("New Device")
        if not ip_known:
            score += 1
            reasons.append("Unknown IP")
        h1, h2 = BUSINESS_HOURS
        hour_now = datetime.now().hour
        if not(h1<=hour_now < h2):
            score += 1
            reasons.append("Odd Login Time")
        if score <= 1:
            low_flow(device or "unknown device")
        elif score <=3:
            otp_flow(device or "unknown device",reasons if reasons else ["Medium baseline"])
        else:
            biometric_flow(device or "unknown device",reasons if reasons else ["High baseline"])
if __name__ == "__main__":
      main()
