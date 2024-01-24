import ipaddr


def overlap(n1, n2):
    return n1.overlaps(n2)


def main():
    print("Hello World!")
    print(overlap(ipaddr.IPNetwork('192.168.1.0/24'), ipaddr.IPNetwork('192.168.2.0/24')))  # should be False
    print(overlap(ipaddr.IPNetwork('192.168.1.0/24'), ipaddr.IPNetwork('192.168.2.0/25')))  # should be False
    print(overlap(ipaddr.IPNetwork('10.0.0.0/16'), ipaddr.IPNetwork('10.1.0.0/16')))  # should be False
    print("Program finished!")


if __name__ == "__main__":
    main()
