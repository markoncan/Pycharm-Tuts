def main():
    print("number\tsquare")
    print("------  ------")
    for number in range(1,11):
        square=number**2
        ##"\t"#  escape characters
        print(number,'\t','\t',square)
main()