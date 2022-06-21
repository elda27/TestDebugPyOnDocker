import time


def main():
    print("Started!")
    for i in range(10000):
        print(f"Sleeping: {i}")
        time.sleep(1)


if __name__ == "__main__":
    main()
