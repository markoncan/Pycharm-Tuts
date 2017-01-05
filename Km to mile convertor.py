def main():
    print("Speed_in-KM\tSpeed_in_Miles")
    print("-----------------------")
    for speed_in_Km in range(10,50,10):
        speed_in_miles=speed_in_Km*0.6214
        print(speed_in_Km,'\t','\t',format(speed_in_miles,'1f'))
main()