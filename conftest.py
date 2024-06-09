
# Add the driver option to the command line and it's requirements
def pytest_addoption(parser):
    parser.addoption(
        "--driver",
        "-D",
        action="store",
        choices=["chrome", "edge", "firefox", "safari"],
        help="Select which driver to use for the program.",
        metavar="driver",
        required=False,
        type=str
        )

    parser.addoption(
        "--month",
        "-M",
        action="store",
        choices=[
            "januari",
            "jan",
            "februari",
            "feb",
            "mars"
            "mar",
            "april",
            "apr",
            "maj",
            "juni"
            "jun",
            "juli",
            "jul",
            "augusti",
            "aug",
            "september",
            "sep",
            "oktober",
            "okt",
            "november",
            "nov",
            "december"
            "dec"
            ],
        help="Select which month the program should use.",
        metavar="month",
        required=False,
        type=str
        )

    parser.addoption(
        "--login",
        "-L",
        action="store",
        choices=["bankid", "freja", "id", "foreignid", "password"],
        help="Select which login option to use.",
        metavar="login",
        required=False,
        type=str
        )


    parser.addoption(
        "--options",
        "-O",
        action="store",
        choices=["work", "inter", "all"],
        default="all",
        help="Select if you want to see Work, interviews or all?",
        metavar="login",
        required=False,
        type=str
        )
