from src import mailExtractor


def main():
    service = mailExtractor.get_mail_service()
    mailExtractor.get_latest_emails(service)
    print("Hello from email-summarizer!")


if __name__ == "__main__":
    main()
