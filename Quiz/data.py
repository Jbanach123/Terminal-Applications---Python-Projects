question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, "
             "you are free to take it home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, "
             "you are entitled to a state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

question_computer = [
    {"type": "boolean", "difficulty": "easy",
     "category": "Science: Computers",
     "question": "Linus Torvalds created Linux and Git.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
     "question": "The logo for Snapchat is a Bell.", "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
     "question": "The Python programming language gets its name from the British comedy group &quot;Monty Python.&quot;",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
     "question": "In most programming languages, the operator ++ is equivalent to the statement &quot;+= 1&quot;.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
     "question": "&quot;HTML&quot; stands for Hypertext Markup Language.", "correct_answer": "True",
     "incorrect_answers": ["False"]}, {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
                                       "question": "The NVidia GTX 1080 gets its name because it can only render at a 1920x1080 screen resolution.",
                                       "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
     "question": "The Windows 7 operating system has six main editions.", "correct_answer": "True",
     "incorrect_answers": ["False"]}, {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
                                       "question": "Time on Computers is measured via the EPOX System.",
                                       "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
     "question": "The programming language &quot;Python&quot; is based off a modified version of &quot;JavaScript&quot;.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
     "question": "RAM stands for Random Access Memory.", "correct_answer": "True", "incorrect_answers": ["False"]}]

question_animals = [{"type": "boolean", "difficulty": "medium", "category": "Animals",
                     "question": "&quot;Kamea,&quot; the Gilbertese Islander word for dog, is derived from the English phrase &quot;Come here!&quot;",
                     "correct_answer": "True", "incorrect_answers": ["False"]},
                    {"type": "boolean", "difficulty": "easy", "category": "Animals",
                     "question": "Cats have whiskers under their legs.", "correct_answer": "True",
                     "incorrect_answers": ["False"]}, {"type": "boolean", "difficulty": "easy", "category": "Animals",
                                                       "question": "A bear does NOT defecate during hibernation. ",
                                                       "correct_answer": "True", "incorrect_answers": ["False"]},
                    {"type": "boolean", "difficulty": "medium", "category": "Animals",
                     "question": "The Ceratosaurus, a dinosaur known for having a horn on the top of its nose, is also known to be a decendent of the Tyrannosaurus Rex.",
                     "correct_answer": "False", "incorrect_answers": ["True"]},
                    {"type": "boolean", "difficulty": "easy", "category": "Animals",
                     "question": "The freshwater amphibian, the Axolotl, can regrow it&#039;s limbs.",
                     "correct_answer": "True", "incorrect_answers": ["False"]},
                    {"type": "boolean", "difficulty": "medium", "category": "Animals",
                     "question": "The Platypus is a mammal.", "correct_answer": "True", "incorrect_answers": ["False"]},
                    {"type": "boolean", "difficulty": "easy", "category": "Animals",
                     "question": "Rabbits are carnivores.", "correct_answer": "False", "incorrect_answers": ["True"]},
                    {"type": "boolean", "difficulty": "medium", "category": "Animals",
                     "question": "Finnish Lapphund dogs were used for herding reindeer.", "correct_answer": "True",
                     "incorrect_answers": ["False"]}, {"type": "boolean", "difficulty": "easy", "category": "Animals",
                                                       "question": "A slug&rsquo;s blood is green.",
                                                       "correct_answer": "True", "incorrect_answers": ["False"]},
                    {"type": "boolean", "difficulty": "easy", "category": "Animals",
                     "question": "Kangaroos keep food in their pouches next to their children.",
                     "correct_answer": "False", "incorrect_answers": ["True"]},
                    {"type": "boolean", "difficulty": "easy", "category": "Animals",
                     "question": "The internet browser Firefox is named after the Red Panda.", "correct_answer": "True",
                     "incorrect_answers": ["False"]}, {"type": "boolean", "difficulty": "easy", "category": "Animals",
                                                       "question": "In 2016, the IUCN reclassified the status of Giant Pandas from endangered to vulnerable.",
                                                       "correct_answer": "True", "incorrect_answers": ["False"]},
                    {"type": "boolean", "difficulty": "easy", "category": "Animals",
                     "question": "The Killer Whale is considered a type of dolphin.", "correct_answer": "True",
                     "incorrect_answers": ["False"]}, {"type": "boolean", "difficulty": "easy", "category": "Animals",
                                                       "question": "Rabbits can see what&#039;s behind themselves without turning their heads.",
                                                       "correct_answer": "True", "incorrect_answers": ["False"]},
                    {"type": "boolean", "difficulty": "medium", "category": "Animals",
                     "question": "You can tell the age of a ladybird by counting the spots on his back.",
                     "correct_answer": "False", "incorrect_answers": ["True"]},
                    {"type": "boolean", "difficulty": "medium", "category": "Animals",
                     "question": "Tigers have one colour of skin despite the stripey fur.", "correct_answer": "False",
                     "incorrect_answers": ["True"]}, {"type": "boolean", "difficulty": "medium", "category": "Animals",
                                                      "question": "The average lifespan of a wildcat is only around 5-6 years. ",
                                                      "correct_answer": "False", "incorrect_answers": ["True"]},
                    {"type": "boolean", "difficulty": "easy", "category": "Animals",
                     "question": "The Axolotl is an amphibian that can spend its whole life in a larval state.",
                     "correct_answer": "True", "incorrect_answers": ["False"]},
                    {"type": "boolean", "difficulty": "easy", "category": "Animals", "question": "Rabbits are rodents.",
                     "correct_answer": "False", "incorrect_answers": ["True"]},
                    {"type": "boolean", "difficulty": "medium", "category": "Animals",
                     "question": "An octopus can fit through any hole larger than its beak.", "correct_answer": "True",
                     "incorrect_answers": ["False"]}]
