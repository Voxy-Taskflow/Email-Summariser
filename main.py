from src import mailExtractor



def main():
    service = mailExtractor.get_mail_service()
    mailExtractor.get_latest_emails(service)


if __name__ == "__main__":
    main()
