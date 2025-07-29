import random

# List of 60 questions with choices and correct answers
questions = [
    
    {
        "question": "What does CPU stand for?",
        "options": ["Central Process Unit", "Central Processing Unit", "Computer Personal Unit", "Central Processor Unit"],
        "answer": "Central Processing Unit"
    },
    {
        "question": "What is the main purpose of RAM in a computer?",
        "options": ["Permanent storage", "Temporary storage for active processes", "Graphic rendering", "Power supply"],
        "answer": "Temporary storage for active processes"
    },
    {
        "question": "Which language is primarily used for writing web pages?",
        "options": ["Python", "HTML", "C++", "Java"],
        "answer": "HTML"
    },
    {
        "question": "What does 'HTTP' stand for?",
        "options": ["HyperText Transfer Protocol", "HyperText Transmission Protocol", "Hyper Tool Transfer Protocol", "HyperText Transfer Program"],
        "answer": "HyperText Transfer Protocol"
    },
    {
        "question": "Which of the following is an operating system?",
        "options": ["Python", "Windows", "HTML", "Google"],
        "answer": "Windows"
    },
    {
        "question": "What is a database?",
        "options": ["A type of programming language", "A collection of data", "An operating system", "A web browser"],
        "answer": "A collection of data"
    },
    {
        "question": "What does 'GUI' stand for?",
        "options": ["Graphical User Interface", "General User Interaction", "Graphic Utility Interface", "Grand User Interface"],
        "answer": "Graphical User Interface"
    },
    {
        "question": "Which device is used to input data into a computer?",
        "options": ["Monitor", "Keyboard", "Printer", "Speaker"],
        "answer": "Keyboard"
    },
    {
        "question": "Which of the following is NOT a programming language?",
        "options": ["Java", "HTML", "Python", "C++"],
        "answer": "HTML"
    },
    {
        "question": "What is the full form of 'USB'?",
        "options": ["Universal Serial Bus", "Unilateral Serial Bus", "Universal System Block", "United Serial Bus"],
        "answer": "Universal Serial Bus"
    },
    {
        "question": "What does IP stand for in networking?",
        "options": ["Internet Provider", "Internet Protocol", "Internal Procedure", "Internet Process"],
        "answer": "Internet Protocol"
    },
    {
        "question": "Which protocol is used to send emails?",
        "options": ["SMTP", "FTP", "HTTP", "DNS"],
        "answer": "SMTP"
    },
    {
        "question": "What component is referred to as the 'brain' of a computer?",
        "options": ["Hard Drive", "CPU", "RAM", "Monitor"],
        "answer": "CPU"
    },
    {
        "question": "In which memory is data stored permanently?",
        "options": ["RAM", "ROM", "Cache", "Register"],
        "answer": "ROM"
    },
    {
        "question": "Which one is a software?",
        "options": ["Monitor", "Keyboard", "Windows 10", "Mouse"],
        "answer": "Windows 10"
    },
    {
        "question": "Which of the following is a search engine?",
        "options": ["Google", "Internet Explorer", "Python", "HTML"],
        "answer": "Google"
    },
    {
        "question": "What is the function of a firewall in a computer network?",
        "options": ["To store data", "To protect against unauthorized access", "To speed up the connection", "To manage hardware"],
        "answer": "To protect against unauthorized access"
    },
    {
        "question": "Which company developed the Windows operating system?",
        "options": ["Apple", "Microsoft", "Google", "IBM"],
        "answer": "Microsoft"
    },
    {
        "question": "What is the main language used for Android app development?",
        "options": ["Swift", "Java", "C#", "HTML"],
        "answer": "Java"
    },
    {
        "question": "Which of these is a type of computer memory?",
        "options": ["SSD", "HDD", "RAM", "ROM"],
        "answer": "RAM"
    },
    {
        "question": "What does SQL stand for?",
        "options": ["Structured Query Language", "Strong Question Language", "Simple Query Language", "Structured Question Language"],
        "answer": "Structured Query Language"
    },
    {
        "question": "What does 'Wi-Fi' stand for?",
        "options": ["Wireless Fidelity", "Wireless File", "Wide Fidelity", "Wide File"],
        "answer": "Wireless Fidelity"
    },
    {
        "question": "What is the URL of a website used for?",
        "options": ["To identify the website's address", "To store web files", "To host web pages", "To program websites"],
        "answer": "To identify the website's address"
    },
    {
        "question": "Which tag is used to insert a hyperlink in HTML?",
        "options": ["<link>", "<a>", "<href>", "<hyperlink>"],
        "answer": "<a>"
    },
    {
        "question": "Which part of the computer is responsible for graphics rendering?",
        "options": ["CPU", "GPU", "RAM", "Hard Drive"],
        "answer": "GPU"
    },
    {
        "question": "Which of the following is NOT a type of software license?",
        "options": ["GPL", "MIT", "HTML", "Apache"],
        "answer": "HTML"
    },
    {
        "question": "Which protocol is used for secure communication over the internet?",
        "options": ["HTTP", "FTP", "HTTPS", "SMTP"],
        "answer": "HTTPS"
    },
    {
        "question": "What does 'IDE' stand for in programming?",
        "options": ["Integrated Development Environment", "Internal Debugging Environment", "Integrated Design Emulator", "Internal Design Environment"],
        "answer": "Integrated Development Environment"
    },
    {
        "question": "Which of these is a cloud computing platform?",
        "options": ["AWS", "HTTP", "HTML", "IP"],
        "answer": "AWS"
    },
    {
        "question": "What is the binary number system based on?",
        "options": ["Base 8", "Base 10", "Base 2", "Base 16"],
        "answer": "Base 2"
    },
   
    {
        "question": "Who is known as the 'Father of Computers'?",
        "options": ["Alan Turing", "Charles Babbage", "Bill Gates", "Steve Jobs"],
        "answer": "Charles Babbage"
    },
    {
        "question": "What does 'HTML' stand for?",
        "options": ["HyperText Markup Language", "HyperText Machine Language", "HyperTool Multi Language", "HighText Markup Language"],
        "answer": "HyperText Markup Language"
    },
    {
        "question": "Which device translates data from analog to digital form?",
        "options": ["Modem", "Router", "Switch", "Bridge"],
        "answer": "Modem"
    },
    {
        "question": "What is the function of the ALU in a CPU?",
        "options": ["Memory Storage", "Arithmetic and Logic Operations", "Data Input", "Data Output"],
        "answer": "Arithmetic and Logic Operations"
    },
    {
        "question": "Which type of software controls the computer hardware?",
        "options": ["Application software", "System software", "Utility software", "Middleware"],
        "answer": "System software"
    },
    {
        "question": "Which of the following is an example of an input device?",
        "options": ["Printer", "Monitor", "Scanner", "Speaker"],
        "answer": "Scanner"
    },
    {
        "question": "What is the abbreviation of BIOS?",
        "options": ["Basic Input Output System", "Binary Input Output System", "Basic Integrated Operating System", "Binary Integrated Operating System"],
        "answer": "Basic Input Output System"
    },
    {
        "question": "Which language is considered a low-level programming language?",
        "options": ["Java", "Assembly", "Python", "Ruby"],
        "answer": "Assembly"
    },
    {
        "question": "What does 'URL' stand for?",
        "options": ["Uniform Resource Locator", "Universal Resource Locator", "Uniform Reference Link", "Universal Reference Link"],
        "answer": "Uniform Resource Locator"
    },
    {
        "question": "What is the main purpose of an IP address?",
        "options": ["Identify a website", "Identify a computer on a network", "Encrypt data", "Send emails"],
        "answer": "Identify a computer on a network"
    },
    {
        "question": "Which of these is an open-source operating system?",
        "options": ["Windows", "macOS", "Linux", "iOS"],
        "answer": "Linux"
    },
    {
        "question": "What does SSD stand for in computer storage?",
        "options": ["Solid State Drive", "Solid Storage Disk", "System Storage Drive", "Streamlined State Disk"],
        "answer": "Solid State Drive"
    },
    {
        "question": "Which protocol is used to transfer files over the internet?",
        "options": ["HTTP", "FTP", "SMTP", "POP3"],
        "answer": "FTP"
    },
    {
        "question": "What does 'CSS' stand for in web design?",
        "options": ["Cascading Style Sheets", "Computer Style Sheets", "Creative Style System", "Colorful Style Sheets"],
        "answer": "Cascading Style Sheets"
    },
    {
        "question": "Which component stores data temporarily while the computer is on?",
        "options": ["ROM", "RAM", "Hard Drive", "Cache"],
        "answer": "RAM"
    },
    {
        "question": "Who founded Microsoft?",
        "options": ["Steve Jobs", "Bill Gates", "Mark Zuckerberg", "Larry Page"],
        "answer": "Bill Gates"
    },
    {
        "question": "What is the purpose of an IP router?",
        "options": ["Store data", "Direct network traffic", "Translate languages", "Secure a network"],
        "answer": "Direct network traffic"
    },
    {
        "question": "Which of these is NOT a programming paradigm?",
        "options": ["Object-oriented", "Functional", "Procedural", "Analog"],
        "answer": "Analog"
    },
    {
        "question": "Which command is used to display the contents of a directory in a command prompt?",
        "options": ["dir", "cd", "ls", "mkdir"],
        "answer": "dir"
    },
    {
        "question": "Which system uses binary digits?",
        "options": ["Decimal", "Hexadecimal", "Binary", "Octal"],
        "answer": "Binary"
    },
    {
        "question": "Which software is used to browse the Internet?",
        "options": ["Word Processor", "Web Browser", "Spreadsheet", "Email Client"],
        "answer": "Web Browser"
    },
    {
        "question": "What is a 'bit' in computing?",
        "options": ["A unit of data", "A programming language", "A network device", "A software program"],
        "answer": "A unit of data"
    },
    {
        "question": "Which of these is NOT part of the CPU?",
        "options": ["ALU", "CU", "RAM", "Registers"],
        "answer": "RAM"
    },
    {
        "question": "What type of device is a USB flash drive?",
        "options": ["Primary memory", "Secondary storage", "Input device", "Output device"],
        "answer": "Secondary storage"
    },
    {
        "question": "Which of the following is a markup language?",
        "options": ["Python", "HTML", "Java", "C++"],
        "answer": "HTML"
    },
    {
        "question": "What is the main purpose of DNS?",
        "options": ["Translate domain names to IP addresses", "Send emails", "Manage databases", "Filter network traffic"],
        "answer": "Translate domain names to IP addresses"
    },
    {
        "question": "Which company created the iPhone?",
        "options": ["Google", "Samsung", "Apple", "Microsoft"],
        "answer": "Apple"
    },
]

def run_quiz():
    print("Welcome to the Computer Quiz App. Developed by Joseph Ajireloja!")
    user_name = input("Please enter your name: ").strip()
    if not user_name:
        user_name = "User"
    score = 0

    # Randomly select 10 questions from the 60 available questions
    selected_questions = random.sample(questions, 10)

    for i, q in enumerate(selected_questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        options = q['options']
        # Shuffle options to make quiz less predictable
        random.shuffle(options)
        for idx, option in enumerate(options, 1):
            print(f"  {idx}. {option}")
        while True:
            try:
                choice = int(input("Your answer (1-4): "))
                if choice < 1 or choice > 4:
                    raise ValueError
                break
            except ValueError:
                print("Please enter a valid option number between 1 and 4.")
        selected_option = options[choice - 1]
        if selected_option == q['answer']:
            print("Correct!")
            score += 10
        else:
            print(f"Wrong! The correct answer is: {q['answer']}")

    print(f"\nQuiz Completed! {user_name}, your score is {score} out of 100.")

def main():
    while True:
        run_quiz()
        retry = input("\nDo you want to try the quiz again? (yes/no): ").strip().lower()
        if retry not in ('yes', 'y'):
            print("Thank you for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()
