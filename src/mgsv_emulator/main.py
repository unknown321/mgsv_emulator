from processor.CommandProcessor import CommandProcessor

def main(request):
    processor = CommandProcessor()
    result = processor.process(request)
    print(result)

if __name__ == "__main__":
        main('123')
