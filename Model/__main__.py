import acid

def runme():
    pass

def main():
    try:
        runme()
    except IOError:
        pass
    except KeyboardInterrupt:
        sys.stdout.write("\n")


if __name__ == "__main__":
    main()

