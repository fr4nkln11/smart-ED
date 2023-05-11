"""0 1111000 1100110 1110000 1110011 - 
    A king who made this possible"""

def parse(questions: str) -> list:

    """Parses a string containing multiple-choice questions and answers, and returns a list of dictionaries
    representing each question, along with its possible answers and the correct answer.

    Args:
        questions: A string containing multiple-choice questions and answers, separated by newlines. Each
            question should start with Qn where `n` represents the question number, followed by the question text.
            The possible answers should be listed underneath the question, with each answer starting with
            a capital letter followed by a period, followed by the answer text. The correct answer should be
            listed last, starting with "Correct Answer:", followed by the correct answer letter (capitalized)
            and a period, followed by the correct answer text.

            Example:
                Q2. What does a firewall do?
                A. Monitors and controls incoming and outgoing network traffic
                B. Encrypts network data
                C. Removes malicious files from a computer
                D. Manages user accounts and permissions
                E. Displays system notifications and alerts
                Correct Answer: A. Monitors and controls incoming and outgoing network traffic

    Returns:
        A list of dictionaries representing each question, with the following keys:
            - 'question': A string representing the question text.
            - 'answers': A list of strings representing the possible answer texts.
            - 'answer': A string representing the correct answer text.

            Example:
                [
                    {
                        'question': 'Q1. What is the purpose of an antivirus software?',
                        'answers': [
                            'A. To protect against viruses and malware',
                            'B. To encrypt sensitive data',
                            'C. To monitor network traffic',
                            'D. To clean computer registry errors',
                            'E. To optimize system performance'
                        ],
                        'answer': 'A. To protect against viruses and malware'
                    }
                ]
    """

    questionsArray = []

    splitQuestions = questions.split("\n")

    questionChunkCount = len(splitQuestions) // 7

    index = 0

    while index < questionChunkCount:
        questionsObject = {
            "question": "",
            "answers": [],
            "answer": ""
        }

        questionChunk = splitQuestions[:7]
        

        questionsObject["question"] = questionChunk[0]

        answersChunk = questionChunk[1 : 6]
        for i in answersChunk:
            questionsObject["answers"].append(i)

        correct_answer = questionChunk[6]
        questionsObject["answer"] = correct_answer[16:].lstrip()
        
        questionsArray.append(questionsObject)

        splitQuestions = splitQuestions[8:]
        
        index += 1

    return questionsArray



