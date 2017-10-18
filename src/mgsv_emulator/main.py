from processor.CommandProcessor import CommandProcessor

def main(request):
    processor = CommandProcessor()
    result = processor.process(request)
    print(result)

if __name__ == "__main__":
        s = "YnHdLj/1b4RBZXynl0xG1B0domEayp/1lLk99kX4wjo7NblxIkhv1ByeVvdNenjEJTavALlsfZfSgBpLKuCMvHkaMHdNOW9g+4ytGq/cFcXOpW6W3rjoDzBVAFXLVj+HRATx/hb68EX3+00fDqDfc0/wdXEaV+G7h5Zc4M2QoF5juLcqskL1iLDYQlLVsTH5VCgC7mK204ygBrK6BopI6RZN6pX+6R+lfT/01GExQVs="
        main(s)
