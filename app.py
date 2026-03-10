from std_log import Logger

def main():
    app_log = Logger(name="TestApp", dir="logs")

    app_log.file_handler()

    # Tester de ulike nivåene
    app_log.info("Dette er en info-melding")
    app_log.debug("Dette er en debug-melding")
    app_log.warn("Dette er en advarsel")
    app_log.error("Dette er en feilmelding")
    app_log.critical("Dette er en kritisk hendelse!")

    console_test()

def console_test():
    console_log = Logger(name="ConsoleTest", dir="logs")
    console_log.console_handler()

    console_log.info("Dette er en info-melding til konsollen")
    console_log.debug("Dette er en debug-melding til konsollen")
    console_log.warn("Dette er en advarsel til konsollen")
    console_log.error("Dette er en feilmelding til konsollen")
    console_log.critical("Dette er en kritisk hendelse til konsollen!")

if __name__ == "__main__":
    main()